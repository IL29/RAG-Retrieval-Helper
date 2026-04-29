from sentence_transformers import SentenceTransformer
import chromadb


model = SentenceTransformer("all-MiniLM-L6-v2")


client = chromadb.Client()
collection = client.get_or_create_collection("docs")



def add_document(doc_id, text):
    chunks = text.split("\n")  
    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            continue

        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[f"{doc_id}_{i}"],  
            embeddings=[embedding],
            documents=[chunk]
        )



def search(query, k=3):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results["documents"][0]