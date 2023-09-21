"""Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html

Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php
"""

################ Spelling Corrector 

import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('data_corpus.txt').read()))
# print(len(WORDS))
# print(sum(WORDS.values()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def getCorrectWord(word): 
    "Most probable spelling correction for word."
    return max(getAllPossibleSpellingCombinations(word), key=P)

def getAllPossibleSpellingCombinations(word): 
    "Generate possible spelling corrections for word."
    return (isKnownWord([word]) or isKnownWord(getAllCombinationsBySingleEditDistance(word)) or isKnownWord(getAllCombinationsByTwoEditDistance(word)) or [word])

def isKnownWord(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def getAllCombinationsBySingleEditDistance(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    # print(set(deletes + transposes + replaces + inserts))
    return set(deletes + transposes + replaces + inserts)

def getAllCombinationsByTwoEditDistance(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in getAllCombinationsBySingleEditDistance(word) for e2 in getAllCombinationsBySingleEditDistance(e1))

################ Test Code 

def unit_tests():
    assert getCorrectWord('speling') == 'spelling'              # insert
    assert getCorrectWord('korrectud') == 'corrected'           # replace 2
    assert getCorrectWord('bycycle') == 'bicycle'               # replace
    assert getCorrectWord('inconvient') == 'inconvenient'       # insert 2
    assert getCorrectWord('arrainged') == 'arranged'            # delete
    assert getCorrectWord('peotry') =='poetry'                  # transpose
    assert getCorrectWord('peotryy') =='poetry'                 # transpose + delete
    assert getCorrectWord('word') == 'word'                     # known
    assert getCorrectWord('quintessential') == 'quintessential' # unknown
    assert words('This is a TEST.') == ['this', 'is', 'a', 'test']
    assert Counter(words('This is a test. 123; A TEST this is.')) == (
           Counter({'123': 1, 'a': 2, 'is': 2, 'test': 2, 'this': 2}))
    assert len(WORDS) == 32198                              
    assert sum(WORDS.values()) == 1115585
    assert WORDS.most_common(10) == [
     ('the', 79809),
     ('of', 40024),
     ('and', 38312),
     ('to', 28765),
     ('in', 22023),
     ('a', 21124),
     ('that', 12512),
     ('he', 12401),
     ('was', 11410),
     ('it', 10681)]
    assert WORDS['the'] == 79809
    assert P('quintessential') == 0
    assert 0.07 < P('the') < 0.08
    return 'unit_tests pass'

def spelltest(tests, verbose=False):
    "Run correction(wrong) on all (right, wrong) pairs; report results."
    import time
    start = time.process_time()
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = getCorrectWord(wrong)
        good += (w == right)
        if w != right:
            unknown += (right not in WORDS)
            if verbose:
                print('correction({}) => {} ({}); expected {} ({})'
                      .format(wrong, w, WORDS[w], right, WORDS[right]))
    dt = time.process_time() - start
    print('{:.0%} of {} correct ({:.0%} unknown) at {:.0f} words per second '
          .format(good / n, n, unknown / n, n / dt))
    
def Testset(lines):
    "Parse 'right: wrong1 wrong2' lines into [('right', 'wrong1'), ('right', 'wrong2')] pairs."
    return [(right, wrong)
            for (right, wrongs) in (line.split(':') for line in lines)
            for wrong in wrongs.split()]

if __name__ == '__main__':
    # Read the input text from 'jd.txt'
    with open('jd.txt', 'r') as file:
        text = file.read()

    # Split the text into lines
    lines = text.splitlines()

    # Initialize a dictionary to store corrected sentences
    corrected_sentences = {}

    # Iterate through each line of text
    for line_number, line in enumerate(lines, start=1):
        words = re.findall(r'\w+', line)
        
        # Initialize variables to store corrected line and a flag for spelling error
        corrected_line = []
        has_spelling_error = False
        
        # Check for spelling errors in each word
        for word in words:
                # Check if the word is misspelled
            word = word.strip().lower()
            corrected_word = getCorrectWord(word)
            if corrected_word.strip().lower() != word:
                print("word: ", word, "corrected_word: ", corrected_word)
#                 corrected_line.append(corrected_word)
#                 has_spelling_error = True
#             else:
#                 corrected_line.append(word)
#         else:
#             corrected_line.append(word)
    
#     # Join the tokens back into a corrected line
#     corrected_line = ' '.join(corrected_line)
    
#     # If the line has a spelling error, store it
#     if has_spelling_error:
#         corrected_sentences[line_number] = {
#             "lineNo": line_number,
#             "problemPhrase": line.strip(),
#             "solutionAdvice": corrected_line.strip(),
#             "stepTaken": "Replace word"
#         }

    # # Create the JSON response
    # response = {
    #     "status": "spelling_errors_detected",
    #     "spellingErrorInstances": list(corrected_sentences.values())
    # }

    # print(response)
