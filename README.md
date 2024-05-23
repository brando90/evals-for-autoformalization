# SNAP Cluster Setup

If you want to do this tutorial with active reflections in the style of a assignment see this: https://docs.google.com/document/d/1k3d3_AOp-Y22L-GbgHivDqKe9r9LC5nscaIzbm3LWYc/edit?usp=sharing

## Get Compute for your Research Project

### SNAP Cluster Important References & Help/Support
Always use the original documentation or wiki for each cluster: https://ilwiki.stanford.edu/doku.php?id=start -- your **snap bible**.
Other useful resources:
- Support IT for snap: il-action@cs.stanford.edu (don't be shy to ask them question or help for SNAP.)
- compute instructions from Professor Koyejo's (Sanmi's) lab (STAIR Lab): https://docs.google.com/document/d/1PSTLJdtG3AymDGKPO-bHtzSnDyPmJPpJWXLmnJKzdfU/edit?usp=sharing
- advanced video from Rylan and Brando (made for the STAIR/Koyejo Lab): https://www.youtube.com/watch?v=XEB79C1yfgE&feature=youtu.be
- our CS 197 section channel
- join the snap slack & ask questions there too: https://join.slack.com/t/snap-group/shared_invite/zt-1lokufgys-g6NOiK3gQi84NjIK_2dUMQ

## Get access to SNAP with a CSID

### First request CSID with Michael Bersntein as sponsor 
First create a CSID here and  please make your CSID the same as your Stanford SUNET id. 
Request it here:  https://webdb.cs.stanford.edu/csid and 
If you are a CS197 (only!) then:
1. Put Michael Bernstein as your CSID sponsor/supervisor and e-mail you are doing cs197 with me.
2. Put Sanmi Koyejo as your CSID sponor/supervisor and e-mail them you are planning to collaborate with me in research.
Note: this is different from SNAP cluster sponso (which you email il-action@stanford.edu), but CSID is needed first. 

### Second get acces to SNAP

To get access to snap write an e-mail with this subject:

> Access Request SNAP Cluster Working With Brando Miranda CS197 for <full_name> <CSID>  <SUNET>

For example: 

> Access Request SNAP Cluster Working With Brando Miranda CS197 for Brando Miranda brando9 brando9$ 

