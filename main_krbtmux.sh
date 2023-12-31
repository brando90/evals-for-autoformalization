#!/bin/bash
# - snap: https://ilwiki.stanford.edu/doku.php?id=snap-servers:snap-servers and support il-action@cs.stanford.edu
# - live server stats: https://ilwiki.stanford.edu/doku.php?id=snap-servers:snap-gpu-servers-stats
#8 a100 80GB
ssh brando9@ampere1.stanford.edu
ssh brando9@skampere1.stanford.edu
#10 Quadro RTX 8000 48GB
ssh brando9@hyperturing1.stanford.edu
ssh brando9@hyperturing2.stanford.edu
#10 RTX A4000 16GB
ssh brando9@mercury1.stanford.edu
ssh brando9@mercury2.stanford.edu

# allows mouse scrolling
tput rmcup

source $AFS/.bashrc.lfs
# conda activate maf
conda activate evals_af
export CUDA_VISIBLE_DEVICES=5; export SLURM_JOBID=$(python -c "import random;print(random.randint(0, 1_000_000))"); echo $SLURM_JOBID;
echo CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES; echo SLURM_JOBID = $SLURM_JOBID; echo hostname = $(hostname)
ulimit -n 120000; ulimit -Sn; ulimit -Hn;
nvidia-smi;hostname
(echo "GPU_ID PID UID APP" ; for GPU in 0 1 2 3 ; do for PID in $( nvidia-smi -q --id=${GPU} --display=PIDS | awk '/Process ID/{print $NF}') ; do echo -n "${GPU} ${PID} " ; ps -up ${PID} | awk 'NR-1 {print $1,$NF}' ; done ; done) | column -t

export CUDA_VISIBLE_DEVICES=3,4,5,6; export SLURM_JOBID=$(python -c "import random;print(random.randint(0, 1_000_000))"); echo $SLURM_JOBID;
export CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7; export SLURM_JOBID=$(python -c "import random;print(random.randint(0, 1_000_000))"); echo $SLURM_JOBID;
echo CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES; echo SLURM_JOBID = $SLURM_JOBID; echo hostname = $(hostname)

# -- Test Pytorch GPU
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
python -c "import torch; print(torch.cuda.get_device_capability())"
python -c "import torch; print(torch.cuda.get_device_capability());print('if >=8 you can use bfloat16');"
python -c "import torch; print(torch.bfloat16);"

# - start krbtmux
#pkill -9 tmux -u brando9; pkill -9 krbtmux -u brando9; pkill -9 reauth -u brando9; pkill -9 python -u brando9; pkill -9 wandb-service* -u brando9;
krbtmux
reauth

ssh brando9@ampere1.stanford.edu
ssh brando9@hyperturing1.stanford.edu
ssh brando9@hyperturing2.stanford.edu
tmux ls

tmux new -s 0
tmux new -s 1
tmux new -s 2
tmux new -s rand
tmux new -s rand0
tmux new -s rand1
tmux new -s rand2
tmux new -s rand3
tmux new -s rand4
tmux new -s rand5
tmux new -s rand6
tmux new -s rand7
tmux new -s rand8
tmux new -s rand9
tmux new -s rand10
tmux new -s rand11
tmux new -s rand12
tmux new -s rand13
tmux new -s rand14
tmux new -s rand15
tmux new -s rand16
tmux new -s rand17
tmux new -s rand18
tmux new -s rand19
tmux new -s rand20
tmux new -s rand21
tmux new -s rand22
tmux new -s rand23
tmux new -s rand24
reauth

# - Min setup code for ru
reauth

source $AFS/.bashrc.lfs
# conda activate maf
conda activate evals_af
export CUDA_VISIBLE_DEVICES=$(nvidia-smi --query-gpu=index,memory.free --format=csv,noheader,nounits | sort -k2 -nr | head -n 1 | awk -F ', ' '{print $1}')
echo CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES

# --- Run
# -- Make data sets HF
# conda activate maf
# python ~/massive-autoformalization-maf/maf-src/data_utils/textbook2hf_dataset.py

# -- Train
#login to hf to use llama2, get your hf token eg cat ~/keys/brandos_hf_token.txt
huggingface-cli login
#login to hf to use llama2, get your hf token eg cat ~/keys/brandos_hf_token.txt
# python ~/massive-autoformalization-maf/maf-src/af_train/unpaired_pytorch_hf_training.py
python ~/evals-for-autoformalization/src/train/train_full_fine_tune.py


# - Create accelerate config & run script using accelerate
# accelerate config
# accelerate config -- ~/massive-autoformalization-maf/configs/accelerate/default_config_ddp_bm.yaml 
cat ~/evals-for-autoformalization/configs/accelerate/default_config_ddp_bm.yaml
# - Login to hf to use llama2, get your hf token eg cat ~/keys/brandos_hf_token.txt
# huggingface-cli login
# get top 3 free gpus & export so every child process gets it
export CUDA_VISIBLE_DEVICES=$(nvidia-smi --query-gpu=index,memory.free --format=csv,noheader,nounits | sort -t ',' -k2 -nr | head -n 3 | awk -F ', ' '{printf "%s,",$1}' | sed 's/,$//')
echo CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES
# accelerate launch --config_file ~/.cache/huggingface/accelerate/default_config.yaml ~/massive-autoformalization-maf/maf-src/af_train/unpaired_pytorch_hf_training.py
# accelerate launch --config_file ~/massive-autoformalization-maf/configs/accelerate/default_config_bm.yaml ~/massive-autoformalization-maf/maf-src/af_train/unpaired_pytorch_hf_training.py
accelerate launch --config_file ~/evals-for-autoformalization/configs/accelerate/default_config_bm.yaml ~/evals-for-autoformalization/src/train/train_full_fine_tune.py

# -- other option is to run `echo $SU_PASSWORD | /afs/cs/software/bin/reauth` inside of python, right?
export JOB_PID=$!
echo $OUT_FILE
echo $ERR_FILE
echo JOB_PID = $JOB_PID
echo SLURM_JOBID = $SLURM_JOBID