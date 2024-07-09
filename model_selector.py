import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, BertForSequenceClassification, BertTokenizer, RobertaForSequenceClassification, RobertaTokenizer, DistilBertForSequenceClassification, DistilBertTokenizer
from fastapi import FastAPI, Query
import json
import groq

app = FastAPI()

# Load configuration
with open("config.json") as f:
    config = json.load(f)

# Load models
models = {}
tokenizers = {}

for model_config in config["models"]:
    name = model_config["name"]
    path = model_config["path"]
    if "gpt2" in name:
        models[name] = GPT2LMHeadModel.from_pretrained(path)
        tokenizers[name] = GPT2Tokenizer.from_pretrained(path)
    elif "bert" in name:
        models[name] = BertForSequenceClassification.from_pretrained(path)
        tokenizers[name] = BertTokenizer.from_pretrained(path)
    elif "roberta" in name:
        models[name] = RobertaForSequenceClassification.from_pretrained(path)
        tokenizers[name] = RobertaTokenizer.from_pretrained(path)
    elif "distilbert" in name:
        models[name] = DistilBertForSequenceClassification.from_pretrained(path)
        tokenizers[name] = DistilBertTokenizer.from_pretrained(path)

@app.get("/generate/")
def generate_text(model: str = Query(..., description="The model to use"), prompt: str = Query(..., description="The input prompt for generating text")):
    tokenizer = tokenizers[model]
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    # Utilize Groq API for optimized performance
    with groq.set_key("YOUR_GROQ_API_KEY"):
        output = models[model].generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"generated_text": generated_text}