and sent it to
- Eric Pineda: eric.pineda@stanford.edu
- Brando Miranda: brando9@stanford.edu
- [SNAP cluster IT](https://ilwiki.stanford.edu/doku.php?id=start): il-action@cs.stanford.edu
<!-- - Sanmi Koyejo: sanmi@stanford.edu -->

Once you get access to it you will be able to login to the cluster via the ssh command in the terminal (cli) and vscode.

## SSH into a Sanmi owned node/server
To access a SNAP server or node owned by Sanmi’s Lab, you can use any of the following machines: skampere1, ampere1, ampere8, hyperturning1, hyperturning2, or any of the mercury machines (mercury1, mercury2). Use your CSID/SUNet ID to log in. For example:
```bash
# Example
ssh brando9@skampere1.stanford.edu

# Yours
ssh CSID@skampere1.stanford.edu
```
type your password and login. 
Then use the `ls` command and `pwd` and `realpath ~` and `realpath $HOME` and `realpath .` commands to see the contents of your root `~` directory.
Do the `cd ..` and `pwd` to be familiar with the file system/directory structure in snap.
Then run the `reauth` command, this command is needed due to the (kerberos) security settings in SNAP (hote: Brando strongly disagrees with how IT set up this part and apologizes for the complexity for you).
[For more info on reauth read the wiki here](https://ilwiki.stanford.edu/doku.php?id=hints:long-jobs).

**Tip**: see the wiki for other nodes that exist on snap!

Sample output if it worked:
```bash
(base) brandomiranda~ ❯ ssh brando9@skampere1.stanford.edu
brando9@skampere1.stanford.edu's password:
Last login: Wed Apr  3 12:07:20 2024 from 172.24.69.154
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 skampere1.stanford.edu
 Ubuntu 20.04 (5.4.0-162-generic)
 128 x AMD EPYC 7543 32-Core Processor, 1.96 TiB RAM, 8.00 GiB swap

 enp44s0f0: 172.24.75.194
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
   -> For help or to report problems, go to http://support.cs.stanford.edu

ln: failed to create symbolic link '/lfs/skampere1/0/brando9/iit-term-synthesis': File exists
(evals_af) brando9@skampere1~ $
(evals_af) brando9@skampere1~ $ realpath ~
/lfs/skampere1/0/brando9
(evals_af) brando9@skampere1~ $ realpath $HOME
/lfs/skampere1/0/brando9
(evals_af) brando9@skampere1~ $ realpath .
/lfs/skampere1/0/brando9
(evals_af) brando9@skampere1~ $ ls
beyond-scale-language-data-diversity			  massive-autoformalization-maf       ultimate-anatome
data							  miniconda			      ultimate-pycoq
diversity-for-predictive-success-of-meta-learning	  miniconda.sh			      ultimate-utils
evals-for-autoformalization				  nltk_data			      vscode.beyond-scale-language-data-diversity.skampere1.code-workspace
evaporate						  proverbot9001			      vscode.evaporate.skampere1.code-workspace
iit-term-synthesis					  putnam-math			      vscode.lean4ai.skampere1.code-workspace
keys							  pycoq				      vscode.maf_data.creating_data_math_training.skamapere1.code-workspace
_KoyejoLab-Predictable-LLM-Evals			  snap-cluster-setup		      vscode.maf_data.training_af_model.skampere1.code-workspace
KoyejoLab-Predictable-LLM-Evals				  tempt.txt			      vscode.snap-cluster-setup.code-workspace
KoyejoLab-Predictable-LLM-Evals.skampere1.code-workspace  test_folder			      wandb
lean4ai							  the-data-quality-edge-for-top-llms
(evals_af) brando9@skampere1~ $ pwd
/lfs/skampere1/0/brando9
(evals_af) brando9@skampere1~ $ cd ..
(evals_af) brando9@skampere1/lfs/skampere1/0 $ pwd
/lfs/skampere1/0
(evals_af) brando9@skampere1/lfs/skampere1/0 $ cd ~
(evals_af) brando9@skampere1~ $
(evals_af) brando9@skampere1~ $ reauth
Password for brando9:
Background process pid is: 4145964
```
Note: this might look slightly different if you already set up your `.bashrc` file. 

**Tip**: If the `reauth `command doesn't work do or/and e-mail the [SNAP cluster IT](https://ilwiki.stanford.edu/doku.php?id=start) il-action@cs.stanford.edu:
```bash
export PATH="/afs/cs/software/bin:$PATH"
```
**TIP**: Ask ChatGPT what `export PATH="/afs/cs/software/bin:$PATH"` does. ChatGPT is excellent at the terminal and bash commands. Note consider adding this to your `.bashrc` for example [see this](https://github.com/brando90/snap-cluster-setup/blob/main/.bashrc#L24). 
**TIP**: you might have to ssh into your node again outside of vscode for this to work if vscode is giving you permission issues or e-mail snap IT. 

## Setup your .bashrc, redirect the $HOME (~) envi variable from afs to lfs and create a soft link for .bashrc (afs/.bashrc -> lfs/.bashrc)
Rationale: [SNAP has 3 file systems afs, lfs, dfs](https://ilwiki.stanford.edu/doku.php?id=hints:storefiles) (folders where your files, data and code could potentially be stored). 
We will only be using `afs` and `lfs`. 
`dsf` stands for distributed file system and it makes your files available with all nodes/servers/computers in the snap cluster but it's too slow to be usable (IT should have set `dfs` up properly but they did not and this is why this tutorial is long).
So what we will do is put your code `afs` and create a soft link to it in `lfs`.
`lfs` stands for local file system and it's where your actual data (trainning data, models, python conda environment will reside).
We will soft link (with `ln -s <src> <target>`) your code/github repos from `afs` (src) to `lfs` (target) later. 

**TIP**: anything you don't understand we encourage you to discuss it with GPT4/Claude/your favorite LLM + paste the entire tutorial to in your conversation with it!  
e.g., ask it what an environment variable is, what a git command does, nvidia-smi command does, what `vim` is or what `git clone` is, `pip install`, `pip instlal -e .` , what conda is and python envs, what `$PATH` or `$HOME` is, tmux, basically bash related things it's great for!.

Now that you understand the rationale, so background on how starting a terminal (cli) works. 
Every time one logins into a snap node/server (or creates a new linux terminal with the `bash` cli command), the terminal (cli) needs to configure your unix/linux environment (the set of variables that hold important paths so that the terminal/cli "works as expected" e.g., standard commands/execuatable binaries are found like `python`, `ls`, `cd`, `echo`, `pwd`, `cat`, `vim` etc. or environment variables like `$HOME`, `$PATH`, etc. have the right content)

Usually the linux terminal (e.g. `bash`) runs ("sources") `.bash_profile` to set up your linux environment before providing the bash/cli/terminal session (where you write commands). 
In the SNAP cluster, the system admins have their `.bash_profile` located at your root's `afs`. 
More precisely, you will have a (sym) link called `.bash_profile` that points to the system adimns file at `/afs/cs/etc/skel/.bash_profile`. 
This file is ran each time you ssh/log in or you run `bash` in SNAP. 
This command usually sets up your environment variables for your terminal (e.g., current `bash` session) by running commands you specify in that file. 
In particular, it sets up [environment variables](https://www.google.com/search?q=environment+variables&rlz=1C5CHFA_enUS741US741&oq=environment+variab&gs_lcrp=EgZjaHJvbWUqDQgAEAAYgwEYsQMYgAQyDQgAEAAYgwEYsQMYgAQyBwgBEAAYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBggEEEUYOTIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDQ0MjVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8), which are terminal/cli variables that point to important locations in the node/computer so that everything works! 
Now, let's inspect your `.bash_profile`. 
For that you need to `/afs/cs.stanford.edu/u/<CSID>` with the `cd` command and then we can display the contents of the file with `cat` (always make sure you understand the commands you're running & read the output):
```bash
# ... AFTER sshing to a SNAP node
(evals_af) brando9@skampere1~ $
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ cd /afs/cs.stanford.edu/u/brando9
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ cat .bash_profile
# DO NOT MODIFY THIS FILE! Your changes will be overwritten!
# For user-customization, please edit ~/.bashrc.user
#
# $ROOT$
#
# CSD-CF miles 2003-01-24

# Don't do anything in this file -- do it in .bashrc

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi
```
In this specific `.bash_profile` runs ("sources") another file called `.bashrc`. 
If you yours runs `~/.bashrc.user` (which is a very non-standard setup), then change your `.bash_profile` to be the same as the one above with `vim`. If you need to do that do:
```bash
vim .bash_profile
```
This open the file. Then move to the line you want to edit. 
Then type `i` in `vim`. Then you are now in insert mode. 
Then change the line `	. ~/.bashrc` to `	. ~/.bashrc` (note the indentation). 
Then do `:w` followed by `:q` (or `:wq` or `:x`) which tells vim to save your changes and exit `vim`. 
Make sure you know the basics of `vim` even if you use vscode with the remote ssh extension (we will cover the basic of vim bellow and we do recommend vscode with the ssh extension). 
Make sure you understand why you are doing this. 
You are doing this so that `.bash_profile` runs **your** configurations of bash each time you start a bash session in the terminal.  
Now, since `.bash_profile` runs/sources your `.bashrc` file each time you ssh/login to snap we will put our personal configurations for SNAP in our `.bashrc` located at `~/.bashrc` (note: `~` is the same as `$HOME` and points to your local path) i.e., that is the meaning of `. ~/.bashrc`. 

The plan is to:
  1. put `.bashrc` in `afs` since `afs` is accessible via all nodes (to manage a single version for all SNAP nodes)
  2. have the environment variable `$HOME` (`~`) point from the root of `afs` to `lfs` automatically everytime you login to any node.
  3. create a soft link in your node's lfs home root `$HOME` (`~`) pointing to the path at `afs` for the `.bashrc` file (otherwise when `.bash_profile` is ran/sourced your terminal won't be set up as you expect/want)
This culminates in you putting your `.bashrc` file in exactly this path:
```bash
/afs/cs.stanford.edu/u/<YOUR_CSID>/.bashrc
```

Let's do setps 1, 2, 3. 

Now we are doing 1 and 2 in one shot in `.bashrc`. 
Remove the sym link to the system admins `.bashrc` (always understand the commands you're running and read the output):
```bash
rm .bashrc
```
This should resolve any permissions issues. 
<!-- https://piazza.com/class/lurxqr2yufy3bk/post/10 -->
Then create a file `.bashrc` at `/afs/cs.stanford.edu/u/<YOUR_CSID>/` with (if it doesn't exist already, if it does exit remove it's contents, you will change it):
```bash
touch /afs/cs.stanford.edu/u/<YOUR_CSID>/.bashrc
```
open it with a terminal text editor. 
I suggest `vim` (read [this for a quick ref for vim](https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started)) since that is what I use:
```bash
vim /afs/cs.stanford.edu/u/<YOUR_CSID>/.bashrc
```
then in `vim` press `i` to get into insert mode. 
Then [copy paste the contents of our base `.bashrc`](https://github.com/brando90/snap-cluster-setup/blob/main/.bashrc#L24) file **but change everywhere the string `brando9` appears and put your `CSID`** (so read the file carefully before copy pasting). 
Then press `esc` to `:w` enter to save the file. Then press `:q` enter to exist (or `:x` enter for for save & exit). 
In particular, [note this command in your `.bashrc` file](https://github.com/brando90/snap-cluster-setup/blob/main/.bashrc#L43C1-L47C31):
```bash
# - The defaul $HOME is /afs/cs.stanford.edu/u/brando9 but since you want to work in a specific server due to otherwise conda being so hard you need to reset what home is, see lfs: https://ilwiki.stanford.edu/doku.php?id=hints:storefiles#lfs_local_server_storage  
export LOCAL_MACHINE_PWD=$(python3 -c "import socket;hostname=socket.gethostname().split('.')[0];print('/lfs/'+str(hostname)+'/0/brando9');")
mkdir -p $LOCAL_MACHINE_PWD
export WANDB_DIR=$LOCAL_MACHINE_PWD
export HOME=$LOCAL_MACHINE_PWD
```
which changes where your `$HOME` directory points to every time you login to a node in SNAP (since `.bashrc` is sourced via `.bash_profile` everytime you login or run the `bash` terminal command). 
It changes your default home/root location from `afs` (some weird Stanford file system with limited disk space) to the local node's `lfs` file system/directories. 
We do this because `afs` does not have a lot of disk compared to `lfs` (so that you don't run into disk space issues, if you do however, you will need to clean your disk or e-mail snap's IT). 
However, `afs` is fast but has little space (so it can only hold small text file e.g., usually git hub repos with code only, so not with data or gitlfs). 
In addition, `lfs` is also quicker (since it is "a local computer" i.e., you are logged in to **a compute node directly**, which is an unusual set up for a cluster). 
I repeat, we won't be using `dfs`. 
The eventual goal is that your code will be at `afs` and that soft link to your code will be at `lfs`. 
Note: the python conda environment, data and big files or data that needs fast access will be at `lfs`.

Now let's do 3 manually and needs to be done manually **every time you want to use a new node in SNAP**. 
This is only SNAP specific. 
Note: if you think you know how to not set up this manually each time, open a gitissue and propose a solution!
So let's make sure there is a pointer/reference to the your `.bashrc` file so `.bash_profile` can actually find it and run it when you create a terminal/cli or run `bash`.
For that create the soft link but change `brando9` to your `CSID`:
```bash
ln -s /afs/cs.stanford.edu/u/brando9/.bashrc ~/.bashrc
```
check that this worked by inspecting if the link exists at your root in lfs. 
Run these commands: 
```bash
cd /lfs/skampere1/0/<CSID>
ls -lah
```
Sample output:
```bash
(evals_af) brando9@skampere1~ $ cd /lfs/skampere1/0/brando9
(evals_af) brando9@skampere1~ $ ls -lah
total 99M
drwxr-sr-x  22 brando9 root 4.0K Apr  3 17:07 .
drwxrwsrwt  23 root    root 4.0K Mar 27 19:21 ..
-rw-------   1 brando9 root  48K Apr  3 11:20 .bash_history
lrwxrwxrwx   1 brando9 root   38 Oct 27 12:57 .bashrc -> /afs/cs.stanford.edu/u/brando9/.bashrc
...
lrwxrwxrwx   1 brando9 root   49 Apr  3 11:02 snap-cluster-setup -> /afs/cs.stanford.edu/u/brando9/snap-cluster-setup
...
```
Notice how we have `.bashrc -> /afs/cs.stanford.edu/u/brando9/.bashrc`, which menas the name `.bashrc` actually points to ` /afs/cs.stanford.edu/u/brando9/.bashrc`.  

Now that your `.bashrc` is in the `afs` location and `$HOME` (`~`) points to your node's `lfs` home path, we should restart your bash terminal in SNAP to test that your changes take effect. 
Recall, your terminal is now set up as in described in 1,2, 3 because `.bash_profile` runs `.bashrc`. 
So let's test it. 
Run in your terminal, one at a time and read the output of each command 
(never run any command blindly, always read/understand the command you're running and it's output): 
```bash
bash
echo $HOME
realpath ~/.bashrc
pwd ~/.bashrc
```
Sample ouput:
```bash
# Or log out and relogin to snap with your preferred node, so bash isn't needed anymore
(evals_af) brando9@skampere1~ $ bash
ln: failed to create symbolic link '/lfs/skampere1/0/brando9/iit-term-synthesis': File exists
(evals_af) brando9@skampere1~ $ echo $HOME
/lfs/skampere1/0/brando9
(evals_af) brando9@skampere1~ $ realpath ~/.bashrc
/afs/cs.stanford.edu/u/brando9/.bashrc
(evals_af) brando9@skampere1~ $ pwd ~/.bashrc
/lfs/skampere1/0/brando9
```
this demonstrates `$HOME` (`~`) points to your node's `lfs` and that the real path of `.bashrc` is actually in `afs`. 

Now repeat the above (without the `bash` command) but log out the snap node you are into and re login via ssh, and check your `.bashrc` is in `afs` and `$HOME` points to `lfs` (never run any command blindly, always read/understand the command you're running and it's output)::
```bash
sh brando9@skampere1.stanford.edu
echo $HOME
realpath ~/.bashrc
pwd ~/.bashrc
```
sample output:
```bash
(evals_af) brando9@skampere1~ $ echo $HOME
/lfs/skampere1/0/brando9
(evals_af) brando9@skampere1~ $ realpath ~/.bashrc
/afs/cs.stanford.edu/u/brando9/.bashrc
(evals_af) brando9@skampere1~ $ pwd ~/.bashrc
/lfs/skampere1/0/brando9
```
make sure you understand the difference between `realpath ~/.bashrc` and `pwd ~/.bashrc`.

Bonus Note: this is (most likely) correct even though the wiki/docs for snap say to update `.bash.user` (but .bash.user is never sourced, I asked the it and I strongly recommend you ask too, see wrong/confusing docs if you want https://ilwiki.stanford.edu/doku.php?id=hints:enviroment but that's not what `.bash_profile` is sourcing!?).

### Basic editing in the terminal with vim
You already created a `.bashrc`
Vim is for editing file in the terminal (cli). 
These are the commands you might need https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started. 
Mostly knowing that:
-> pressing `i` puts you in insert mode
-> pressing `w` writes/save the files
-> pressing `q` quits
that's all you need.
If you want more experience with vim do this:

Certainly! Below is a small, self-contained markdown tutorial focusing on editing files in the terminal using Vim. This tutorial will cover the basics of opening a file, entering insert mode for editing, exiting insert mode, and saving your changes.

```markdown
#### Vim Editing Basics Tutorial
Vim is a highly efficient text editor that operates in various modes. The most commonly used modes are "Normal" and "Insert" modes. This tutorial will guide you through opening a file in Vim, editing it, and saving your changes.
## Opening a File in Vim
To open a file with Vim, use the following command in your terminal:
```bash
vim filename
```
Replace `filename` with the name of the file you wish to edit. If the file does not exist, Vim will create it for you.
Entering Insert Mode: 
Once you have your file opened in Vim, you'll start in Normal mode. To start editing your file, you need to enter Insert mode.
```vim
i
```
Pressing `i` will switch you from Normal mode to Insert mode. Now you can start typing and editing the file as you would in a conventional text editor.
Exiting Insert Mode: 
To stop editing and return to Normal mode, press:
```vim
Esc
```
The `Esc` key brings you back to Normal mode, where you can execute Vim commands.

Saving Changes: To save your changes in Normal mode, type:
```vim
:w
```
This command writes your modifications to the file but keeps it open in Vim.

Exiting Vim: If you want to exit Vim *after* saving your changes, type:
```vim
:q
```
However, to both save your changes and exit Vim in one command, you can use:
```vim
:x
```
or
```vim
:wq
```
Both commands save any changes and then close the file.

Conclusion: 
This tutorial covered the basics of file editing with Vim in the terminal, including opening files, switching between Insert and Normal modes, saving changes, and exiting Vim. With these commands, you can start editing files efficiently in the terminal. 
[Couresty of ChatGPT (GPT4)](https://chat.openai.com/c/9fbefbf9-f7c7-4e68-84de-6bbd23853a77).

## Using git and conda environments in SNAP
At this point, you know what the environment variable `$HOME` is and that yours should be pointing to your node’s `lfs` home directory -- as suggested by [this .bahrc file](https://github.com/brando90/snap-cluster-setup/blob/main/.bashrc#L43C1-L47C31) (but using your CSID).

Now the goal will be to:
1. show you how to `git clone` (from your git fork of this repo) a small sized git project (so not using `gitlfs`, that would most likely create issues with AFS's storage limit) like [this one (`snap-cluster-setup`)](https://github.com/brando90/snap-cluster-setup)
2. learn what a [python environment](<https://csguide.cs.princeton.edu/software/virtualenv#:~:text=A%20Python%20virtual%20environment%20(venv,installed%20in%20the%20specific%20venv.>) is and create one using [conda](https://docs.conda.io/en/latest/)

For step 1 we will first go to your `afs` home root path. 
We do this because `afs` is the only "distributed" file system that isn't very slow and that **is** accessible at all [SNAP nodes/servers](https://ilwiki.stanford.edu/doku.php?id=start). 
It will be similar to how we created our `.bashrc` file previously at your `afs` root directory and then soft link it at your `lfs` directory (which should be your `$HOME` path). 
The main difference is that instead of soft linking a file, we will soft linke a directory. 

So `cd` to your `afs` root directory. 
If you correctly edited your `.bashrc` then you should be able to do to move to your `afs` root: 
```bash
cd $AFS
```
tip: do `echo $AFS` or to any environment variable to see the contents of them!).
If that didn't work, fix your `.bashrc` and do the previous command (e.g., make sure `.bashrc` exports `$AFS`, change all `brando9` instances with your `CSID`, and potentially see the original `.bashrc` if something doesn't work or even start with a new `.bashrc` again.
Note, `cd $AFS` should be equivalent to doing (with your `CSID`):
```bash
cd /afs/cs.stanford.edu/u/brando9
```
Since AFS should be point to your afs due to this command `export AFS=/afs/cs.stanford.edu/u/brando9` in the `.bashrc`. 
Sample output (understand the commands): 
```bash
# after sshing into a snap node or running bash on your terminal (cli)
(evals_af) brando9@skampere1~ $
(evals_af) brando9@skampere1~ $ realpath .
/lfs/skampere1/0/brando9
(evals_af) brando9@skampere1~ $ pwd
/lfs/skampere1/0/brando9
(evals_af) brando9@skampere1~ $ cd $AFS
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ pwd
/afs/cs.stanford.edu/u/brando9
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ realpath .
/afs/cs.stanford.edu/u/brando9
```

Now that we are at our `afs` home root directory, let's git clone your git fork.
First git fork this repo using the github UI (likely best option is to Google this or ChatGPT it). 
This step is really showing you to git clone any github repo to your `afs` (npte: later you will git clone your actual project's repo and repeat cloning it to your afs every time you have a new repo you want to use for snap.
Note: if you're following this setup, since we are using `lfs` due to storage issues with `afs` you will need to set up a new conda env each time use a new node, although the repo might be available already).

Git clone this repo with using ssh path from the github repo option and check that it was downloaded with `ls -lah` and `realpath`
e.g.,: 
```bash
cd $AFS
git clone git@github.com:brando90/snap-cluster-setup.git
ls -lah
realpath snap-cluster-setup
```
Sample output: 
```bash
(evals_af) brando9@skampere1~ $ cd $AFS
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ 
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $  git clone git@github.com:brando90/snap-cluster-setup.git
Cloning into 'snap-cluster-setup'...
remote: Enumerating objects: 906, done.
remote: Counting objects: 100% (360/360), done.
remote: Compressing objects: 100% (134/134), done.
remote: Total 906 (delta 284), reused 291 (delta 225), pack-reused 546
Receiving objects: 100% (906/906), 74.63 MiB | 7.03 MiB/s, done.
Resolving deltas: 100% (503/503), done.
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ ls -lah
total 74M
drwxrwxrwx 29 brando9 users 4.0K Apr  3 13:41 .
drwxr-xr-x  2 root    users 520K Apr  1 11:10 ..
...
-rw-r--r--  1 brando9 users 8.8K Jan 29 16:33 .bashrc
...
drwxr-xr-x  5 brando9 users 2.0K Apr  3 16:50 snap-cluster-setup
...
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ realpath snap-cluster-setup
/afs/cs.stanford.edu/u/brando9/snap-cluster-setup
```
Note that since you are at your root `afs`, the `.bashrc` file is not a soft link. 
Your `snap-cluster-setup` should also **not** be a soft link at your root `afs` directory. 
Verify that with `realpath` (and not `pwd`):
```bash
pwd .bashrc
realpath .bashrc
pwd snap-cluster-setup/
realpath snap-cluster-setup/
```
Sample output:
```bash
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ pwd .bashrc
/afs/cs.stanford.edu/u/brando9
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ realpath .bashrc
/afs/cs.stanford.edu/u/brando9/.bashrc
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ pwd snap-cluster-setup/
/afs/cs.stanford.edu/u/brando9
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ realpath snap-cluster-setup/
/afs/cs.stanford.edu/u/brando9/snap-cluster-setup
```

### Create a soft link for your cloned github project (lfs -> afs)
We will create a soft link as we previously did in your home `lfs` path for the github project you just cloned, and santiy check it is a soft link (similar to your `.bashrc` file).
Run one command at a time and see output (we strongly suggest against running command blindly, e.g., if one doesn't work, then how will you fix it if you don't know what you've run so far?):
```bash
echo $HOME
# cd ~ 
cd $HOME
# ln -s /afs/cs.stanford.edu/u/brando9/snap-cluster-setup $HOME/snap-cluster-setup
ln -s $AFS/snap-cluster-setup $HOME/snap-cluster-setup
ls -lah
pwd $HOME/snap-cluster-setup
realpath $HOME/snap-cluster-setup
```
(Tip: to learn about the equivalence of `~` and `$HOME`, re-run the `pwd` command with `~` instead of `$HOME`. 
What happens?)
Sample output:
```bash
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ echo $HOME
/lfs/skampere1/0/brando9
(evals_af) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ cd $HOME
(evals_af) brando9@skampere1~ $ ln -s $AFS/snap-cluster-setup $HOME/snap-cluster-setup
(evals_af) brando9@skampere1~ $ ln -s $AFS/snap-cluster-setup $HOME/snap-cluster-setup
(evals_af) brando9@skampere1~ $ ls -lah
total 99M
drwxr-sr-x  22 brando9 root 4.0K Apr  3 19:39 .
drwxrwsrwt  24 root    root 4.0K Apr  3 18:33 ..
...
lrwxrwxrwx   1 brando9 root   38 Oct 27 12:57 .bashrc -> /afs/cs.stanford.edu/u/brando9/.bashrc
...
lrwxrwxrwx   1 brando9 root   49 Apr  3 11:02 snap-cluster-setup -> /afs/cs.stanford.edu/u/brando9/snap-cluster-setup
...
(evals_af) brando9@skampere1~ $ pwd $HOME/snap-cluster-setup
/lfs/skampere1/0/brando9
(evals_af) brando9@skampere1~ $ realpath $HOME/snap-cluster-setup
/afs/cs.stanford.edu/u/brando9/snap-cluster-setup
```
Tip: `ls` is a very useful command. What is is? Try `ls` vs `ls -l` vs `ls -la` vs `ls -lah`. 
What is the difference? Use the `man` command or `help` flag to learn more about it.

This sanity checks that your `snap-cluster-setup` indeed is locacted at your root `afs` but a soft link is at your root `lfs` path. 
This should convince you by looking where `.bashrc` points too and where your github repo called `snap-cluster-setup` points too. 

Note: you have to repeat the above ach time you set up a new github repo in SNAP. 
This is because you have not cloned the repo to `afs` to be shared accross all the SNAP nodes. 
In addition `afs` is small (but fast) and `dfs` is useless in this cluster sadly, so we put the code in `afs` so it's shared accross all nodes and not use `dfs`. 

### Python envs with Conda in lfs (not afs!)
When you have python projects, they usually have libraries they depend on. 
These are called depedencies (Google it to learn more!). 
So that these depedency installations for different projects in the same machine do not conflict we have different "<https://csguide.cs.princeton.edu/software/virtualenv#:~:text=A%20Python%20virtual%20environment%20(venv,installed%20in%20the%20specific%20venv.>) is and create one using [conda](https://docs.conda.io/en/latest/)" (also called conda environments or [virtual environments](https://ilwiki.stanford.edu/doku.php?id=hints:virtualenv)). 
Approximately, these are different locations in your system will your the installations for each project and setting up usually "secret" enviornment variable depending what depedency management system you are using e.g., conda or virtual env or poetry etc. 
This is usually specific for each programming langauge you use (e.g., pip, conda for python, opam for coq, etc.) so it's often hard to remember the details and often people learn one setup and re-use it all the time. 

For snap we will use conda. 
First check if you have conda in your cli by doing
```bash
which conda 
```
Pro Tip: if you are using vscode make sure your vscode is pointing to the python or conda env you want for your project, usually you set it up at the bottom right in vscode. 
Sample output:
```bash
(base) brando9@skampere1~ $ which conda
/lfs/skampere1/0/brando9/miniconda/bin/conda
```
Tip: a nice sanity check is check which binary the default/system is using. Usually by doing conda deactivate and then which python in the cli. 

If the previous command doesn't work then we will have to **locally** install conda (i.e., you will install conda in lfs by putting it's binary in a location you have permission to use).  
When you have a cluster usually the system admins install software you need and usually you do not have sudo priviledges (google that or do `man sudo` t learn!). 
Otherwise a trick to go around it is to install locally as we are about to do (but it's not usually recommended). 
Install conda (and update pip) if it's missing by running the following commands (**do not run them blindly, see the output before proceeding to the next one**):
```bash
echo $HOME
cd $HOME

# -- Install miniconda
# get conda from the web
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
# source conda with the bash command and put the installation at $HOME/miniconda
bash $HOME/miniconda.sh -b -p $HOME/miniconda
# activate conda
source $HOME/miniconda/bin/activate

# - Set up conda
conda init
conda init bash
conda install conda-build
conda update -n base -c defaults conda
conda update conda

# - Make sure pip is up to date
pip install --upgrade pip
pip3 install --upgrade pip
which pip
which pip3

# - Restart your bash terminal
bash
```
The previous commands take a while so instead I will only demonstrate two commands to check if conda was installed right. 
Make sure you have a fresh `bash` terminal (understand the commands):
```bash
# which conda binary are we using?
which conda
# which python binary are we using?
which python
# which conda envs do we have?
conda info -e
```
sample output:
```bash
(base) brando9@skampere1~ $ which conda
/lfs/skampere1/0/brando9/miniconda/bin/conda
(base) brando9@skampere1~ $ which python
/lfs/skampere1/0/brando9/miniconda/bin/python
(base) brando9@skampere1~ $ conda info -e
# conda environments:
#
base                  *  /lfs/skampere1/0/brando9/miniconda
beyond_scale             /lfs/skampere1/0/brando9/miniconda/envs/beyond_scale
evaporate                /lfs/skampere1/0/brando9/miniconda/envs/evaporate
lean4ai                  /lfs/skampere1/0/brando9/miniconda/envs/lean4ai
maf                      /lfs/skampere1/0/brando9/miniconda/envs/maf
my_env                   /lfs/skampere1/0/brando9/miniconda/envs/my_env
olympus                  /lfs/skampere1/0/brando9/miniconda/envs/olympus
pred_llm_evals_env       /lfs/skampere1/0/brando9/miniconda/envs/pred_llm_evals_env
putnam_math              /lfs/skampere1/0/brando9/miniconda/envs/putnam_math
snap_cluster_setup       /lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup
```

It would be ideal to create a single conda env for each project and put it in afs so that all nodes can use all the code for your github project **and** it's depedencies too. 
Unfortuantely, installing depedencies usually takes a lot of space. 
Thus we will install conda and create a conda env for each github project with it's installed depedencies in each node's lfs. 
Thus, create a new conda env for this `snap-cluster-setup` tutorial:
```bash
# - check envs
conda info -e

# - activate conda
conda update
pip install --upgrade pip

# - create conda env (note: vllm has issues with 3.10 so we are using 3.9)
conda create -n snap_cluster_setup python=3.9

# - activate your conda env
conda activate snap_cluster_setup
```
Note: I try to use pip as much as I can instead of conda to install my packages (or be consistent with which one I use, but sometimes you will have to combine each one since package management and installation can be tricky and hacky. Welcome to the real world!).
Sample output:
```bash
(base) brando9@skampere1~ $ conda create -n snap_cluster_setup python=3.9
Retrieving notices: ...working... done
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup

  added / updated specs:
    - python=3.9


The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main 
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu 
  ca-certificates    pkgs/main/linux-64::ca-certificates-2024.3.11-h06a4308_0 
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.38-h1181459_1 
  libffi             pkgs/main/linux-64::libffi-3.4.4-h6a678d5_0 
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-11.2.0-h1234567_1 
  libgomp            pkgs/main/linux-64::libgomp-11.2.0-h1234567_1 
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-11.2.0-h1234567_1 
  ncurses            pkgs/main/linux-64::ncurses-6.4-h6a678d5_0 
  openssl            pkgs/main/linux-64::openssl-3.0.13-h7f8727e_0 
  pip                pkgs/main/linux-64::pip-23.3.1-py39h06a4308_0 
  python             pkgs/main/linux-64::python-3.9.19-h955ad1f_0 
  readline           pkgs/main/linux-64::readline-8.2-h5eee18b_0 
  setuptools         pkgs/main/linux-64::setuptools-68.2.2-py39h06a4308_0 
  sqlite             pkgs/main/linux-64::sqlite-3.41.2-h5eee18b_0 
  tk                 pkgs/main/linux-64::tk-8.6.12-h1ccaba5_0 
  tzdata             pkgs/main/noarch::tzdata-2024a-h04d1e81_0 
  wheel              pkgs/main/linux-64::wheel-0.41.2-py39h06a4308_0 
  xz                 pkgs/main/linux-64::xz-5.4.6-h5eee18b_0 
  zlib               pkgs/main/linux-64::zlib-1.2.13-h5eee18b_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snap_cluster_setup
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) brando9@skampere1~ $ conda activate snap_cluster_setup
(snap_cluster_setup) brando9@skampere1~ $ which python
/lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup/bin/python
(snap_cluster_setup) brando9@skampere1~ $ pip install --upgrade pip
Requirement already satisfied: pip in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (24.0)

(snap_cluster_setup) brando9@skampere1~ $ pip install wandb
Requirement already satisfied: wandb in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (0.16.6)
Requirement already satisfied: Click!=8.0.0,>=7.1 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (8.1.7)
Requirement already satisfied: GitPython!=3.1.29,>=1.0.0 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (3.1.43)
Requirement already satisfied: requests<3,>=2.0.0 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (2.31.0)
Requirement already satisfied: psutil>=5.0.0 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (5.9.8)
Requirement already satisfied: sentry-sdk>=1.0.0 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (1.44.1)
Requirement already satisfied: docker-pycreds>=0.4.0 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (0.4.0)
Requirement already satisfied: PyYAML in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (6.0.1)
Requirement already satisfied: setproctitle in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (1.3.3)
Requirement already satisfied: setuptools in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (68.2.2)
Requirement already satisfied: appdirs>=1.4.3 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (1.4.4)
Requirement already satisfied: typing-extensions in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (4.11.0)
Requirement already satisfied: protobuf!=4.21.0,<5,>=3.15.0 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from wandb) (4.25.3)
Requirement already satisfied: six>=1.4.0 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from docker-pycreds>=0.4.0->wandb) (1.16.0)
Requirement already satisfied: gitdb<5,>=4.0.1 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from GitPython!=3.1.29,>=1.0.0->wandb) (4.0.11)
Requirement already satisfied: charset-normalizer<4,>=2 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from requests<3,>=2.0.0->wandb) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from requests<3,>=2.0.0->wandb) (3.6)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from requests<3,>=2.0.0->wandb) (2.2.1)
Requirement already satisfied: certifi>=2017.4.17 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from requests<3,>=2.0.0->wandb) (2024.2.2)
Requirement already satisfied: smmap<6,>=3.0.1 in ./miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from gitdb<5,>=4.0.1->GitPython!=3.1.29,>=1.0.0->wandb) (5.0.1)
```
Note: to remove a conda env do `conda remove --name snap_cluster_setup --all`, careful!
Note: sometimes you might have to do `pip3`, not sure why pip is inconsistent. 

## Setting up a python project and using an editable pip installation (pip install -e .)
At this point, you know what the environment variable `$HOME` is, and it is pointing to your/any node’s lfs path as suggested by this .bahrc file (but using your CSID instead of Brando’s). In addition, you have created a fork of the snap-cluster-setup github repo in your afs root, and made sure you have a soft link in your lfs pointing to the afs path of the github repo. You also created a conda environment in your lfs (NOT your afs). You also know why we put large storage things (like conda installations and data or models) in your working node’s lfs and not lfs or afs (if not review it here).

### Setting up a python project with setup.py and testing imports
Every programming language has it's own way to organize installations of the project itself and it's depedencies. 
In python usually you have one folder called `src` where the python code goes and you tell `setup.py` that it is the projects root package. 
For details see the comments in this project [`setup.py`](https://github.com/brando90/snap-cluster-setup/blob/main/setup.py).
In particular see the [`package_dir={'': 'src'}` line](https://github.com/brando90/snap-cluster-setup/blob/f2211e3642b5f5d495c7f8f26d6ba8f92178d4c6/setup.py#L28) and [`packages=find_packages('src')`](https://github.com/brando90/snap-cluster-setup/blob/f2211e3642b5f5d495c7f8f26d6ba8f92178d4c6/setup.py#L45) and the accompanying documentation and the [setuptools website](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#using-find-or-find-packages) to get a feel of how python packages are installed. 
Note: one reason that file is heavily documented is because I often forget how python packages have to be install (since it's programming language depdent e.g., Coq and Lean are different).

Now that you know how the `setup.p`y has to be set up for this projects source code to work and with an example of the dependencies, let’s install this code's python repo. 
For this we will pip install this project in editable (development) mode, usually done with `pip install -e .` or `pip install -e <path_2_setup.py>` or `pip install -e $HOME/setup.py`. 
Usually a python project is installed with `pip install <package_name>` and that install a **fixed** usually non-editable version of it. 
If we do `pip install <package_name>` it won't work since our project has not been pushed to the internat. 
Instead we will install locally an editable version -- **so that whenever you make code edits you run the new code**. 
For that you will run **one** of the following editable install commands: 
```bash
cd <path_2_your_project_root>
pip install -e .

