# Fine-tuning protein language models

Introduction to protein language models (PLM) using ESM-2 ([Lin et al., 2023](https://doi.org/10.1126/science.ade2574)):

[1_plm-embeddings.ipynb](1_plm-embeddings.ipynb):
* Predict masked residues on an example from ([Cheng et al., 2024](https://doi.org/10.1126/science.adg7492))
* Explore how PLM embeddings from different layers correlate with different aspects of protein structure ([Vig et al., 2020](https://doi.org/10.48550/arXiv.2006.15222))

[2_plm-fine-tuning.ipynb](2_plm-fine-tuning.ipynb):
* Fine-tune ESM-2 to predict protein localisation from sequence, using the setup from ([Moreno et al., 2024](https://doi.org/10.1093/bioinformatics/btae677)).

## Further reading
* [Various materials on transformers (Hacker News post)](https://news.ycombinator.com/item?id=35712334)
* [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/en/chapter1/1)
* Reviews on biological applications: [Bepler et al., 2021](https://doi.org/10.1016/j.cels.2021.05.017), [Ruffolo et al., 2024](https://doi.org/10.1038/s41587-024-02123-4)
