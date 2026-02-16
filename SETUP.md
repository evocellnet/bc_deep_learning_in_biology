# Getting started (on MOL)

We use
[(bio)conda](https://doi.org/10.1038/s41592-018-0046-7)
throughout the course.
Use the commands below to remove the existing conda installation if needed.
The default shell may be set to tcsh (not bash); therefore may need to switch to bash manually. 
Copy the following commands and run them in a terminal window. 
```
bash
conda init --reverse --all
rm -rf ~/anaconda3 ~/bc_deep_learning_in_biology ~/miniconda3
exit
```

Next, install
[uv](https://docs.astral.sh/uv/),
download the course repository using git (see
[a blog post](https://medium.com/@protobioengineering/github-for-biologists-407fab350083)
&
[a paper](https://doi.org/10.1371/journal.pcbi.1004947)
)
and the deep learning libraries used throughout the course such as
[Pytorch Lightning](https://lightning.ai/docs/pytorch/stable/),
[TensorBoard](https://www.tensorflow.org/tensorboard/get_started):
```
bash
git clone https://github.com/evocellnet/bc_deep_learning_in_biology/
cd ~/bc_deep_learning_in_biology/
pip install uv
uv sync
exit
```

Finally launch jupyter lab:
```
bash
cd ~/bc_deep_learning_in_biology/
uv run jupyter lab
```

At the end of the course, please remove the course repository/other files from the machine you've been using.
```
bash
rm -rf ~/bc_deep_learning_in_biology/
exit
```
