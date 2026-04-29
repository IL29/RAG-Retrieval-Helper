This is an AI project combining AWS services such as Amazon S3 with an AI RAG system. The purpose is to allow users to upload txt files and then ask questions related
to the content of the file. 

The sequence of events goes like this:

The user uploads a txt file, the file is stored in S3, and then that file is indexed into the vector database. What's retrieved after is only the information most relevant via semantic similarity. 
