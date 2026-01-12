import os
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
def get_embeddings(chunks):
    embeddings_list = []
    try:
        for chunk in chunks:
            emb = model.encode(chunk)
            embeddings_list.append(emb)
        return embeddings_list
    except Exception as e:
        print(e)
        return None

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""] 
)

base_dir = Path.cwd()
doc = base_dir / 'data' / 'knowledge.md'

with open(doc, "r") as file:
    full_text = file.read()   

chunks = text_splitter.split_text(full_text) 
all_embeddings = get_embeddings(chunks)
print(all_embeddings) 

