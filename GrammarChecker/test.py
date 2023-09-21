
from gramformer import Gramformer
import torch

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1212)


gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector

# Read the input text from 'jd.txt'
with open('jd.txt', 'r') as file:
    text = file.read()

# Split the text into lines
lines = text.splitlines()
 
print("-" *100)
for line in lines:
    if len(line)>0:
      corrected_sentences = gf.correct(line, max_candidates=1)
      for corrected_sentence in corrected_sentences:
        if line!=corrected_sentence:
          print("\n[Correction] ",corrected_sentence)
          print("-" *100)