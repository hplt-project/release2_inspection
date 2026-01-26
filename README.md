# release2_inspection
This repository contains data, code and documentation related to manual inspection of [HPLT v2](https://hplt-project.org/datasets/v2.0).  

## Purpose of inspection
We want to get a rough idea about the actual content of the cleaned verion of the 2nd data release. More specifically, for a subset that should correspond to some language L we want to estimate:
1) the proportion of texts that are in fact not in the language L,
2) the proportion of texts that can be considered undesirable because they are unnatural,
3) the proportion of texts that can be considered undesirable porn texts.

Additionally, we want to compare these characteristics for the older and the newer crawls, and also for the IA and CC crawls.


PROMPSIT ALTERNATIVE INSPECTION EFFORT ([20 docs per lang in HPLT v2](https://drive.google.com/file/d/1GNPIU9LoO8ewoE6uWdSGwU0zZP3BY0p7/view?usp=sharing)): [results](https://docs.google.com/spreadsheets/d/1f8QVm5L3nKcjlLVJipr2wN3Chuc4n5iEK6YWNN1uclU/edit?usp=sharing)


## Data for round 1 of inspection: 
* samples stratified by language and crawl group,
*  4 groups (cc/ia old/new), NB! these 4 groups do not cover the full dataset, so generalization of conclusions based on the annotated subset to the full dataset may be incorrect!
*  first 5 batches per language,
*  200 examples per batch,
*  500/500 characters from the beginning of the fist/second half of each text.

## Inspection
Inspection is performed by volunteers who were mostly the members of the HPLT project. Volunteers inspect languages 
which they are native or fluent speakers of following the [guidelines](GUIDELINES.md).


## Results
Data:
- [the original sample](per_lang_group_1K)
- [the sample converted to a format appropriate for annotation, partially annotated](annot_round1)
- [observations provided by the annotators](observations/README.md)
- [all annotations](annotations.tsv)
- [all annotated documents in one file along with annotations](annotated.jsonl.zst)
- 
Analysis:
- [summary table](results_per_lang.tsv)
- [detailed analysis](Proportions.ipynb)


# Acknowledgements

This project has received funding from the European Union’s Horizon Europe research and innovation programme under grant agreement No 101070350 and from UK Research and Innovation (UKRI) under the UK government’s Horizon Europe funding guarantee [grant number 10052546]
