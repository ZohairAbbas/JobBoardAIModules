# DigitalHire Job Board AI Modules

This repo contains AI Features for DigitalHire's Job Board. **It is being made for testing purposes only**

## Spell Checker

It contains a simple Python script and doesn't need any dependencies.

- data-corpus.txt: Word corpus for Spell Checker containing all existing Job Ads.
- jd.txt: Test file, *make changes here to test Spell Checker script.*
- spell-correct.py: Python script for Spell Checker.
- spell-testset1.txt: Additional file for unit tests.


### Usage:


```python
python3 spell-correct.py
```

```
word:  telented corrected_word:  talented
word:  stuning corrected_word:  stunning
word:  seamles corrected_word:  seamless
```

## Grammar Checker

Grammar Checker uses Gramformer library which is a pre-trained ML model and uses Pytorch transformers for detecting grammatical errors.

- jd.txt: Test file, *make changes here to test Grammar Checker.*
- requirements.txt: Contains all the dependencies required for this library.
- test.py: Python script for Grammar Checker.

### Usage:

- Create a new conda environment
```bash
conda create -n gramformer
```
- Activate gramformer environment
```bash
conda activate gramformer
```
- Install all dependencies
```bash
pip3 install -r requirements.txt
```
-Once everything is setup, run the test.py file for Grammar Checking
```bash
python3 test.py
```
```bash
[Gramformer] Grammar error correct/highlight model loaded..
----------------------------------------------------------------------------------------------------
[Incorrect]   Proficient in use Adobe XD and Figma to design user interfaces.
[Correction]  Proficient in using Adobe XD and Figma to design user interfaces.
----------------------------------------------------------------------------------------------------
```

## Foul Language Detection

DistilBERT is a transformer model that performs sentiment analysis. 
The model is fine-tuned on Reddit posts for classifying text as SFW and NSFW. 

The model is a fine-tuned version of DistilBERT.

It was fine-tuned on 19604 Reddit posts pulled from the Comprehensive Abusiveness Detection Dataset.

- foul-checker.py: Python script for Foul Language Detection

### Usage:

```bash
python3 foul-checker.py
```
```
"This job is for people from EU and US. We don't want Asians, they suck at Maths lol."
[{'label': 'NSFW', 'score': 0.9757649302482605}]
```
