from pathlib import Path
import os
import json
from typing import Union, Callable, Iterator, Optional
import datetime
import wandb
import fire

from vllm import LLM, SamplingParams, CompletionOutput

from evals.data_eval_utils import get_iter_for_eval_data_set, save_completions
from evals.prompts_evals import get_prob_str_minerva_prompt, extract_answer_minerva_prompt, H_MATH_MINERVA_PROMPT_TEMPLATE, H_MATH_MINERVA_PROMPT_TEMPLATE_2_BETTER, H_MATH_MINERVA_PROMPT_TEMPLATE_3_COT, get_prob_str_minerva_prompt_cot, STOP_TOKENS, extract_answer_from_list_completion_strings_mv
from evals.prompts_evals import HELM_MATH_PROMPT_8SHOT_COT2_TEMPLATE, get_math_problem_prompt_ala_helm_8shot_cot2 
from evals.utils import extract_model_answers, eval_boxed_accuracy_results, extract_gold_answers, get_dtype_for_vllm, load_model_block_size
from evals.inference_eval import VllmGenerator, inference_vllm_prompt_only, OpenAIGenerator, HFPipelineGenerator, HFDirectModelGenerator

import sys
MAX_INT = sys.maxsize

from pdb import set_trace as st

# -- tests

def main(
        # path_2_eval_dataset: str = '~/gold-ai-olympiad/data/MATH/test',
        path_2_eval_dataset: str = '~/putnam-math/data/Putnam_MATH_original_static2/test',
        # model: str = 'mistralai/Mistral-7B-Instruct-v0.1',
        model: str = 'deepseek-ai/deepseek-math-7b-instruct',
        # model: str = 'gpt2',
        # model: str = 'gpt-3.5-turbo',
        # model: str = 'gpt-4-turbo',
        output_dir: Optional[str] = '~/data/results_{today}/',  # e.g., where to save completions
        completion_filename: str = 'completions.json',
        start: int = 0, 
        end: int = sys.maxsize, 
        # end: int = 10,  # do 10 so enough boxed qs are there 
        # batch_size: int = 3,  # putnam has 348 
        batch_size: int = 10,  # putnam has 348 
        n: int = 4, # num seqs to return for given prompt
        max_tokens: int = 2048,
        # max_tokens: int = 4096,
        top_p: float = 0.95, 
        temperature: float = 0.8,
        # num_beams: int = 5,
        num_beams: Optional[int] = None,
        hf_gen_type: Optional[str] = None,
        # hf_gen_type: Optional[str] = 'pipeline',
        # hf_gen_type: Optional[str] = 'hf_direct_model_gen',
        verbose_eval: bool = True,
        # boxed_acc_probs_only: bool = False,
        boxed_acc_probs_only: bool = True,
        use_beam_search: bool = False,
        best_of: Optional[int] = None,
        mode: str = 'dryrun',  # 'dryrun' or 'online'
        # mode: str = 'online',  # 'dryrun' or 'online'
        ):
    """ """
    # - Start wandb run
    CUDA_VISIBLE_DEVICES = os.environ.get('CUDA_VISIBLE_DEVICES')
    current_tmux_session = os.environ.get("TMUX", "").split(",")[-1]
    today = datetime.datetime.now().strftime('%Y-m%m-d%d-t%Hh_%Mm_%Ss')
    run_name = f'putnam-math ({today=} {model} {path_2_eval_dataset} {CUDA_VISIBLE_DEVICES=} {current_tmux_session=})'
    run = wandb.init(mode=mode, project="putnam-math", name=run_name, save_code=True)
    print(f'{run.url=}')
    output_dir = Path(f'~/data/results_{today}/').expanduser() 
    output_dir.mkdir(parents=True, exist_ok=True)

    # - Get eval data
    path_2_eval_dataset: Path = Path(path_2_eval_dataset).expanduser()
    math_gold_probs_solns: list[dict] = list(get_iter_for_eval_data_set(path_2_eval_dataset))
    print(f'{len(math_gold_probs_solns)=}')
    math_gold_probs_solns: list[dict] = math_gold_probs_solns[start:end]
    print(f'{len(math_gold_probs_solns)=}')
    # filter out all dicts that don't have a latex box
    if boxed_acc_probs_only:
        math_gold_probs_solns = [d for d in math_gold_probs_solns if '\\boxed' in d['solution'] or '\\fbox' in d['solution']] 
    print(f'{path_2_eval_dataset=} \n {len(math_gold_probs_solns)=}')
    assert len(math_gold_probs_solns) > 0, f'No math problems found in {path_2_eval_dataset=}'

    # - Get vllm generator
    # prompt_template: str = H_MATH_MINERVA_PROMPT_TEMPLATE
    # prompt_template: str = H_MATH_MINERVA_PROMPT_TEMPLATE_2
    # prompt_template: str = H_MATH_MINERVA_PROMPT_TEMPLATE_3_COT
    prompt_template: str = HELM_MATH_PROMPT_8SHOT_COT2_TEMPLATE
    print(f'{prompt_template=}')
    # prompt_gen_func: Callable = get_prob_str_minerva_prompt
    prompt_gen_func: Callable = get_math_problem_prompt_ala_helm_8shot_cot2
    print(f'{prompt_gen_func=}')
    # extract_answer_func: Callable = extract_answer_minerva_prompt
    extract_answer_func: Callable = extract_answer_from_list_completion_strings_mv
    print(f'{extract_answer_func=}')
    # stop_tokens = ["Question:", "Question", "USER:", "USER", "ASSISTANT:", "ASSISTANT", "Instruction:", "Instruction", "Response:", "Response"]
    stop: list[str] = STOP_TOKENS
    # push to config before loading model to avoid any common llm issues
    wandb.config.update(dict(prompt_template=prompt_template, prompt_gen_func=str(prompt_gen_func), model=model, path_2_eval_dataset=path_2_eval_dataset, output_dir=output_dir, stop_tokens=stop, extract_answer_func=extract_answer_func))
    dtype: str = get_dtype_for_vllm()
    print(f'{dtype=}')
    sampling_params: SamplingParams = SamplingParams(n=n, max_tokens=max_tokens, top_p=top_p, temperature=temperature, stop=stop, use_beam_search=use_beam_search, best_of=best_of)
    print(f'--> {model=}')
    if 'gpt-4-' in model or 'gpt-3.5-' in model or 'gpt-4o' in model:
        #         # api_key = os.environ.get("OPENAI_KEY").strip()
        #         # api_key = open(Path('~/keys/openai_api_brandos_personal_key.txt').expanduser(), 'r').read().strip()
        #         # api_key = open(Path('~/keys/claude_api_brandos_personal_key.txt').expanduser(), 'r').read().strip()
        api_key = open(Path('~/keys/openai_api_key_brandos_koyejolab.txt').expanduser(), 'r').read().strip()
        gen: OpenAIGenerator = OpenAIGenerator(model, sampling_params, api_key)
    elif hf_gen_type == 'pipeline':
        print(f'{hf_gen_type=}')
        from transformers import pipeline, Pipeline
        mdl, tok = load_model_block_size(pretrained_model_name_or_path=model, block_size=sampling_params.max_tokens)
        llm: Pipeline = pipeline("text-generation", model=mdl, tokenizer=tok)
        sampling_params.num_beams = num_beams
        gen: HFPipelineGenerator = HFPipelineGenerator(llm, sampling_params)
        print(f'{llm.device=}')
    elif hf_gen_type == 'hf_direct_model_gen':
        print(f'{hf_gen_type=}')
        from transformers import pipeline, Pipeline
        mdl, tok = load_model_block_size(pretrained_model_name_or_path=model, block_size=sampling_params.max_tokens)
        llm: Pipeline = pipeline("text-generation", model=mdl, tokenizer=tok)
        gen: HFDirectModelGenerator = HFDirectModelGenerator(llm, sampling_params)
        print(f'{llm.device=}')
        assert ValueError(f'Don\'t use {hf_gen_type=} for now, odd bug, see: https://discuss.huggingface.co/t/how-to-generate-multiple-text-completions-per-prompt-like-vllm-using-huggingface-transformers-pipeline-without-triggering-an-error/86297/4')
    else:
        llm: LLM = LLM(model=model, dtype=dtype)
        gen: VllmGenerator = VllmGenerator(llm, sampling_params)
    print(f'{sampling_params} \n {sampling_params=}')

    # - Gen completions - completions are list of lists because completions can be multiple for a single prompt, for single response completions inside are length 1
    results: dict = inference_vllm_prompt_only(gen, math_gold_probs_solns, prompt_template, prompt_gen_func, batch_size, start, end) 
    completions_strs: list[list[str]] = results['completions_strs']  # completions strs per prompt
    model_answers: list[Union[str, None]] = extract_model_answers(completions_strs, extract_answer_func)
    math_gold_answers: list[str] = extract_gold_answers(math_gold_probs_solns)
    assert len(completions_strs) == len(math_gold_probs_solns), f'Length of completions_strs and math_gold_probs_solns should be equal but got: {len(completions_strs)=}, {len(math_gold_probs_solns)=}'
    assert len(model_answers) == len(math_gold_answers), f'Length of model_answers and math_gold_answers should be equal but got: {len(model_answers)=}, {len(math_gold_answers)=}'

    # - Evaluate
    results_d: dict = eval_boxed_accuracy_results(math_gold_answers, model_answers, verbose_eval=verbose_eval)
    print(f'{results_d["boxed_acc"]=} \n {results_d["len(results)"]=} \n {results_d["len(results_boxed)"]=} \n {results_d["sum(results_boxed)"]=}')
    wandb.log({'boxed_acc': results_d['boxed_acc'], 'len(results)': results_d['len(results)'], 'len(results_boxed)': results_d['len(results_boxed)'], 'sum(results_boxed)': results_d['sum(results_boxed)']})
    save_completions(output_dir, completion_filename, completions_strs, model_answers, math_gold_probs_solns, math_gold_answers,)
    wandb.save(output_dir / completion_filename)

    # - End run
    wandb.config.update(dict(prompt_gen_func=str(prompt_gen_func), prompt_template=prompt_template, model=str(model), path_2_eval_dataset=path_2_eval_dataset, output_dir=output_dir, sampling_params=vars(sampling_params)))
    print(f'{wandb.config=}')
    run.finish()

if __name__ == '__main__':
    import fire
    import time
    start = time.time()
    # main()
    fire.Fire(main)
    # pyton boxed_acc_eval.py --model meta-llama/Meta-Llama-3-8B-Instruct
    print(f"Done!\a Time: {time.time()-start:.2f} sec, {(time.time()-start)/60:.2f} min, {(time.time()-start)/3600:.2f} hr\a")