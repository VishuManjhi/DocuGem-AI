from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

import tempfile
import os

def get_pdf_text(uploaded_file):
    from PyPDF2 import PdfReader

    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return [Document(page_content=text)]


def create_vectorstore_from_texts(documents, api_key, file_name="default.pdf"):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )

    persist_dir = os.path.join("vectorstores", file_name.replace(".pdf", ""))
    vectorstore = Chroma.from_documents(texts, embedding=embeddings, persist_directory=persist_dir)
    return vectorstore


def query_document(vectorstore, query, api_key):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
        return_source_documents=False
    )

    result = qa_chain.run(query)
    return result