# OR
pip install -e $HOME/setup.py

# check it installed
pip list | grep <name_github_repo>

# check all installations
pip list
```
This will install this package and all it's depedencies in the location where you installed conda (for us `~/minicoda` or sometimes in other places like `~/opt` or even `~/.minicoda` but it is conda installation dedepdent!). 
Note: you can also check the installations conda has done so far with `conda list` (but, perhaps confusingly, we are avoiding `conda` to install).

Sample output (note: I pasted the whole thing to emphasize I am reading the output, because if something does NOT isntall you usually have to fix it! e.g., a common issue is the version of pytorch or vllm and it has to be the right version according to the hardware you use and sometimes you have to manually install and unistall packages. So don't ever assume the installation instructions work for your setting!):
```bash
(snap_cluster_setup) brando9@skampere1~ $ cd ~/snap-cluster-setup
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ pip install -e .
Obtaining file:///afs/cs.stanford.edu/u/brando9/snap-cluster-setup
  Preparing metadata (setup.py) ... done
Collecting dill (from snap-cluster-setup==0.0.1)
  Using cached dill-0.3.8-py3-none-any.whl.metadata (10 kB)
Collecting networkx>=2.5 (from snap-cluster-setup==0.0.1)
  Using cached networkx-3.2.1-py3-none-any.whl.metadata (5.2 kB)
Collecting scipy (from snap-cluster-setup==0.0.1)
  Using cached scipy-1.13.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
Collecting scikit-learn (from snap-cluster-setup==0.0.1)
  Using cached scikit_learn-1.4.1.post1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
Collecting lark-parser (from snap-cluster-setup==0.0.1)
  Using cached lark_parser-0.12.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting tensorboard (from snap-cluster-setup==0.0.1)
  Using cached tensorboard-2.16.2-py3-none-any.whl.metadata (1.6 kB)
Collecting pandas (from snap-cluster-setup==0.0.1)
  Using cached pandas-2.2.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)
Collecting progressbar2 (from snap-cluster-setup==0.0.1)
  Using cached progressbar2-4.4.2-py3-none-any.whl.metadata (17 kB)
Collecting requests (from snap-cluster-setup==0.0.1)
  Using cached requests-2.31.0-py3-none-any.whl.metadata (4.6 kB)
Collecting aiohttp (from snap-cluster-setup==0.0.1)
  Using cached aiohttp-3.9.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.4 kB)
Collecting numpy (from snap-cluster-setup==0.0.1)
  Using cached numpy-1.26.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (61 kB)
Collecting plotly (from snap-cluster-setup==0.0.1)
  Using cached plotly-5.20.0-py3-none-any.whl.metadata (7.0 kB)
Collecting wandb (from snap-cluster-setup==0.0.1)
  Using cached wandb-0.16.6-py3-none-any.whl.metadata (10 kB)
Collecting matplotlib (from snap-cluster-setup==0.0.1)
  Using cached matplotlib-3.8.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
Collecting twine (from snap-cluster-setup==0.0.1)
  Using cached twine-5.0.0-py3-none-any.whl.metadata (3.3 kB)
Collecting torch==2.1.2 (from snap-cluster-setup==0.0.1)
  Using cached torch-2.1.2-cp39-cp39-manylinux1_x86_64.whl.metadata (25 kB)
Collecting transformers==4.39.2 (from snap-cluster-setup==0.0.1)
  Using cached transformers-4.39.2-py3-none-any.whl.metadata (134 kB)
Collecting datasets==2.18.0 (from snap-cluster-setup==0.0.1)
  Using cached datasets-2.18.0-py3-none-any.whl.metadata (20 kB)
Collecting filelock (from datasets==2.18.0->snap-cluster-setup==0.0.1)
  Using cached filelock-3.13.3-py3-none-any.whl.metadata (2.8 kB)
Collecting pyarrow>=12.0.0 (from datasets==2.18.0->snap-cluster-setup==0.0.1)
  Using cached pyarrow-15.0.2-cp39-cp39-manylinux_2_28_x86_64.whl.metadata (3.0 kB)
Collecting pyarrow-hotfix (from datasets==2.18.0->snap-cluster-setup==0.0.1)
  Using cached pyarrow_hotfix-0.6-py3-none-any.whl.metadata (3.6 kB)
Collecting tqdm>=4.62.1 (from datasets==2.18.0->snap-cluster-setup==0.0.1)
  Using cached tqdm-4.66.2-py3-none-any.whl.metadata (57 kB)
Collecting xxhash (from datasets==2.18.0->snap-cluster-setup==0.0.1)
  Using cached xxhash-3.4.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (12 kB)
Collecting multiprocess (from datasets==2.18.0->snap-cluster-setup==0.0.1)
  Using cached multiprocess-0.70.16-py39-none-any.whl.metadata (7.2 kB)
Collecting fsspec<=2024.2.0,>=2023.1.0 (from fsspec[http]<=2024.2.0,>=2023.1.0->datasets==2.18.0->snap-cluster-setup==0.0.1)
  Using cached fsspec-2024.2.0-py3-none-any.whl.metadata (6.8 kB)
Collecting huggingface-hub>=0.19.4 (from datasets==2.18.0->snap-cluster-setup==0.0.1)
  Using cached huggingface_hub-0.22.2-py3-none-any.whl.metadata (12 kB)
Collecting packaging (from datasets==2.18.0->snap-cluster-setup==0.0.1)
  Using cached packaging-24.0-py3-none-any.whl.metadata (3.2 kB)
Collecting pyyaml>=5.1 (from datasets==2.18.0->snap-cluster-setup==0.0.1)
  Using cached PyYAML-6.0.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.1 kB)
