from flask import Flask, request, jsonify
import numpy as np
import json
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from openai import OpenAI
import os

app = Flask(__name__)

# load openAI API key
load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def gen_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-large",
    )
    return np.array(response.data[0].embedding)

def load_embeddings_from_file():
    with open("bill_embeddings.jsons", "r") as file:
        bill_embeddings = []
        for line in file:
            json_object = json.loads(line)
            bill_embeddings.append(
                (
                    json_object["billId"],
                    json_object["title"],
                    np.array(json_object["embedding"]),
                )
            )
        return bill_embeddings

bill_embeddings = load_embeddings_from_file()

def cosine_sim(embedding1, embedding2):
    return cosine_similarity([embedding1], [embedding2])[0][0]

def search_bills(query, bill_embeddings):
    query_embedding = gen_embedding(query)
    similarities = [
        (bill_id, title, cosine_sim(query_embedding, embedding))
        for bill_id, title, embedding in bill_embeddings
    ]
    similarities.sort(key=lambda x: x[2], reverse=True)
    return similarities[:5]

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    results = search_bills(query, bill_embeddings)
    return jsonify([
        {'bill_id': bill_id, 'title': title, 'similarity': similarity}
        for bill_id, title, similarity in results
    ])

if __name__ == '__main__':
    app.run(debug=True)
