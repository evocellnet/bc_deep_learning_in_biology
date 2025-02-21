# Fine-tuning protein language models

Introduction to protein language models (PLM) using ESM-2 ([Lin et al., 2023](https://doi.org/10.1126/science.ade2574)):

[1_plm-embeddings.ipynb](1_plm-embeddings.ipynb):
* Predict masked residues on an example from ([Cheng et al., 2024](https://doi.org/10.1126/science.adg7492))
* Explore how PLM embeddings from different layers correlate with different aspects of protein structure ([Vig et al., 2020](https://doi.org/10.48550/arXiv.2006.15222))

[2_plm-fine-tuning.ipynb](2_plm-fine-tuning.ipynb):
* Fine-tune ESM-2 to predict protein localisation from sequence, using the setup from ([Moreno et al., 2024](https://doi.org/10.1093/bioinformatics/btae677))

## Further reading
* [Various materials on transformers (Hacker News post)](https://news.ycombinator.com/item?id=35712334)
* Practical examples of fine-tuning ESM-2: [predicting PTM sites](https://huggingface.co/blog/AmelieSchreiber/esm2-ptm), [designing peptide binders](https://huggingface.co/blog/AmelieSchreiber/esm-interact), [predicting the effects of individual mutations](https://huggingface.co/blog/AmelieSchreiber/mutation-scoring)
* [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/) has practical examples for using the libraries: 
[datasets](https://huggingface.co/docs/datasets/index),
[evaluate](https://huggingface.co/docs/evaluate/index),
[transformers](https://huggingface.co/docs/transformers/index)
* Reviews on biological applications: [Bepler et al., 2021](https://doi.org/10.1016/j.cels.2021.05.017), [Ruffolo et al., 2024](https://doi.org/10.1038/s41587-024-02123-4)
* [CS25: Transformers United V4](https://web.stanford.edu/class/cs25/) goes deeper into the latest architecture/methods