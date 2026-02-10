# Project: Protein Stability Prediction

In this project, you will predict protein stability changes upon point mutations. 

We use accumulated data from experimental databases, specifically the Megascale dataset. A current [paper](https://www.pnas.org/doi/10.1073/pnas.2314853121) has preprocessed the dataset and created homology-reduced data splits. We reuse these splits. To get started, download the data folder from [here](https://polybox.ethz.ch/index.php/s/txvcb5jKy1A0TbY) and unzip it.

## Data Overview

The dataset includes measurements of changes in Gibbs free energy ($\Delta \Delta G$). This is the value you need to predict for a given protein with a point mutation.

The data folder you download contains the following files:

- **mega_train.csv** / **mega_val.csv**: CSV files with metadata and labels for train/validation splits
  - Contains columns like: name, mutation info, wild-type sequence, mutated sequence, ΔΔG values
  - **mega_test.csv** for the final testing of the models will be released towards the end of the project.
- **embeddings**: pre-computed protein embeddings, in case you decide to use them as input (see below).

## Code Strcuture and Input Options
We provide some Jupyter notebooks that you can start with. They already implement dataloading and some simple visualization.

You can build your model using:
1. **Sequence-based**: Raw amino acid sequences - see `stability_prediction_from_sequence.ipynb`
2. **ESM Embedding-based**: Precomputed embeddings from ESM - see `stability_prediction_from_embeddings.ipynb`
3. **Own ideas**: You can come up with and try any input or other type of model

If you want to compute your own embeddings, e.g. from other layers or larger ESM models, feel free to do so. You can adjust the code in `stability_prediction_more_embeddings.ipynb`. 

## Benchmark Baseline

We provide a BLOSUM-based baseline model in `stability_prediction_BLOSUM_baseline.ipynb`. This notebook computes a simple benchmark score based on BLOSUM substitution matrices. We recommend you compare your deep learning models against this baseline to evaluate whether your approach provides an improvement over classical methods.

## Getting Started

The structure provided in the notebooks can be used as a starting point for your project. Start with exploring the data and thinking about modeling choices for your neural network. Edit the cells and add more code to create your final model for protein stability prediction.


Good luck with your project!
