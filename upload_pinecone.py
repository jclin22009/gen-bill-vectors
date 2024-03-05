from pinecone import Pinecone
import json
from tqdm import tqdm

pc = Pinecone(api_key="e6bf0792-bec2-4711-9d4c-f4a202db8f12")
index = pc.Index("bills-semantic-search")

# open bill_embeddings.jsons file
# the schema of this file is as follows (on consecutive lines):
# {"billId": ____, "title": _____, "embedding": _____}
# {"billId": ____, "title": _____, "embedding": _____}
# so it's basically a ton of jsons, one per line

with open("bill_embeddings.jsons", "r") as f:
    for line in tqdm(f, desc="Uploading bills"):
        bill = json.loads(line)
        index.upsert(
            vectors=[
                {
                    "id": bill["billId"],
                    "values": bill["embedding"],
                    "metadata": {"title": bill["title"]},
                }
            ]
        )