Collecting typing-extensions (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached typing_extensions-4.11.0-py3-none-any.whl.metadata (3.0 kB)
Collecting sympy (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached sympy-1.12-py3-none-any.whl.metadata (12 kB)
Collecting jinja2 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached Jinja2-3.1.3-py3-none-any.whl.metadata (3.3 kB)
Collecting nvidia-cuda-nvrtc-cu12==12.1.105 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_cuda_nvrtc_cu12-12.1.105-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-cuda-runtime-cu12==12.1.105 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_cuda_runtime_cu12-12.1.105-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-cuda-cupti-cu12==12.1.105 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_cuda_cupti_cu12-12.1.105-py3-none-manylinux1_x86_64.whl.metadata (1.6 kB)
Collecting nvidia-cudnn-cu12==8.9.2.26 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl.metadata (1.6 kB)
Collecting nvidia-cublas-cu12==12.1.3.1 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_cublas_cu12-12.1.3.1-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-cufft-cu12==11.0.2.54 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_cufft_cu12-11.0.2.54-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-curand-cu12==10.3.2.106 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_curand_cu12-10.3.2.106-py3-none-manylinux1_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-cusolver-cu12==11.4.5.107 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_cusolver_cu12-11.4.5.107-py3-none-manylinux1_x86_64.whl.metadata (1.6 kB)
Collecting nvidia-cusparse-cu12==12.1.0.106 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_cusparse_cu12-12.1.0.106-py3-none-manylinux1_x86_64.whl.metadata (1.6 kB)
Collecting nvidia-nccl-cu12==2.18.1 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_nccl_cu12-2.18.1-py3-none-manylinux1_x86_64.whl.metadata (1.8 kB)
Collecting nvidia-nvtx-cu12==12.1.105 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_nvtx_cu12-12.1.105-py3-none-manylinux1_x86_64.whl.metadata (1.7 kB)
Collecting triton==2.1.0 (from torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached triton-2.1.0-0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.3 kB)
Collecting regex!=2019.12.17 (from transformers==4.39.2->snap-cluster-setup==0.0.1)
  Using cached regex-2023.12.25-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (40 kB)
Collecting tokenizers<0.19,>=0.14 (from transformers==4.39.2->snap-cluster-setup==0.0.1)
  Using cached tokenizers-0.15.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.7 kB)
Collecting safetensors>=0.4.1 (from transformers==4.39.2->snap-cluster-setup==0.0.1)
  Using cached safetensors-0.4.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.8 kB)
Collecting nvidia-nvjitlink-cu12 (from nvidia-cusolver-cu12==11.4.5.107->torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)
Collecting charset-normalizer<4,>=2 (from requests->snap-cluster-setup==0.0.1)
  Using cached charset_normalizer-3.3.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (33 kB)
Collecting idna<4,>=2.5 (from requests->snap-cluster-setup==0.0.1)
  Using cached idna-3.6-py3-none-any.whl.metadata (9.9 kB)
Collecting urllib3<3,>=1.21.1 (from requests->snap-cluster-setup==0.0.1)
  Using cached urllib3-2.2.1-py3-none-any.whl.metadata (6.4 kB)
Collecting certifi>=2017.4.17 (from requests->snap-cluster-setup==0.0.1)
  Using cached certifi-2024.2.2-py3-none-any.whl.metadata (2.2 kB)
Collecting aiosignal>=1.1.2 (from aiohttp->snap-cluster-setup==0.0.1)
  Using cached aiosignal-1.3.1-py3-none-any.whl.metadata (4.0 kB)
Collecting attrs>=17.3.0 (from aiohttp->snap-cluster-setup==0.0.1)
  Using cached attrs-23.2.0-py3-none-any.whl.metadata (9.5 kB)
Collecting frozenlist>=1.1.1 (from aiohttp->snap-cluster-setup==0.0.1)
  Using cached frozenlist-1.4.1-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (12 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp->snap-cluster-setup==0.0.1)
  Using cached multidict-6.0.5-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.2 kB)
Collecting yarl<2.0,>=1.0 (from aiohttp->snap-cluster-setup==0.0.1)
  Using cached yarl-1.9.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (31 kB)
Collecting async-timeout<5.0,>=4.0 (from aiohttp->snap-cluster-setup==0.0.1)
  Using cached async_timeout-4.0.3-py3-none-any.whl.metadata (4.2 kB)
Collecting contourpy>=1.0.1 (from matplotlib->snap-cluster-setup==0.0.1)
  Using cached contourpy-1.2.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
Collecting cycler>=0.10 (from matplotlib->snap-cluster-setup==0.0.1)
  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib->snap-cluster-setup==0.0.1)
  Using cached fonttools-4.51.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (159 kB)
Collecting kiwisolver>=1.3.1 (from matplotlib->snap-cluster-setup==0.0.1)
  Using cached kiwisolver-1.4.5-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl.metadata (6.4 kB)
Collecting pillow>=8 (from matplotlib->snap-cluster-setup==0.0.1)
  Using cached pillow-10.3.0-cp39-cp39-manylinux_2_28_x86_64.whl.metadata (9.2 kB)
Collecting pyparsing>=2.3.1 (from matplotlib->snap-cluster-setup==0.0.1)
  Using cached pyparsing-3.1.2-py3-none-any.whl.metadata (5.1 kB)
Collecting python-dateutil>=2.7 (from matplotlib->snap-cluster-setup==0.0.1)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting importlib-resources>=3.2.0 (from matplotlib->snap-cluster-setup==0.0.1)
  Using cached importlib_resources-6.4.0-py3-none-any.whl.metadata (3.9 kB)
Collecting pytz>=2020.1 (from pandas->snap-cluster-setup==0.0.1)
  Using cached pytz-2024.1-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas->snap-cluster-setup==0.0.1)
  Using cached tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting tenacity>=6.2.0 (from plotly->snap-cluster-setup==0.0.1)
  Using cached tenacity-8.2.3-py3-none-any.whl.metadata (1.0 kB)
Collecting python-utils>=3.8.1 (from progressbar2->snap-cluster-setup==0.0.1)
  Using cached python_utils-3.8.2-py2.py3-none-any.whl.metadata (9.7 kB)
Collecting joblib>=1.2.0 (from scikit-learn->snap-cluster-setup==0.0.1)
  Using cached joblib-1.4.0-py3-none-any.whl.metadata (5.4 kB)
Collecting threadpoolctl>=2.0.0 (from scikit-learn->snap-cluster-setup==0.0.1)
  Using cached threadpoolctl-3.4.0-py3-none-any.whl.metadata (13 kB)
Collecting absl-py>=0.4 (from tensorboard->snap-cluster-setup==0.0.1)
  Using cached absl_py-2.1.0-py3-none-any.whl.metadata (2.3 kB)
Collecting grpcio>=1.48.2 (from tensorboard->snap-cluster-setup==0.0.1)
  Using cached grpcio-1.62.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Collecting markdown>=2.6.8 (from tensorboard->snap-cluster-setup==0.0.1)
  Using cached Markdown-3.6-py3-none-any.whl.metadata (7.0 kB)
Collecting protobuf!=4.24.0,>=3.19.6 (from tensorboard->snap-cluster-setup==0.0.1)
  Using cached protobuf-5.26.1-cp37-abi3-manylinux2014_x86_64.whl.metadata (592 bytes)
Requirement already satisfied: setuptools>=41.0.0 in /lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages (from tensorboard->snap-cluster-setup==0.0.1) (68.2.2)
Collecting six>1.9 (from tensorboard->snap-cluster-setup==0.0.1)
  Using cached six-1.16.0-py2.py3-none-any.whl.metadata (1.8 kB)
Collecting tensorboard-data-server<0.8.0,>=0.7.0 (from tensorboard->snap-cluster-setup==0.0.1)
  Using cached tensorboard_data_server-0.7.2-py3-none-manylinux_2_31_x86_64.whl.metadata (1.1 kB)
Collecting werkzeug>=1.0.1 (from tensorboard->snap-cluster-setup==0.0.1)
  Using cached werkzeug-3.0.2-py3-none-any.whl.metadata (4.1 kB)
Collecting pkginfo>=1.8.1 (from twine->snap-cluster-setup==0.0.1)
  Using cached pkginfo-1.10.0-py3-none-any.whl.metadata (11 kB)
Collecting readme-renderer>=35.0 (from twine->snap-cluster-setup==0.0.1)
  Using cached readme_renderer-43.0-py3-none-any.whl.metadata (2.8 kB)
Collecting requests-toolbelt!=0.9.0,>=0.8.0 (from twine->snap-cluster-setup==0.0.1)
  Using cached requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
Collecting importlib-metadata>=3.6 (from twine->snap-cluster-setup==0.0.1)
  Using cached importlib_metadata-7.1.0-py3-none-any.whl.metadata (4.7 kB)
Collecting keyring>=15.1 (from twine->snap-cluster-setup==0.0.1)
  Using cached keyring-25.1.0-py3-none-any.whl.metadata (20 kB)
Collecting rfc3986>=1.4.0 (from twine->snap-cluster-setup==0.0.1)
  Using cached rfc3986-2.0.0-py2.py3-none-any.whl.metadata (6.6 kB)
Collecting rich>=12.0.0 (from twine->snap-cluster-setup==0.0.1)
  Using cached rich-13.7.1-py3-none-any.whl.metadata (18 kB)
Collecting Click!=8.0.0,>=7.1 (from wandb->snap-cluster-setup==0.0.1)
  Using cached click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting GitPython!=3.1.29,>=1.0.0 (from wandb->snap-cluster-setup==0.0.1)
  Using cached GitPython-3.1.43-py3-none-any.whl.metadata (13 kB)
Collecting psutil>=5.0.0 (from wandb->snap-cluster-setup==0.0.1)
  Using cached psutil-5.9.8-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (21 kB)
Collecting sentry-sdk>=1.0.0 (from wandb->snap-cluster-setup==0.0.1)
  Using cached sentry_sdk-1.44.1-py2.py3-none-any.whl.metadata (9.9 kB)
Collecting docker-pycreds>=0.4.0 (from wandb->snap-cluster-setup==0.0.1)
  Using cached docker_pycreds-0.4.0-py2.py3-none-any.whl.metadata (1.8 kB)
Collecting setproctitle (from wandb->snap-cluster-setup==0.0.1)
  Using cached setproctitle-1.3.3-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.9 kB)
Collecting appdirs>=1.4.3 (from wandb->snap-cluster-setup==0.0.1)
  Using cached appdirs-1.4.4-py2.py3-none-any.whl.metadata (9.0 kB)
Collecting protobuf!=4.24.0,>=3.19.6 (from tensorboard->snap-cluster-setup==0.0.1)
  Using cached protobuf-4.25.3-cp37-abi3-manylinux2014_x86_64.whl.metadata (541 bytes)
Collecting gitdb<5,>=4.0.1 (from GitPython!=3.1.29,>=1.0.0->wandb->snap-cluster-setup==0.0.1)
  Using cached gitdb-4.0.11-py3-none-any.whl.metadata (1.2 kB)
Collecting zipp>=0.5 (from importlib-metadata>=3.6->twine->snap-cluster-setup==0.0.1)
  Using cached zipp-3.18.1-py3-none-any.whl.metadata (3.5 kB)
Collecting jaraco.classes (from keyring>=15.1->twine->snap-cluster-setup==0.0.1)
  Using cached jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
Collecting jaraco.functools (from keyring>=15.1->twine->snap-cluster-setup==0.0.1)
  Using cached jaraco.functools-4.0.0-py3-none-any.whl.metadata (3.1 kB)
Collecting jaraco.context (from keyring>=15.1->twine->snap-cluster-setup==0.0.1)
  Using cached jaraco.context-5.3.0-py3-none-any.whl.metadata (4.0 kB)
Collecting SecretStorage>=3.2 (from keyring>=15.1->twine->snap-cluster-setup==0.0.1)
  Using cached SecretStorage-3.3.3-py3-none-any.whl.metadata (4.0 kB)
Collecting jeepney>=0.4.2 (from keyring>=15.1->twine->snap-cluster-setup==0.0.1)
  Using cached jeepney-0.8.0-py3-none-any.whl.metadata (1.3 kB)
Collecting nh3>=0.2.14 (from readme-renderer>=35.0->twine->snap-cluster-setup==0.0.1)
  Using cached nh3-0.2.17-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.7 kB)
Collecting docutils>=0.13.1 (from readme-renderer>=35.0->twine->snap-cluster-setup==0.0.1)
  Using cached docutils-0.20.1-py3-none-any.whl.metadata (2.8 kB)
Collecting Pygments>=2.5.1 (from readme-renderer>=35.0->twine->snap-cluster-setup==0.0.1)
  Using cached pygments-2.17.2-py3-none-any.whl.metadata (2.6 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=12.0.0->twine->snap-cluster-setup==0.0.1)
  Using cached markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Collecting MarkupSafe>=2.1.1 (from werkzeug>=1.0.1->tensorboard->snap-cluster-setup==0.0.1)
  Using cached MarkupSafe-2.1.5-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)
Collecting mpmath>=0.19 (from sympy->torch==2.1.2->snap-cluster-setup==0.0.1)
  Using cached mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->GitPython!=3.1.29,>=1.0.0->wandb->snap-cluster-setup==0.0.1)
  Using cached smmap-5.0.1-py3-none-any.whl.metadata (4.3 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=12.0.0->twine->snap-cluster-setup==0.0.1)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting cryptography>=2.0 (from SecretStorage>=3.2->keyring>=15.1->twine->snap-cluster-setup==0.0.1)
  Using cached cryptography-42.0.5-cp39-abi3-manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting more-itertools (from jaraco.classes->keyring>=15.1->twine->snap-cluster-setup==0.0.1)
  Using cached more_itertools-10.2.0-py3-none-any.whl.metadata (34 kB)
Collecting backports.tarfile (from jaraco.context->keyring>=15.1->twine->snap-cluster-setup==0.0.1)
  Using cached backports.tarfile-1.0.0-py3-none-any.whl.metadata (1.9 kB)
Collecting cffi>=1.12 (from cryptography>=2.0->SecretStorage>=3.2->keyring>=15.1->twine->snap-cluster-setup==0.0.1)
  Using cached cffi-1.16.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.5 kB)
Collecting pycparser (from cffi>=1.12->cryptography>=2.0->SecretStorage>=3.2->keyring>=15.1->twine->snap-cluster-setup==0.0.1)
  Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Using cached datasets-2.18.0-py3-none-any.whl (510 kB)
