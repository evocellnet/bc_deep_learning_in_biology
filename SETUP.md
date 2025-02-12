# Getting started (on MOL)

We use
[(bio)conda](https://doi.org/10.1038/s41592-018-0046-7)
throughout the course. Install from Terminal
[as described here](https://docs.anaconda.com/free/anaconda/install/linux/).
The default shell may be set to tcsh (not bash); therefore may need to switch to bash manually. 
Copy the following commands and run them in a terminal window. 
```
bash
conda init --reverse --all
rm -rf ~/anaconda3
exit
```

```
bash
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
bash Anaconda3-2024.10-1-Linux-x86_64.sh -b
exit
```

```
bash
git clone https://github.com/evocellnet/bc_deep_learning_in_biology/
cd bc_deep_learning_in_biology
conda env update --prune --file=block-course.yaml 
```

For some commands below, do not copy the preceeding `$` or `>>>` signs. They simply indicate commands compared to the output. 
Check the CUDA Toolkit version installed (11.7):
```console
$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Wed_Jun__8_16:49:14_PDT_2022
Cuda compilation tools, release 11.7, V11.7.99
Build cuda_11.7.r11.7/compiler.31442593_0
```

Install the latest versions of PyTorch and associated packages still compatible with the CUDA version.
The example below was obtained from the list of
[previous versions](https://pytorch.org/get-started/previous-versions/)
on the CUDA web site, and searching for `11.7`.
Run this command:
```
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
```

Continue by installing
[Pytorch Lightning](https://lightning.ai/docs/pytorch/stable/)
and
[TensorBoard](https://www.tensorflow.org/tensorboard/get_started) (lab 1-3) with this command:
```
conda install lightning tensorboard -c conda-forge
```

And the Transformers library form Hugging Face (lab 4):
```
conda install biopython transformers datasets evaluate -c conda-forge
```
After installing conda, close and reopen the terminal window, to make the installation available. 

Quick check that the GPU is available from python:
```console
$ python
Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch.cuda
>>> torch.cuda.is_available()
True
>>> exit()
```

Install git & download the course repository (see
[a blog post](https://medium.com/@protobioengineering/github-for-biologists-407fab350083)
and
[a paper](https://doi.org/10.1371/journal.pcbi.1004947)
on using git):
```
conda install git
git clone https://github.com/evocellnet/bc_deep_learning_in_biology/
```

Go to the repository, and launch jupyter lab:
```
cd ~/bc_deep_learning/
jupyter lab
```

At the end of the course, please
[clean up anaconda](https://docs.anaconda.com/free/anaconda/install/uninstall/),
and remove the course repository/other files from the machine you've been using.
