#!pip install flask transformers torch

from flask import Flask, request, jsonify
from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F

# Initialize the Flask app
app = Flask(__name__)

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Cosine similarity function
def cosine_similarity(emb1, emb2):
    return F.cosine_similarity(emb1, emb2).item()

# API endpoint to compute cosine similarity between two texts
@app.route("/similarity", methods=["POST"])
def get_similarity():
    try:
        # Get the JSON request data
        data = request.get_json()
        text1 = data['text1']
        text2 = data['text2']

        # Tokenize and encode input texts
        inputs1 = tokenizer(text1, return_tensors='pt', truncation=True, padding=True, max_length=512)
        inputs2 = tokenizer(text2, return_tensors='pt', truncation=True, padding=True, max_length=512)

        # Get the embeddings from BERT
        with torch.no_grad():
            outputs1 = model(**inputs1)
            outputs2 = model(**inputs2)

        # Get the CLS token representation
        emb1 = outputs1.last_hidden_state[:, 0, :]
        emb2 = outputs2.last_hidden_state[:, 0, :]

        # Calculate cosine similarity
        similarity_score = cosine_similarity(emb1, emb2)

        return jsonify({"similarity_score": similarity_score})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Root endpoint for health check
@app.route("/")
def index():
    return jsonify({"message": "BERT Similarity API is up and running!"})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
