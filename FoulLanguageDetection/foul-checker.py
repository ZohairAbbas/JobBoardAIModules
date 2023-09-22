from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="michellejieli/inappropriate_text_classifier")
response = classifier("This job is for people from EU and US. We don't want Asians, they suck at Maths lol.")
print(response)