from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
import os
from database import run_db


# def qa_model(folder_path):
folder_path = 'pdf_dataset/' 
# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):  # Check if the file is a PDF
        pdf_path = os.path.join(folder_path, filename)
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        model_name = "text-davinci-003"
        embeddings = OpenAIEmbeddings(openai_api_key='....................')
        docsearch = Chroma.from_documents(texts, embeddings)

        qa = RetrievalQA.from_chain_type(llm=OpenAI(model_name = model_name,openai_api_key='..........'),chain_type="stuff", retriever=docsearch.as_retriever())
        query = "What is invoice number,tax id and client name and gross worth . Return the result only as JSON with key as InvoiceNo,TaxId,ClientName and GrossWorth. Skip any fields that are unavailable"
        res = qa.run(query)
        print(res)
        res = run_db(res)
 