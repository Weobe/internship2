from langchain.document_loaders import PyPDFLoader
from c6 import *
from c7 import *
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os 
from text import wrap_text


def read_pdf():
    pdf_name = input("Enter pdf name: ")
    if not pdf_name.endswith(".pdf"):
        pdf_name = pdf_name + ".pdf"

    loader = PyPDFLoader(
        pdf_name,# mode="elements", strategy="fast",
        )

    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    all_splits = text_splitter.split_documents(docs)

    vectorstore = FAISS.from_documents(documents=all_splits, embedding=HuggingFaceEmbeddings())

    qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())
    while True:
        os.system('clear')
        question = input("Ask a question: ")
        if (question == "exit"):
            return
        ans = qa_chain({"query": question})
        txt = ans['result']
        wrapped_txt = wrap_text(txt, 60)
        print("\n" + wrapped_txt)
        input("\nPress enter to continue...")

