from transformers import pipeline

classifier = pipeline('text-classification', model="sentiment_roberta_model", tokenizer="sentiment_roberta_model")

def infer_feeling(text):
  return classifier(text)
