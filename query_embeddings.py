import supabase
import vecs
from dotenv import load_dotenv
from openai import OpenAI
import os


# LOAD ENVIRONMENT VARIABLES
load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


# CREATE DB CONNECTION
DB_CONNECTION = "postgresql://postgres.tvmjxkwjlhnnbkihjjdj:esfizNnQrTF3wanP@aws-0-us-west-1.pooler.supabase.com:5432/postgres"
vx = vecs.Client(DB_CONNECTION)
sentences = vx.get_or_create_collection(name="uwu", dimension=1536)
print(sentences)

# vx.list_collections()
# docs = vx.get_collection("bills")


# def gen_embedding(text):
#     response = client.embeddings.create(
#         input=text,
#         model="text-embedding-3-large",
#     )
#     return response.data[0].embedding

# def query_db(text):
#     query_embedding = gen_embedding(text)
#     results = docs.query(
#         data=query_embedding,
#         limit=5,
#         include_value=True
#     )
#     return results

# # run the query
# query = "Gun control"
# results = query_db(query)
# print(results)