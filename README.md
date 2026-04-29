This is an AI project with the sole purpose of using a RAG system combined with FastAPI, which allows users to upload txt files and then ask questions based on the content of said files. This is done via semantic search and vector embeddings. For example, using the txt file uploaded here, random.txt, and then asking the question, "What animals are mentioned?" It will pull up that cats and dogs are mentioned. 

STEPS TO MAKE IT WORK:


1) Download the project
2) Open the project in VS Code.
3) Open a terminal inside the project and run this: pip install fastapi uvicorn chromadb sentence-transformers
4) Then start the server with this command: uvicorn app:app --reload
5) Open the API in the browser and go to: http://127.0.0.1:8000/docs
6) Using POST, upload the random.txt file and then execute
7) Then click GET and ask the question ("What animals are mentioned?") and then execute.
8) The output will come out something along these lines: "answer": "According to the given context, the following animals are mentioned: \n\n* Cat\n* Dogs",



