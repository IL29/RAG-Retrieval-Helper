import os
from fastapi import FastAPI, UploadFile
import boto3
from rag import add_document, search

app = FastAPI()

s3 = boto3.client("s3")
BUCKET = "project-genai-bucket"


@app.post("/upload")
async def upload(file: UploadFile):
    content = await file.read()
    text = content.decode()

    s3.put_object(
        Bucket=BUCKET,
        Key=file.filename,
        Body=content
    )

    add_document(file.filename, text)

    return {"message": "uploaded + indexed"}


@app.get("/ask")
def ask(filename: str, question: str):

    context_chunks = search(question, k=3)
    context = "\n".join(context_chunks)

    prompt = f"""
    Answer ONLY using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    # NOTE: Ollama works locally only
    answer_text = f"(Demo mode)\n\n{context}"

    return {
        "answer": answer_text,
        "sources": context_chunks
    }