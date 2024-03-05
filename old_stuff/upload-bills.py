"""
In this file, I will upload the generated embeddings of a bill to a vector database. The
embeddings have been calculated in `gen_embeddings.ipynb` and stored into `bill_embeddings.jsons`.
The `jsons` format is as follows. It's essentially a list of json objects.
```
{'bill_id': 'title', 'embedding': [0.1, 0.2, 0.3, ...]}
{'bill_id': 'title', 'embedding': [0.1, 0.2, 0.3, ...]}
```

The vector database was created like so:
create table bills (
  id serial primary key,
  title text not null,
  body text not null,
  embedding vector(384)
);
"""
import json
import supabase
from tqdm import tqdm
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

with open('bill_embeddings.jsons', 'r') as f:
    lines = f.readlines()
    for line in tqdm(lines):
        bill = json.loads(line)
        # upload to vector database
        supabase.table('bills').insert({
            'bill_id': bill['billId'],
            'title': bill['title'],
            'embedding': bill['embedding']
        }).execute()