Using cached torch-2.1.2-cp39-cp39-manylinux1_x86_64.whl (670.2 MB)
Using cached transformers-4.39.2-py3-none-any.whl (8.8 MB)
Using cached nvidia_cublas_cu12-12.1.3.1-py3-none-manylinux1_x86_64.whl (410.6 MB)
Using cached nvidia_cuda_cupti_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (14.1 MB)
Using cached nvidia_cuda_nvrtc_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (23.7 MB)
Using cached nvidia_cuda_runtime_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (823 kB)
Using cached nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl (731.7 MB)
Using cached nvidia_cufft_cu12-11.0.2.54-py3-none-manylinux1_x86_64.whl (121.6 MB)
Using cached nvidia_curand_cu12-10.3.2.106-py3-none-manylinux1_x86_64.whl (56.5 MB)
Using cached nvidia_cusolver_cu12-11.4.5.107-py3-none-manylinux1_x86_64.whl (124.2 MB)
Using cached nvidia_cusparse_cu12-12.1.0.106-py3-none-manylinux1_x86_64.whl (196.0 MB)
Using cached nvidia_nccl_cu12-2.18.1-py3-none-manylinux1_x86_64.whl (209.8 MB)
Using cached nvidia_nvtx_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (99 kB)
Using cached triton-2.1.0-0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (89.3 MB)
Using cached dill-0.3.8-py3-none-any.whl (116 kB)
Using cached networkx-3.2.1-py3-none-any.whl (1.6 MB)
Using cached numpy-1.26.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.2 MB)
Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Using cached aiohttp-3.9.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)
Using cached lark_parser-0.12.0-py2.py3-none-any.whl (103 kB)
Using cached matplotlib-3.8.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
Using cached pandas-2.2.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.0 MB)
Using cached plotly-5.20.0-py3-none-any.whl (15.7 MB)
Using cached progressbar2-4.4.2-py3-none-any.whl (56 kB)
Using cached scikit_learn-1.4.1.post1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.2 MB)
Using cached scipy-1.13.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (38.6 MB)
Using cached tensorboard-2.16.2-py3-none-any.whl (5.5 MB)
Using cached twine-5.0.0-py3-none-any.whl (37 kB)
Using cached wandb-0.16.6-py3-none-any.whl (2.2 MB)
Using cached absl_py-2.1.0-py3-none-any.whl (133 kB)
Using cached aiosignal-1.3.1-py3-none-any.whl (7.6 kB)
Using cached appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)
Using cached async_timeout-4.0.3-py3-none-any.whl (5.7 kB)
Using cached attrs-23.2.0-py3-none-any.whl (60 kB)
Using cached certifi-2024.2.2-py3-none-any.whl (163 kB)
Using cached charset_normalizer-3.3.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (142 kB)
Using cached click-8.1.7-py3-none-any.whl (97 kB)
Using cached contourpy-1.2.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (304 kB)
Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Using cached docker_pycreds-0.4.0-py2.py3-none-any.whl (9.0 kB)
Using cached fonttools-4.51.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
Using cached frozenlist-1.4.1-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (240 kB)
Using cached fsspec-2024.2.0-py3-none-any.whl (170 kB)
Using cached GitPython-3.1.43-py3-none-any.whl (207 kB)
Using cached grpcio-1.62.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.6 MB)
Using cached huggingface_hub-0.22.2-py3-none-any.whl (388 kB)
Using cached idna-3.6-py3-none-any.whl (61 kB)
Using cached importlib_metadata-7.1.0-py3-none-any.whl (24 kB)
Using cached importlib_resources-6.4.0-py3-none-any.whl (38 kB)
Using cached joblib-1.4.0-py3-none-any.whl (301 kB)
Using cached keyring-25.1.0-py3-none-any.whl (37 kB)
Using cached kiwisolver-1.4.5-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
Using cached Markdown-3.6-py3-none-any.whl (105 kB)
Using cached multidict-6.0.5-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (123 kB)
Using cached packaging-24.0-py3-none-any.whl (53 kB)
Using cached pillow-10.3.0-cp39-cp39-manylinux_2_28_x86_64.whl (4.5 MB)
Using cached pkginfo-1.10.0-py3-none-any.whl (30 kB)
Using cached protobuf-4.25.3-cp37-abi3-manylinux2014_x86_64.whl (294 kB)
Using cached psutil-5.9.8-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (288 kB)
Using cached pyarrow-15.0.2-cp39-cp39-manylinux_2_28_x86_64.whl (38.3 MB)
Using cached pyparsing-3.1.2-py3-none-any.whl (103 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached python_utils-3.8.2-py2.py3-none-any.whl (27 kB)
Using cached pytz-2024.1-py2.py3-none-any.whl (505 kB)
Using cached PyYAML-6.0.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (738 kB)
Using cached readme_renderer-43.0-py3-none-any.whl (13 kB)
Using cached regex-2023.12.25-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (773 kB)
Using cached requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
Using cached rfc3986-2.0.0-py2.py3-none-any.whl (31 kB)
Using cached rich-13.7.1-py3-none-any.whl (240 kB)
Using cached safetensors-0.4.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
Using cached sentry_sdk-1.44.1-py2.py3-none-any.whl (266 kB)
Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Using cached tenacity-8.2.3-py3-none-any.whl (24 kB)
Using cached tensorboard_data_server-0.7.2-py3-none-manylinux_2_31_x86_64.whl (6.6 MB)
Using cached threadpoolctl-3.4.0-py3-none-any.whl (17 kB)
Using cached tokenizers-0.15.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.6 MB)
Using cached tqdm-4.66.2-py3-none-any.whl (78 kB)
Using cached typing_extensions-4.11.0-py3-none-any.whl (34 kB)
Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
Using cached urllib3-2.2.1-py3-none-any.whl (121 kB)
Using cached werkzeug-3.0.2-py3-none-any.whl (226 kB)
Using cached yarl-1.9.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (304 kB)
Using cached filelock-3.13.3-py3-none-any.whl (11 kB)
Using cached Jinja2-3.1.3-py3-none-any.whl (133 kB)
Using cached multiprocess-0.70.16-py39-none-any.whl (133 kB)
Using cached pyarrow_hotfix-0.6-py3-none-any.whl (7.9 kB)
Using cached setproctitle-1.3.3-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (30 kB)
Using cached sympy-1.12-py3-none-any.whl (5.7 MB)
Using cached xxhash-3.4.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (193 kB)
Using cached docutils-0.20.1-py3-none-any.whl (572 kB)
Using cached gitdb-4.0.11-py3-none-any.whl (62 kB)
Using cached jeepney-0.8.0-py3-none-any.whl (48 kB)
Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Using cached MarkupSafe-2.1.5-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)
Using cached nh3-0.2.17-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (777 kB)
Using cached pygments-2.17.2-py3-none-any.whl (1.2 MB)
Using cached SecretStorage-3.3.3-py3-none-any.whl (15 kB)
Using cached zipp-3.18.1-py3-none-any.whl (8.2 kB)
Using cached jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
Using cached jaraco.context-5.3.0-py3-none-any.whl (6.5 kB)
Using cached jaraco.functools-4.0.0-py3-none-any.whl (9.8 kB)
Using cached nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (21.1 MB)
Using cached cryptography-42.0.5-cp39-abi3-manylinux_2_28_x86_64.whl (4.6 MB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Using cached smmap-5.0.1-py3-none-any.whl (24 kB)
Using cached backports.tarfile-1.0.0-py3-none-any.whl (28 kB)
Using cached more_itertools-10.2.0-py3-none-any.whl (57 kB)
Using cached cffi-1.16.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (443 kB)
Using cached pycparser-2.22-py3-none-any.whl (117 kB)
Installing collected packages: pytz, nh3, mpmath, lark-parser, appdirs, zipp, xxhash, urllib3, tzdata, typing-extensions, tqdm, threadpoolctl, tensorboard-data-server, tenacity, sympy, smmap, six, setproctitle, safetensors, rfc3986, regex, pyyaml, pyparsing, Pygments, pycparser, pyarrow-hotfix, psutil, protobuf, pkginfo, pillow, packaging, nvidia-nvtx-cu12, nvidia-nvjitlink-cu12, nvidia-nccl-cu12, nvidia-curand-cu12, nvidia-cufft-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, numpy, networkx, multidict, more-itertools, mdurl, MarkupSafe, kiwisolver, joblib, jeepney, idna, grpcio, fsspec, frozenlist, fonttools, filelock, docutils, dill, cycler, Click, charset-normalizer, certifi, backports.tarfile, attrs, async-timeout, absl-py, yarl, werkzeug, triton, sentry-sdk, scipy, requests, readme-renderer, python-utils, python-dateutil, pyarrow, plotly, nvidia-cusparse-cu12, nvidia-cudnn-cu12, multiprocess, markdown-it-py, jinja2, jaraco.functools, jaraco.context, jaraco.classes, importlib-resources, importlib-metadata, gitdb, docker-pycreds, contourpy, cffi, aiosignal, scikit-learn, rich, requests-toolbelt, progressbar2, pandas, nvidia-cusolver-cu12, matplotlib, markdown, huggingface-hub, GitPython, cryptography, aiohttp, wandb, torch, tokenizers, tensorboard, SecretStorage, transformers, keyring, datasets, twine, snap-cluster-setup
Running setup.py develop for snap-cluster-setup
Successfully installed Click-8.1.7 GitPython-3.1.43 MarkupSafe-2.1.5 Pygments-2.17.2 SecretStorage-3.3.3 absl-py-2.1.0 aiohttp-3.9.3 aiosignal-1.3.1 appdirs-1.4.4 async-timeout-4.0.3 attrs-23.2.0 backports.tarfile-1.0.0 certifi-2024.2.2 cffi-1.16.0 charset-normalizer-3.3.2 contourpy-1.2.1 cryptography-42.0.5 cycler-0.12.1 datasets-2.18.0 dill-0.3.8 docker-pycreds-0.4.0 docutils-0.20.1 filelock-3.13.3 fonttools-4.51.0 frozenlist-1.4.1 fsspec-2024.2.0 gitdb-4.0.11 grpcio-1.62.1 huggingface-hub-0.22.2 idna-3.6 importlib-metadata-7.1.0 importlib-resources-6.4.0 jaraco.classes-3.4.0 jaraco.context-5.3.0 jaraco.functools-4.0.0 jeepney-0.8.0 jinja2-3.1.3 joblib-1.4.0 keyring-25.1.0 kiwisolver-1.4.5 lark-parser-0.12.0 markdown-3.6 markdown-it-py-3.0.0 matplotlib-3.8.4 mdurl-0.1.2 more-itertools-10.2.0 mpmath-1.3.0 multidict-6.0.5 multiprocess-0.70.16 networkx-3.2.1 nh3-0.2.17 numpy-1.26.4 nvidia-cublas-cu12-12.1.3.1 nvidia-cuda-cupti-cu12-12.1.105 nvidia-cuda-nvrtc-cu12-12.1.105 nvidia-cuda-runtime-cu12-12.1.105 nvidia-cudnn-cu12-8.9.2.26 nvidia-cufft-cu12-11.0.2.54 nvidia-curand-cu12-10.3.2.106 nvidia-cusolver-cu12-11.4.5.107 nvidia-cusparse-cu12-12.1.0.106 nvidia-nccl-cu12-2.18.1 nvidia-nvjitlink-cu12-12.4.127 nvidia-nvtx-cu12-12.1.105 packaging-24.0 pandas-2.2.1 pillow-10.3.0 pkginfo-1.10.0 plotly-5.20.0 progressbar2-4.4.2 protobuf-4.25.3 psutil-5.9.8 pyarrow-15.0.2 pyarrow-hotfix-0.6 pycparser-2.22 pyparsing-3.1.2 python-dateutil-2.9.0.post0 python-utils-3.8.2 pytz-2024.1 pyyaml-6.0.1 readme-renderer-43.0 regex-2023.12.25 requests-2.31.0 requests-toolbelt-1.0.0 rfc3986-2.0.0 rich-13.7.1 safetensors-0.4.2 scikit-learn-1.4.1.post1 scipy-1.13.0 sentry-sdk-1.44.1 setproctitle-1.3.3 six-1.16.0 smmap-5.0.1 snap-cluster-setup-0.0.1 sympy-1.12 tenacity-8.2.3 tensorboard-2.16.2 tensorboard-data-server-0.7.2 threadpoolctl-3.4.0 tokenizers-0.15.2 torch-2.1.2 tqdm-4.66.2 transformers-4.39.2 triton-2.1.0 twine-5.0.0 typing-extensions-4.11.0 tzdata-2024.1 urllib3-2.2.1 wandb-0.16.6 werkzeug-3.0.2 xxhash-3.4.1 yarl-1.9.4 zipp-3.18.1
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ pip list | grep snap-cluster-setup
snap-cluster-setup       0.0.1       /afs/cs.stanford.edu/u/brando9/snap-cluster-setup/src
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ pip list
Package                  Version     Editable project location
------------------------ ----------- -----------------------------------------------------
absl-py                  2.1.0
accelerate               0.29.1
aiohttp                  3.9.3
aiosignal                1.3.1
appdirs                  1.4.4
async-timeout            4.0.3
attrs                    20.3.0
bitsandbytes             0.43.0
bnb                      0.3.0
certifi                  2024.2.2
charset-normalizer       3.3.2
click                    7.1.2
contourpy                1.2.1
cycler                   0.12.1
datasets                 2.18.0
dill                     0.3.8
docker-pycreds           0.4.0
filelock                 3.13.3
fonttools                4.51.0
frozenlist               1.4.1
fsspec                   2024.2.0
gitdb                    4.0.11
GitPython                3.1.43
grpcio                   1.62.1
huggingface-hub          0.22.2
idna                     3.6
importlib_metadata       7.1.0
importlib_resources      6.4.0
jax                      0.4.26
Jinja2                   3.1.3
joblib                   1.4.0
kiwisolver               1.4.5
Markdown                 3.6
MarkupSafe               2.1.5
matplotlib               3.8.4
ml-dtypes                0.4.0
mpmath                   1.3.0
multidict                6.0.5
multiprocess             0.70.16
networkx                 3.2.1
numpy                    1.26.4
nvidia-cublas-cu12       12.1.3.1
nvidia-cuda-cupti-cu12   12.1.105
nvidia-cuda-nvrtc-cu12   12.1.105
nvidia-cuda-runtime-cu12 12.1.105
nvidia-cudnn-cu12        8.9.2.26
nvidia-cufft-cu12        11.0.2.54
nvidia-curand-cu12       10.3.2.106
nvidia-cusolver-cu12     11.4.5.107
nvidia-cusparse-cu12     12.1.0.106
nvidia-nccl-cu12         2.19.3
nvidia-nvjitlink-cu12    12.4.127
nvidia-nvtx-cu12         12.1.105
opt-einsum               3.3.0
packaging                24.0
pandas                   2.2.1
patsy                    0.5.6
pillow                   10.3.0
pip                      24.0
plotly                   5.20.0
progressbar2             4.4.2
prompt-toolkit           3.0.43
protobuf                 4.25.3
psutil                   5.9.8
pyarrow                  15.0.2
pyarrow-hotfix           0.6
pyparsing                3.1.2
python-dateutil          2.9.0.post0
python-utils             3.8.2
pytz                     2024.1
PyYAML                   5.4.1
questionary              1.10.0
regex                    2023.12.25
requests                 2.31.0
safetensors              0.4.2
scikit-learn             1.4.1.post1
scipy                    1.13.0
seaborn                  0.13.2
sentencepiece            0.2.0
sentry-sdk               1.44.1
setproctitle             1.3.3
setuptools               68.2.2
six                      1.16.0
smart-getenv             1.1.0
smmap                    5.0.1
snap-cluster-setup       0.0.1       /afs/cs.stanford.edu/u/brando9/snap-cluster-setup/src
statsmodels              0.14.1
sympy                    1.12
tenacity                 8.2.3
tensorboard              2.16.2
tensorboard-data-server  0.7.2
threadpoolctl            3.4.0
tokenizers               0.15.2
torch                    2.2.2
torchaudio               2.2.2
torchvision              0.17.2
tqdm                     4.66.2
transformers             4.39.3
triton                   2.2.0
typing_extensions        4.11.0
tzdata                   2024.1
urllib3                  2.2.1
wandb                    0.16.6
wcwidth                  0.2.13
Werkzeug                 3.0.2
wheel                    0.41.2
xxhash                   3.4.1
yarl                     1.9.4
zipp                     3.18.1
zstandard                0.22.0
```
Note, no errors! But the version of pytorch chaged and it is good to be aware of them or anything funny that might have happened. 

Now that we pip installed this project in editable, we will play around with imports and make sure we installed our project in editable mode. 
Fire up a [python interactive shell or REPL](https://chat.openai.com/c/0924a033-6e5f-4d5e-9c8d-cbc2c521c0cd) (REPL stands for Read-Eval-Print). 
```bash
python
```
then import the function to print hello from the `hello_world.py` module in `src`:
```bash
from hello_world import print_hello_snap
```
Sample output;
```bash
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ python
Python 3.9.19 (main, Mar 21 2024, 17:11:28) 
[GCC 11.2.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from hello_world import print_hello_snap
>>> print_hello_snap()
Hello, World from the Snap Cluster Setup src!
```
Now check that your imports work! i.e., that you can use code form another file/package:
```bash
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ python
Python 3.9.19 (main, Mar 21 2024, 17:11:28) 
[GCC 11.2.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from hello_world import print_from_another
>>> print_from_another()
another
```

Now let's try the same but by running a file explicitly:
For that we will do:
```bash
python /lfs/skampere1/0/brando9/snap-cluster-setup/src/hello_world.py
# Or when in your projects root folder usually
python src/hello_world.py
```
Sample output:
```bash
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ python /lfs/skampere1/0/brando9/snap-cluster-setup/src/hello_world.py
Hello, World from the Snap Cluster Setup src!
EDIT THIS
another
Time taken: 0.00 seconds, or 0.00 minutes, or 0.00 hours.
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ python src/hello_world.py
Hello, World from the Snap Cluster Setup src!
EDIT THIS
another
Time taken: 0.00 seconds, or 0.00 minutes, or 0.00 hours.
```
This is where you learn that imports "run" the code they import and that `__name__ == "__main__":` is the code that is run only when you explicitly run this file. 
This python specific. 
I personally use  [`__name__ == "__main__":`](https://www.google.com/search?q=what+is+__name__+%3D%3D+__main__+in+python&rlz=1C5CHFA_enUS741US741&oq=what+is+__name__+in+python&gs_lcrp=EgZjaHJvbWUqCAgDEAAYFhgeMgkIABBFGDkYgAQyCAgBEAAYFhgeMggIAhAAGBYYHjIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yCAgHEAAYFhgeMggICBAAGBYYHjIICAkQABgWGB7SAQg2MzUwajBqN6gCALACAA&sourceid=chrome&ie=UTF-8) to put code for unit tests (but really you can do whatever you want).  


## Installing Pytorch and Cuda
Usually installing pytorch can be non-trivial. 
For example, depending on other depedencies or specific python version you might need, it can lead to taking a few hours downgrading pytorch versions, cuda version, python versions etc. until the fragile depedency set up is done. 
In addition, if the node or cluster is not set up the way you expect, you mind need to e-mail the system admins until the version of cuda (gpu lib for pytorch) you need is installed with the right version and the right environment variables. 
In this case because you likely will use the `vllm` library for fast inference with llms, it means we are forced to use `python 3.9`. 
In this case I already figure out the right version of pytorch from [this vllm git issue.](https://github.com/vllm-project/vllm/issues/2747) and put the right versions of everything in the `setup.py` file. 

Therefore, you only need to run these commands to check that pytorch with a gpu works:
```bash
python -c "import torch; print(torch.__version__); print(torch.version.cuda); print((torch.randn(2, 4).cuda() @ torch.randn(4, 1).cuda()))"
python -c "import torch; print(torch.version.cuda); print((torch.randn(2, 4).cuda() @ torch.randn(4, 1).cuda()))"
python -c "import torch; print(f'{torch.cuda.device_count()=}'); print(f'Device: {torch.cuda.get_device_name(0)=}')"
```
Note: the `-c` is just the quick way to open a python shell and run a command without going manually into the python shell. 
Sample output:
```bash
(snap_cluster_setup) brando9@skampere1~ $ python -c "import torch; print(torch.__version__); print(torch.version.cuda); print((torch.randn(2, 4).cuda() @ torch.randn(4, 1).cuda()))"
"import torch; print(torch.version.cuda); print((torch.randn(2, 4).cuda() @ torch.randn(4, 1).cuda()))"
python -c "import torch; print(f'{torch.cuda.device_count()=}'); print(f'Device: {torch.cuda.get_device_name(0)=}')"
2.1.2+cu121
12.1
tensor([[1.5192],
        [2.3463]], device='cuda:0')
(snap_cluster_setup) brando9@skampere1~ $ python -c "import torch; print(torch.version.cuda); print((torch.randn(2, 4).cuda() @ torch.randn(4, 1).cuda()))"
12.1
tensor([[-0.5750],
        [ 0.2061]], device='cuda:0')
(snap_cluster_setup) brando9@skampere1~ $ python -c "import torch; print(f'{torch.cuda.device_count()=}'); print(f'Device: {torch.cuda.get_device_name(0)=}')"
torch.cuda.device_count()=1
Device: torch.cuda.get_device_name(0)='NVIDIA A100-SXM4-80GB'
```
Note: read the commands and understand what they are. 
Also, let's test vllm:
```bash
python ~/snap-cluster-setup/src/test_vllm.py
```
Note: if you ever use `~` inside python you need to use your some library to expand the user path e.g., `os.path.expanduser(path_string)`.
Sample output:
```bash
(snap_cluster_setup) brando9@skampere1~ $ python /lfs/skampere1/0/brando9/snap-cluster-setup/src/test_vllm.py
INFO 04-08 19:52:46 llm_engine.py:74] Initializing an LLM engine (v0.4.0.post1) with config: model='facebook/opt-125m', tokenizer='facebook/opt-125m', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0)
INFO 04-08 19:52:47 selector.py:51] Cannot use FlashAttention because the package is not found. Please install it for better performance.
INFO 04-08 19:52:47 selector.py:25] Using XFormers backend.
INFO 04-08 19:52:48 weight_utils.py:177] Using model weights format ['*.bin']
INFO 04-08 19:52:49 model_runner.py:104] Loading model weights took 0.2389 GB
INFO 04-08 19:52:49 gpu_executor.py:94] # GPU blocks: 127981, # CPU blocks: 7281
INFO 04-08 19:52:51 model_runner.py:791] Capturing the model for CUDA graphs. This may lead to unexpected consequences if the model is not static. To run the model in eager mode, set 'enforce_eager=True' or use '--enforce-eager' in the CLI.
INFO 04-08 19:52:51 model_runner.py:795] CUDA graphs can take additional 1~3 GiB memory per GPU. If you are running out of memory, consider decreasing `gpu_memory_utilization` or enforcing eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory usage.
INFO 04-08 19:52:53 model_runner.py:867] Graph capturing finished in 2 secs.
Processed prompts: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 53.56it/s]
Prompt: 'Hello, my name is', Generated text: ' Joel, my dad is my friend and we are in a relationship. I am'
Prompt: 'The president of the United States is', Generated text: ' speaking out against the release of some State Department documents which show the Russians are trying'
Prompt: 'The capital of France is', Generated text: ' known as the “Proud French capital”. What is this city'
Prompt: 'The future of AI is', Generated text: ' literally in danger of being taken by any other company.\nAgreed. '
Time taken: 8.17 seconds, or 0.14 minutes, or 0.00 hours.
```
Note: inspect the `test_vllm.py` file, and note vscode might complain it's not installed. I think this happens because it's such optimized code that it's not quite installed in the "standard pytorch way" e.g., the binaries are stored instead of the stnadard pytorch bytes (not sure).

It is often that you are sharing GPUs with other. 
Usually people share GPUs (or compute) with the [slurm workload manger](https://slurm.schedmd.com/documentation.html). 
But in the SNAP cluster we loging to nodes directly. 
Therefore, you might need to make sure the right GPU is available e.g., "righ" meaning one with enough memory for example. 
For that one can do `nvia-smi`. 
Do nvidia-smi:
```bash
nvidia-smi
nvcc --version
```
Sample output:
```bash
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ nvidia-smi
Mon Apr  8 20:02:00 2024       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.54.03              Driver Version: 535.54.03    CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA A100-SXM4-80GB          On  | 00000000:07:00.0 Off |                    0 |
| N/A   31C    P0              64W / 350W |      4MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   1  NVIDIA A100-SXM4-80GB          On  | 00000000:0A:00.0 Off |                    0 |
| N/A   29C    P0              67W / 350W |      4MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   2  NVIDIA A100-SXM4-80GB          On  | 00000000:44:00.0 Off |                    0 |
| N/A   29C    P0              66W / 350W |      4MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   3  NVIDIA A100-SXM4-80GB          On  | 00000000:4A:00.0 Off |                    0 |
| N/A   33C    P0              65W / 350W |      4MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   4  NVIDIA A100-SXM4-80GB          On  | 00000000:84:00.0 Off |                    0 |
| N/A   33C    P0              64W / 350W |      4MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   5  NVIDIA A100-SXM4-80GB          On  | 00000000:8A:00.0 Off |                    0 |
| N/A   28C    P0              61W / 350W |      4MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   6  NVIDIA A100-SXM4-80GB          On  | 00000000:C0:00.0 Off |                    0 |
| N/A   29C    P0              64W / 350W |      4MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   7  NVIDIA A100-SXM4-80GB          On  | 00000000:C3:00.0 Off |                    0 |
| N/A   31C    P0              62W / 350W |      4MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      uname -a|
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Tue_May__3_18:49:52_PDT_2022
Cuda compilation tools, release 11.7, V11.7.64
Build cuda_11.7.r11.7/compiler.31294372_0
```
The last command is for:
> The command nvcc --version is used to check the version of the NVIDIA CUDA Compiler (NVCC) installed on your system.
To change gpu you can do it with the following env variable:
```bash
export $CUDA_VISIBLE_DEVICES=1
```
for multiple:
```bash
CUDA_VISIBLE_DEVICES=0,7
```
Tip: as reference, I always suggest to at least skim the suggested ways to use resources according to the admins/"official wiki" of the compute cluster you're using -- in this case [skim the suggested way to use GPUs in SNAP](https://ilwiki.stanford.edu/doku.php?id=hints:gpu).

## Long running jobs in SNAP and fine-tuning GPT2
Usually one of the reasons to use a compute cluster, is to dispatch/run long running jobs. 
In a standard cluster (note SNAP's set up is not standard) one usually [uses a workload manager like slurm is more standard](https://slurm.schedmd.com/documentation.html).
This workload manger (e.g., slurm) usually has commands like `srun` or `sbatch` to run an interactive job and a long running background job respectively. 
We will mimic these slurm commands and run them manually. 
The standard workflow in slurm is:

1. ssh/login into the ("non compute") head node (where your code lies in). You do not run real jobs here, it's only for scheduling the jobs with slurm.
2. get your script, data, command etc. ready and ask slurm to run it (`srun` if you need a cli terminal to interact with your job e.g., to get a gpu for debugging or `sbatch` to run a long running job)

In SNAP we will do the following:

1. Since we can ssh directly into **compute nodes** (e.g., with GPUS) -- we don't need `srun`
2. For long running jobs we will use (kerberos) `tmux` to run (because that is [the recommended way to do it in SNAP](https://ilwiki.stanford.edu/doku.php?id=hints:long-jobs))

Note: usually the system admins set up slurm so that you minimally have to worry about the file system (afs, lfs, dfs). 
It usually "just works". If not, they tell you how to take care of it and it's only difficult/extra work if you use a lot of storage or many files (or file descriptors).

### Interactive "job" in SNAP
You should be logged in to a (compute) node already. 
In this case when you ran GPU commands in the python shell previously is the essence of a interactive job! 
You get a node + GPU and you are aple to interact with it. 
Now we will expand that so that you run GPT2 fine tunning with Hugging Face (HF). 
For that make sure you check which GPU is free and then set up which GPU you want:
```bash
nvidia-smi
# I saw the output and all gpus were free so I choose any gpu
export CUDA_VISIBLE_DEVICES=0
```
Tip: never run commands blindly or they will fail and you won't be able to debug them. 
Tip: do you know what `CUDA_VISIBLE_DEVICES` is for? 

Now let's run a small training run for GPT2 small. 
We are doing small to avoid memory issues, which is a common problem in LLM projects and one that eventually you need to know how to solve 
(according to the reqs for your project! e.g., many many options, some open problems; larger gpu, use fsdp, use lora, use qlora, hf accelerate, deep speed. 
Feel free to Google them if you are curious, but you will use them as your requirement for your project need them).
Using the code from your fork, run: 
```bash
python ~/snap-cluster-setup/src/train/simple_train.py 
# or CUDA_VISIBLE_DEVICES=0 python ~/snap-cluster-setup/src/train/simple_train.py 
```
Sample output:
```bash
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ python ~/snap-cluster-setup/src/train/simple_train.py 
tokenizer.pad_token='<|endoftext|>'
block_size=1024
Number of parameters: 124439808
/lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages/accelerate/accelerator.py:436: FutureWarning: Passing the following arguments to `Accelerator` is deprecated and will be removed in version 1.0 of Accelerate: dict_keys(['dispatch_batches', 'split_batches', 'even_batches', 'use_seedable_sampler']). Please pass an `accelerate.DataLoaderConfiguration` instead: 
dataloader_config = DataLoaderConfiguration(dispatch_batches=None, split_batches=False, even_batches=True, use_seedable_sampler=True)
  warnings.warn(
Detected kernel version 5.4.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
{'train_runtime': 4.4686, 'train_samples_per_second': 41.4, 'train_steps_per_second': 10.294, 'train_loss': 2.902917944866678, 'epoch': 0.99}                                                                                                                                                                                                                                                       
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 46/46 [00:04<00:00, 10.30it/s]
/lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages/accelerate/accelerator.py:436: FutureWarning: Passing the following arguments to `Accelerator` is deprecated and will be removed in version 1.0 of Accelerate: dict_keys(['dispatch_batches', 'split_batches', 'even_batches', 'use_seedable_sampler']). Please pass an `accelerate.DataLoaderConfiguration` instead: 
dataloader_config = DataLoaderConfiguration(dispatch_batches=None, split_batches=False, even_batches=True, use_seedable_sampler=True)
  warnings.warn(
Detected kernel version 5.4.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 24/24 [00:00<00:00, 28.52it/s]
Eval metrics hoskinson-center_proofnet  test Unknown_Eval_Max_Samples: metrics={'eval_loss': 2.3169755935668945, 'eval_runtime': 0.8879, 'eval_samples_per_second': 209.491, 'eval_steps_per_second': 27.031, 'perplexity': 10.144945422979891}
***** eval_hoskinson-center_proofnet__test_Unknown_Eval_Max_Samples metrics *****
  eval_loss               =      2.317
  eval_runtime            = 0:00:00.88
  eval_samples_per_second =    209.491
  eval_steps_per_second   =     27.031
  perplexity              =    10.1449
path='hoskinson-center/proofnet' split=test results={'eval_loss': 2.3169755935668945, 'eval_runtime': 0.8879, 'eval_samples_per_second': 209.491, 'eval_steps_per_second': 27.031, 'perplexity': 10.144945422979891}
Time taken: 12.64 seconds, or 0.21 minutes, or 0.00 hours.
```


Now edit your gpt2 small file to use wandb and to train for more epochs:
```bash
CUDA_VISIBLE_DEVICES=0 python ~/snap-cluster-setup/src/train/simple_train.py
```
Sample output:
```bash
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ python ~/snap-cluster-setup/src/train/simple_train.py 
tokenizer.pad_token='<|endoftext|>'
block_size=1024
Number of parameters: 124439808
/lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages/accelerate/accelerator.py:436: FutureWarning: Passing the following arguments to `Accelerator` is deprecated and will be removed in version 1.0 of Accelerate: dict_keys(['dispatch_batches', 'split_batches', 'even_batches', 'use_seedable_sampler']). Please pass an `accelerate.DataLoaderConfiguration` instead: 
dataloader_config = DataLoaderConfiguration(dispatch_batches=None, split_batches=False, even_batches=True, use_seedable_sampler=True)
  warnings.warn(
Detected kernel version 5.4.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
wandb: Currently logged in as: brando. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.6
wandb: Run data is saved locally in /lfs/skampere1/0/brando9/wandb/run-20240410_180758-7tns0d5y
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run morning-music-5
wandb: ⭐️ View project at https://wandb.ai/brando/huggingface
wandb: 🚀 View run at https://wandb.ai/brando/huggingface/runs/7tns0d5y
{'train_runtime': 9.9081, 'train_samples_per_second': 18.672, 'train_steps_per_second': 4.643, 'train_loss': 2.902917944866678, 'epoch': 0.99}                                                                                                                                                                                                                                                      
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 46/46 [00:04<00:00, 10.46it/s]
/lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages/accelerate/accelerator.py:436: FutureWarning: Passing the following arguments to `Accelerator` is deprecated and will be removed in version 1.0 of Accelerate: dict_keys(['dispatch_batches', 'split_batches', 'even_batches', 'use_seedable_sampler']). Please pass an `accelerate.DataLoaderConfiguration` instead: 
dataloader_config = DataLoaderConfiguration(dispatch_batches=None, split_batches=False, even_batches=True, use_seedable_sampler=True)
  warnings.warn(
Detected kernel version 5.4.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 24/24 [00:00<00:00, 28.45it/s]
Eval metrics hoskinson-center_proofnet  test Unknown_Eval_Max_Samples: metrics={'eval_loss': 2.3169755935668945, 'eval_runtime': 0.886, 'eval_samples_per_second': 209.933, 'eval_steps_per_second': 27.088, 'perplexity': 10.144945422979891}
***** eval_hoskinson-center_proofnet__test_Unknown_Eval_Max_Samples metrics *****
  eval_loss               =      2.317
  eval_runtime            = 0:00:00.88
  eval_samples_per_second =    209.933
  eval_steps_per_second   =     27.088
  perplexity              =    10.1449
path='hoskinson-center/proofnet' split=test results={'eval_loss': 2.3169755935668945, 'eval_runtime': 0.886, 'eval_samples_per_second': 209.933, 'eval_steps_per_second': 27.088, 'perplexity': 10.144945422979891}
Time taken: 18.53 seconds, or 0.31 minutes, or 0.01 hours.
wandb: | 0.037 MB of 0.037 MB uploaded
wandb: Run history:
wandb:               eval/loss ▁
wandb:            eval/runtime ▁
wandb: eval/samples_per_second ▁
wandb:   eval/steps_per_second ▁
wandb:             train/epoch ▁
wandb:       train/global_step █▁
wandb: 
wandb: Run summary:
wandb:                eval/loss 2.31698
wandb:             eval/runtime 0.886
wandb:  eval/samples_per_second 209.933
wandb:    eval/steps_per_second 27.088
wandb:               total_flos 48077733888000.0
wandb:              train/epoch 0.99
wandb:        train/global_step 0
wandb:               train_loss 2.90292
wandb:            train_runtime 9.9081
wandb: train_samples_per_second 18.672
wandb:   train_steps_per_second 4.643
wandb: 
wandb: 🚀 View run morning-music-5 at: https://wandb.ai/brando/huggingface/runs/7tns0d5y
wandb: ⭐️ View project at: https://wandb.ai/brando/huggingface
wandb: Synced 7 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: /lfs/skampere1/0/brando9/wandb/run-20240410_180758-7tns0d5y/logs
(snap_cluster_setup) brando9@skampere1~/snap-cluster-setup $ python ~/snap-cluster-setup/src/train/simple_train.py 
tokenizer.pad_token='<|endoftext|>'
block_size=1024
Number of parameters: 124439808
/lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages/accelerate/accelerator.py:436: FutureWarning: Passing the following arguments to `Accelerator` is deprecated and will be removed in version 1.0 of Accelerate: dict_keys(['dispatch_batches', 'split_batches', 'even_batches', 'use_seedable_sampler']). Please pass an `accelerate.DataLoaderConfiguration` instead: 
dataloader_config = DataLoaderConfiguration(dispatch_batches=None, split_batches=False, even_batches=True, use_seedable_sampler=True)
  warnings.warn(
Detected kernel version 5.4.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
wandb: Currently logged in as: brando. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.6
wandb: Run data is saved locally in /lfs/skampere1/0/brando9/wandb/run-20240410_181121-deik32un
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run comic-bird-6
wandb: ⭐️ View project at https://wandb.ai/brando/huggingface
wandb: 🚀 View run at https://wandb.ai/brando/huggingface/runs/deik32un
{'train_runtime': 24.3208, 'train_samples_per_second': 38.033, 'train_steps_per_second': 9.457, 'train_loss': 2.0359664253566576, 'epoch': 4.95}                                                                                                                                                                                                                                                    
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 230/230 [00:18<00:00, 12.21it/s]
/lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages/accelerate/accelerator.py:436: FutureWarning: Passing the following arguments to `Accelerator` is deprecated and will be removed in version 1.0 of Accelerate: dict_keys(['dispatch_batches', 'split_batches', 'even_batches', 'use_seedable_sampler']). Please pass an `accelerate.DataLoaderConfiguration` instead: 
dataloader_config = DataLoaderConfiguration(dispatch_batches=None, split_batches=False, even_batches=True, use_seedable_sampler=True)
  warnings.warn(
Detected kernel version 5.4.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 24/24 [00:00<00:00, 28.38it/s]
Eval metrics hoskinson-center_proofnet  test Unknown_Eval_Max_Samples: metrics={'eval_loss': 1.7542803287506104, 'eval_runtime': 0.9027, 'eval_samples_per_second': 206.051, 'eval_steps_per_second': 26.587, 'perplexity': 5.779287058236344}
***** eval_hoskinson-center_proofnet__test_Unknown_Eval_Max_Samples metrics *****
  eval_loss               =     1.7543
  eval_runtime            = 0:00:00.90
  eval_samples_per_second =    206.051
  eval_steps_per_second   =     26.587
  perplexity              =     5.7793
path='hoskinson-center/proofnet' split=test results={'eval_loss': 1.7542803287506104, 'eval_runtime': 0.9027, 'eval_samples_per_second': 206.051, 'eval_steps_per_second': 26.587, 'perplexity': 5.779287058236344}
Time taken: 33.09 seconds, or 0.55 minutes, or 0.01 hours.
wandb: | 0.024 MB of 0.045 MB uploaded
wandb: Run history:
wandb:               eval/loss ▁
wandb:            eval/runtime ▁
wandb: eval/samples_per_second ▁
wandb:   eval/steps_per_second ▁
wandb:             train/epoch ▁
wandb:       train/global_step █▁
wandb: 
wandb: Run summary:
wandb:                eval/loss 1.75428
wandb:             eval/runtime 0.9027
wandb:  eval/samples_per_second 206.051
wandb:    eval/steps_per_second 26.587
wandb:               total_flos 239343501312000.0
wandb:              train/epoch 4.95
wandb:        train/global_step 0
wandb:               train_loss 2.03597
wandb:            train_runtime 24.3208
wandb: train_samples_per_second 38.033
wandb:   train_steps_per_second 9.457
wandb: 
wandb: 🚀 View run comic-bird-6 at: https://wandb.ai/brando/huggingface/runs/deik32un
wandb: ⭐️ View project at: https://wandb.ai/brando/huggingface
wandb: Synced 7 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: /lfs/skampere1/0/brando9/wandb/run-20240410_181121-deik32un/logs
```

### Background/long lived job in SNAP
First read [long lived jobs in SNAP](https://ilwiki.stanford.edu/doku.php?id=hints:long-jobs).

Now we will train small GPT2 for a longer time using krbtmux/tmux. 
First open krbtmux and run reauth and type your password:
```bash
krbtmux
reauth
```
reauth is a SNAP specific command so that any process (inside bash or a cli or tmux) has the kerberos ticket renewed so that it can it's not killed. 
Sample output:
```bash
brando9@skampere1:/afs/cs.stanford.edu/u/brando9/snap-cluster-setup$ 
```
Since this opens a fresh like (multiplexed) cli we need to re activate your bash settings (see why SNAP is annoying?!):
```bash
source $AFS/.bash_profile
# or type bash
```
Sample output:
```bash
brando9@skampere1:/afs/cs.stanford.edu/u/brando9/snap-cluster-setup$ bash

EnvironmentNameNotFound: Could not find conda environment: evals_af
You can list all discoverable environments with `conda info --envs`.


ln: failed to create symbolic link '/lfs/skampere1/0/brando9/iit-term-synthesis': File exists
(base) brando9@skampere1~ $ reauth
Password for brando9: 
Background process pid is: 1198383
```


If you notice I made a [`main_krbtmux.sh` file](https://github.com/brando90/snap-cluster-setup/blob/main/main_krbtmux.sh). 
This is so that it's easier to run long lived jobs. 
Now use it to run a long lived job training GPT2 (for say 10 epochs, edit your github's fork to change that):
```bash
bash ~/snap-cluster-setup/main_krbtmux.sh
# or source ~/snap-cluster-setup/main_krbtmux.sh
# or python ~/snap-cluster-setup/src/train/simple_train.py after you set up bash and conda and your gpu, see the main_krbtmux.sh file! that's why I made it to automate the borning things
```
Tip: you might have to set the cuda visible devices manually depending on what is free or what you need. 

Sample output:
```bash
(base) brando9@skampere1~ $ bash ~/snap-cluster-setup/main_krbtmux.sh

EnvironmentNameNotFound: Could not find conda environment: evals_af
You can list all discoverable environments with `conda info --envs`.


ln: failed to create symbolic link '/lfs/skampere1/0/brando9/iit-term-synthesis': File exists
CUDA_VISIBLE_DEVICES = 0
tokenizer.pad_token='<|endoftext|>'
block_size=1024
Number of parameters: 124439808
/lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages/accelerate/accelerator.py:436: FutureWarning: Passing the following arguments to `Accelerator` is deprecated and will be removed in version 1.0 of Accelerate: dict_keys(['dispatch_batches', 'split_batches', 'even_batches', 'use_seedable_sampler']). Please pass an `accelerate.DataLoaderConfiguration` instead: 
dataloader_config = DataLoaderConfiguration(dispatch_batches=None, split_batches=False, even_batches=True, use_seedable_sampler=True)
  warnings.warn(
Detected kernel version 5.4.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
wandb: Currently logged in as: brando. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.6
wandb: Run data is saved locally in /lfs/skampere1/0/brando9/wandb/run-20240410_192505-t5pg9q3o
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run jolly-forest-8
wandb: ⭐️ View project at https://wandb.ai/brando/huggingface
wandb: 🚀 View run at https://wandb.ai/brando/huggingface/runs/t5pg9q3o
{'loss': 4.0951, 'grad_norm': 15.34875202178955, 'learning_rate': 4.9782608695652176e-05, 'epoch': 0.02}                                                                                                                                                                                                                                                                                            
{'loss': 2.7984, 'grad_norm': 9.243730545043945, 'learning_rate': 4e-05, 'epoch': 0.99}                                                                                                                                                                                                                                                                                                             
{'loss': 2.0728, 'grad_norm': 11.679845809936523, 'learning_rate': 2.9782608695652175e-05, 'epoch': 2.0}                                                                                                                                                                                                                                                                                            
{'loss': 1.8794, 'grad_norm': 7.380716800689697, 'learning_rate': 1.9782608695652176e-05, 'epoch': 2.99}                                                                                                                                                                                                                                                                                            
{'loss': 1.7264, 'grad_norm': 10.552717208862305, 'learning_rate': 9.565217391304349e-06, 'epoch': 4.0}                                                                                                                                                                                                                                                                                             
{'loss': 1.6644, 'grad_norm': 8.1737060546875, 'learning_rate': 0.0, 'epoch': 4.95}                                                                                                                                                                                                                                                                                                                 
{'train_runtime': 24.0418, 'train_samples_per_second': 38.475, 'train_steps_per_second': 9.567, 'train_loss': 2.035966329989226, 'epoch': 4.95}                                                                                                                                                                                                                                                     
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 230/230 [00:18<00:00, 12.31it/s]
/lfs/skampere1/0/brando9/miniconda/envs/snap_cluster_setup/lib/python3.9/site-packages/accelerate/accelerator.py:436: FutureWarning: Passing the following arguments to `Accelerator` is deprecated and will be removed in version 1.0 of Accelerate: dict_keys(['dispatch_batches', 'split_batches', 'even_batches', 'use_seedable_sampler']). Please pass an `accelerate.DataLoaderConfiguration` instead: 
dataloader_config = DataLoaderConfiguration(dispatch_batches=None, split_batches=False, even_batches=True, use_seedable_sampler=True)
  warnings.warn(
Detected kernel version 5.4.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 24/24 [00:00<00:00, 27.82it/s]
Eval metrics hoskinson-center_proofnet  test Unknown_Eval_Max_Samples: metrics={'eval_loss': 1.7542803287506104, 'eval_runtime': 0.8845, 'eval_samples_per_second': 210.294, 'eval_steps_per_second': 27.135, 'perplexity': 5.779287058236344}
***** eval_hoskinson-center_proofnet__test_Unknown_Eval_Max_Samples metrics *****
  eval_loss               =     1.7543
  eval_runtime            = 0:00:00.88
  eval_samples_per_second =    210.294
  eval_steps_per_second   =     27.135
  perplexity              =     5.7793
path='hoskinson-center/proofnet' split=test results={'eval_loss': 1.7542803287506104, 'eval_runtime': 0.8845, 'eval_samples_per_second': 210.294, 'eval_steps_per_second': 27.135, 'perplexity': 5.779287058236344}
Time taken: 32.63 seconds, or 0.54 minutes, or 0.01 hours.
wandb: \ 0.023 MB of 0.048 MB uploaded
wandb: Run history:
wandb:               eval/loss ▁
wandb:            eval/runtime ▁
wandb: eval/samples_per_second ▁
wandb:   eval/steps_per_second ▁
wandb:             train/epoch ▁▂▄▅▇██
wandb:       train/global_step ▁▂▄▅▇██▁
wandb:         train/grad_norm █▃▅▁▄▂
wandb:     train/learning_rate █▇▅▄▂▁
wandb:              train/loss █▄▂▂▁▁
wandb: 
wandb: Run summary:
wandb:                eval/loss 1.75428
wandb:             eval/runtime 0.8845
wandb:  eval/samples_per_second 210.294
wandb:    eval/steps_per_second 27.135
wandb:               total_flos 239343501312000.0
wandb:              train/epoch 4.95
wandb:        train/global_step 0
wandb:          train/grad_norm 8.17371
wandb:      train/learning_rate 0.0
wandb:               train/loss 1.6644
wandb:               train_loss 2.03597
wandb:            train_runtime 24.0418
wandb: train_samples_per_second 38.475
wandb:   train_steps_per_second 9.567
wandb: 
wandb: 🚀 View run jolly-forest-8 at: https://wandb.ai/brando/huggingface/runs/t5pg9q3o
wandb: ⭐️ View project at: https://wandb.ai/brando/huggingface
wandb: Synced 6 W&B file(s), 0 media file(s), 0 artifact file(s) and 1 other file(s)
wandb: Find logs at: ./wandb/run-20240410_192505-t5pg9q3o/logs
```
Tip: todo: allows mouse scrolling `tput rmcupa` in tmux, help, can't remember why I use this command!

### Discussion of pros cons of slurm vs SNAP
Pros of SNAP's setup:
- you can run jobs for months without having to worry about the sys admins limits on `sbatch` commands
  - but no guarantees it won't fail for some random (hardware) reason!
Cons:
- very complicated e.g., afs vs lfs vs dfs and too many things you have to manually do like:
  - gpu selection, manually running background jobs with (hacked) tmux sessions, reauth shouldn't exist etc.

Pros of slurm setup:
- sys admins do all the dirty work
Cons of slurm setup:
- only one I personally know of is that it's hard to by pass the "let me run a job for X months"
  - but your labmates might get mad anyway...and ping you.
  
In either case the sys admins have control of what you can install, so SNAP's set up doesn't even provide that advantage e.g., use the `module avail` command and Google what it is and why sys admins want it like that. 

## Killing Process in SNAP (kill vsoce in SNAP)
Sometimes you might need to kill vscode processes so that vscode does not lose the kerberos authentication it needs. Some useful commands I run **very carefully** e.g., if you have a job running, it might kill it!
```bash
# kill vscode
# https://chat.openai.com/c/a114f637-cfb7-4515-afe8-6590d0ce9c78

ps -f -u brando9

pkill -f 'code-server'
pkill -f 'vscode-remote'
pkill -f code-insiders-f
pgrep -f 'code|code-insiders|vscode' | xargs -r kill


kills all my processes:
pkill -f 'brando9' || pgrep -f 'brando9' | xargs -r kill
```

## Check Disk Size
To see the disk space of the current path/dir you can do:
```bash
du -sh
```
sample output:
```bash
(base) brando9@skampere1/afs/cs.stanford.edu/u/brando9 $ du -sh .
4.6G    .
```
To find size of all files and dirs at `.` do:
```
du -sh * .[!.]*
```
Note: .[!.]*: This is a pattern that matches hidden files and directories in the current directory, excluding the special directories . and ...

Ref: handy [claude Opus 2024 april 14](https://claude.ai/chat/97ea37ad-7446-48c1-814a-0d44a713d7b4).

## Gitlfs
First if you are in SNAP, to make sure `afs` is not overwhelmed do:
```bash
git config --global lfs.storage ~/.cache/git-lfs
```
This makes sure that the large files (e.g., the image files) to be tracked by git lfs are not tracked in your github repo, where we usually store the git repo in SNAP. 
We do this since your `afs` directory is available on all nodes and it's fast so **only** the code can be there. 
But the large files might still be needed. For that the previous command puts the git lfs files in `lfs` and since we made sure `$HOME` (`~`) points to your lfs home directory path where is storage.

Now to initialize git lfs do:
```bash
git lfs install
```
This will trakc the large files in a remote directory in the remove and in the local at `~/.cache/git-lfs`.
Every file type you want to associate with Git LFS will need to be added with git lfs track. 
To track all image files with Git LFS, you can use the git lfs track command followed by the file patterns for common image file extensions. Here's an example command that tracks several popular image file formats:
```bash
git lfs track "*.jpg" "*.jpeg" "*.png" "*.gif" "*.psd" "*.tiff" "*.bmp" "*.svg" "*.eps" "*.webp"
```
It creates a `.gitattributes` file that tracks git lfs tracked files. 
If you want to then commit them you do:
```bash
git commit -m "Convert image files to Git LFS"
```
But if you did a "mistake" and had already pushed them, you can do:
```bash
git lfs migrate import --include="*.jpg,*.jpeg,*.png,*.gif,*.psd,*.tiff,*.bmp,*.svg,*.eps,*.webp"
# if it worked, then do:
git push
```
check if this fixed it with:
```bash
git lfs status
git status
```
this should show no issues with either normal code vs the git lfs tracked files.

Ref: 
  - ref: https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage 

## Undo last git commit & add (safely)
To undo the last git commit that hasn't been pushed to a remote repository, you can use the git reset command. Here's how you can do it:
```bash
git reset --soft HEAD~1
```
Explanation:
- `git reset` is the command used to undo commits.
- The `--soft` option moves the branch pointer back to the previous commit, but keeps the changes from the last commit in the staging area. 
This means that the changes from the last commit will still be present in your working directory and staged for the next commit.
-`HEAD~1` refers to the commit that is one before the current `HEAD`. This effectively undoes the last commit.
Sample output:
```bash
(base) brando9@skampere1/afs/cs.stanford.edu/u/brando9/gold-ai-olympiad $ git reset --soft HEAD~1
(base) brando9@skampere1/afs/cs.stanford.edu/u/brando9/gold-ai-olympiad $ 
```
Ref: handy claude [reference in the context of git lfs](https://claude.ai/chat/97ea37ad-7446-48c1-814a-0d44a713d7b4).

To undo last `git add .` do:
```bash
git restore --staged .
```

## VScode code workspace files
You can [put your vscode files in AFS and symlink them to all nodes](https://chat.openai.com/c/8a3ad71e-48af-456a-ac3e-1029afc184bb) e.g.,
```bash
# Set the AFS environment variable if it is not already set
export AFS="/afs/cs.stanford.edu/u/brando9"

# Move and rename the VS Code workspaces to the AFS directory, and create symbolic links in the home directory
mv "$HOME/vscode.beyond-scale-language-data-diversity.ampere1.code-workspace" "$AFS/vscode.beyond-scale-language-data-diversity.code-workspace"
ln -s "$AFS/vscode.beyond-scale-language-data-diversity.code-workspace" "$HOME/vscode.beyond-scale-language-data-diversity.code-workspace"

mv "$HOME/vscode.gold-ai-olympiad.afs_snap.code-workspace" "$AFS/vscode.gold-ai-olympiad.code-workspace"
ln -s "$AFS/vscode.gold-ai-olympiad.code-workspace" "$HOME/vscode.gold-ai-olympiad.code-workspace"

mv "$HOME/vscode.evaporate.skampere1.code-workspace" "$AFS/vscode.evaporate.code-workspace"
ln -s "$AFS/vscode.evaporate.code-workspace" "$HOME/vscode.evaporate.code-workspace"

mv "$HOME/vscode.lean4ai.skampere1.code-workspace" "$AFS/vscode.lean4ai.code-workspace"
ln -s "$AFS/vscode.lean4ai.code-workspace" "$HOME/vscode.lean4ai.code-workspace"

mv "$HOME/vscode.snap-cluster-setup.code-workspace" "$AFS/vscode.snap-cluster-setup.code-workspace"
ln -s "$AFS/vscode.snap-cluster-setup.code-workspace" "$HOME/vscode.snap-cluster-setup.code-workspace"

mv "$HOME/vscode.maf_data.creating_data_math_training.skamapere1.code-workspace" "$AFS/vscode.maf_data.creating_data_math_training.code-workspace"
ln -s "$AFS/vscode.maf_data.creating_data_math_training.code-workspace" "$HOME/vscode.maf_data.creating_data_math_training.code-workspace"

mv "$HOME/vscode.maf_data.training_af_model.skampere1.code-workspace" "$AFS/vscode.maf_data.training_af_model.code-workspace"
ln -s "$AFS/vscode.maf_data.training_af_model.code-workspace" "$HOME/vscode.maf_data.training_af_model.code-workspace"

mv "$HOME/vscode.math_evaporate.skampere1.code-workspace" "$AFS/vscode.math_evaporate.code-workspace"
ln -s "$AFS/vscode.math_evaporate.code-workspace" "$HOME/vscode.math_evaporate.code-workspace"

mv "$HOME/vscode.beyond-scale-language-data-diversity.skampere1.code-workspace" "$AFS/vscode.beyond-scale-language-data-diversity.code-workspace"
ln -s "$AFS/vscode.beyond-scale-language-data-diversity.code-workspace" "$HOME/vscode.beyond-scale-language-data-diversity.code-workspace"
```
this is because the vscode file looks as follows:
```bash
(gold_ai_olympiad) (base) brando9@ampere1:~$ cat vscode.beyond-scale-language-data-diversity.ampere1.code-workspace
{
        "folders": [
                {
                        "path": "beyond-scale-language-data-diversity"
                },
                {
                        "path": "massive-autoformalization-maf"
                },
                {
                        "path": "data/maf_data"
                },
                {
                        "path": "evals-for-autoformalization"
                },
                {
                        "path": "ultimate-anatome"
                },
                {
                        "path": "ultimate-utils"
                },
                {
                        "path": "data"
                }
        ],
        "settings": {}
```
which means it's relative to `$HOME` most likely. 

## Poetry

### Manual Installation of Poetry in SNAP
Official reference for installing manually: https://python-poetry.org/docs/#installing-manually

So that poetry's own depedencies don't get accidentally overwritten, you need to install poetry in a virtual env. 
Thus, to install Poetry manually in a virtual env using pip and the venv module with python, do: 
```bash
# check your %HOME (~) points to lfs
echo $HOME 

# If the virtual env folder doesn't exist create it (note $HOME should point to your lfs)
mkdir $HOME/.virtualenvs

# Set the python virtual env that will hold poetry
export VENV_PATH=$HOME/.virtualenvs/venv_for_poetry

# Create a virtual environment at the specified path (python3 -m uses python's way to execute modules without needing to know their location, in this case we use the venv, virtualenv, one to create a virtual env at $VENV_PATH)
python3 -m venv $VENV_PATH

# Upgrade pip and setuptools within the virtual environment
$VENV_PATH/bin/pip install -U pip setuptools

# Install poetry within the virtual environment
$VENV_PATH/bin/pip install poetry
```
Poetry will be available at `$VENV_PATH/bin/poetry`, but to have the `poetry` command available without using the full path, add the virtual env's path to you `$PATH` env:
```bash
# WARNING: put this export command before conda does the same thing, so that this path is not used by accident over your conda's python env
export PATH="$VENV_PATH/bin:$PATH"
```
Ideally (especially if you are using conda), the following commands have to be placed carefully in your `.bashrc` file:
```bash
# create env for the virtual env that will have the poetry command (note: assumes `mkdir $HOME/.virtualenvs` has been ran)
export VENV_PATH=$HOME/.virtualenvs/venv_for_poetry
# careful running the export bellow, it will put it in front of your conda path if you are using conda and you won't use your conda env's python
export PATH="$VENV_PATH/bin:$PATH"
```
In particular, you need to put it before your export for your conda env ([see our `.bashrc`](https://github.com/brando90/snap-cluster-setup/blob/main/.bashrc) for an example)
In particular note how `export PATH="$VENV_PATH/bin:$PATH"` is before any of the following commands:
```bash
# dummy .bashrc file

# exports to make the poetry command available goes first
export VENV_PATH=$HOME/.virtualenvs/venv_for_poetry
export PATH="$VENV_PATH/bin:$PATH"

# export to make conda work (assuming that's what you want to use)
export PATH="$HOME/miniconda/bin:$PATH"
source $HOME/miniconda/bin/activate
conda activate snap_cluster_setup
```

To uninstall Poetry, simply delete the entire `$VENV_PATH` directory:
```bash
# uninstall Poetry
rm -rf $VENV_PATH
```

ref: [venv](https://docs.python.org/3/library/venv.html)
ref: SNAP cluster tutorial for venv https://ilwiki.stanford.edu/doku.php?id=hints:virtualenv
ref: chat that got us here: https://chat.openai.com/c/9f4f25f6-fbce-445c-8955-ce0b9bc5ab6f

### Poetry depedencies
TODO

ref: https://chat.openai.com/c/e01336a7-6f67-4cd2-b6cd-09b8ee8aef5a

### Poetry development/editable install of your Project
TODO

ref: https://chat.openai.com/c/e01336a7-6f67-4cd2-b6cd-09b8ee8aef5a

### cheat sheet

poetry build: Packages the project into distributable formats (like .whl and .tar.gz) based on the configurations set in pyproject.toml.
poetry install: Installs the project and its dependencies into the virtual environment, creating the environment if it doesn't exist, in editable mode.
poetry shell: Spawns a new shell with the project's virtual environment activated, making it the primary Python environment.
poetry env use: Specifies which Python interpreter to use for the project's virtual environment, creating a new environment if the specified interpreter doesn't match any existing one.
poetry env list: Lists all virtual environments associated with the current project, indicating which is currently activated.
poetry show: lists and provides detailed information about each package installed in the current project's Poetry-managed virtual environment, including version numbers and descriptions.
poetry show --tree: displays a hierarchical view of all packages installed in the project's environment, showing dependencies in a tree-like structure to illustrate their relationships

# Git Submodules

If you have not added the submodules to your `.gitmodules` files, you can do it as follows:
```bash
# -- add the following modules to your .gitsubmodule file
git submodule add -f -b hdb --name meta-dataset git@github.com:brando90/meta-dataset.git meta-dataset/
```
Then to initialize the git submodules so that git can keep track of the submodules being used do:
```bash
# - initialize the git submodules by preparing the git repository, but it does not clone or fetch them, just init's git's internal configs
git submodule init
```
Then to clone, fetch & update the submodules code (and also initilize anything you might have forgotten that is specificed in the `.gitmodules` file):
```bash
# - initialize the git submodules so that git can track them and then the update clone/fetches & updates the submodules
git submodule update --init
```

# Lean in SNAP
You will need a small tool called `elan` will handle updating Lean according to the needs of your current project. 
Install it with:
```bash
# this special version is needed in SNAP because of $HOME points to lfs and elan detects that it seems
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y
```

Sample output:
```bash
(base) brando9@ampere1~/PyPantograph $ curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y
info: downloading installer
warning: $HOME differs from euid-obtained home directory: you may be using sudo
info: syncing channel updates for 'stable'
info: latest update on stable, lean version v4.7.0
info: downloading component 'lean'
info: installing component 'lean'
info: default toolchain set to 'stable'

  stable installed - Lean (version 4.7.0, x86_64-unknown-linux-gnu, commit 6fce8f7d5cd1, Release)
```

Let's sanity check that the hidden that Lean's `elan` tool is where we expect it to be:
```bash
(base) brando9@ampere1~/PyPantograph $ ls $HOME/.elan
bin  env  settings.toml  tmp  toolchains  update-hashes
```
The previous curl install will also try to put put the `$HOME/.elan` hidden path in your `PATH` env variable, so that the `elan` becomes available by creating a `.profile` with the following contents:
```bash
(base) brando9@ampere1~/PyPantograph $ cat $HOME/.profile

export PATH="$HOME/.elan/bin:$PATH"
```
However, you will need to put the above in your `.bashrc` file (e.g., at the end) if it's not already there. 
Note: the default `.bashrc` I provide should now already have it. 

Then you can check if it worked by installing [PyPentograph](https://github.com/lenianiva/PyPantograph).

ref: https://leanprover-community.github.io/install/linux.html