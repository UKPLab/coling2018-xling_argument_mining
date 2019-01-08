# Code

## Direct Transfer model

We provide a YAML file for specifying a character-level bidirectional LSTM for token level sequence tagging. The underlying framework can be obtained from [here](https://github.com/UKPLab/thesis2018-tk_mtl_sequence_tagging).

In the YAML file, replace the following:

* paths for the train,dev,test file should point to your train,dev,test splits (in CONLL format)
* paths to the (bilingual) embedding file

We do not provide the embedding file. It is easy to generate a bilingual embedding file using e.g. Europarl data. Alternatively, you can also get good bilingual word embedding files for EN-DE from [here](https://github.com/UKPLab/arxiv2018-xling-sentence-embeddings). This also contains EN-FR embeddings. In the embedding files, you may wish to flag each word with its language, e.g., by appending _de or _en to each word.

Feel free to adapt the hyperparameters in the YAML file according to your taste (e.g., size of hidden states, etc.)

## Annotation projection

For annotation projection, we provide the algorithm that projects annotation spans from a source to the target language.
Once the target data is annotated using the projection algorithm, you can use the same model as for direct transfer to train a target language model. 
