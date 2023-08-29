from langchain.document_loaders import PyPDFLoader
from load_sentence_transformer import *
from pdf_init import *
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os 
from text import wrap_text


def read_pdf():
    #load document
    pdf_name = input("Enter pdf name: ")
    if not pdf_name.endswith(".pdf"):
        pdf_name = pdf_name + ".pdf"

    try:
        loader = PyPDFLoader(
        pdf_name,# mode="elements", strategy="fast",
        )

        docs = loader.load()

    except:
        return
        
    #split text and store embedding in vectorstore
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    all_splits = text_splitter.split_documents(docs)

    vectorstore = FAISS.from_documents(documents=all_splits, embedding=HuggingFaceEmbeddings())

    #initialize a Q&A chain with the main LLM and vectorstore of the pdf
    qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())

    #answer questions from the pdf until user types 'exit'
    while True:
        os.system('clear')
        question = input("Ask a question: ")
        if (question == "exit"):
            return
        ans = qa_chain({"query": question})
        txt = ans['result']
        
        #format text for better readability in terminal
        wrapped_txt = wrap_text(txt, 60)
        
        print("\n" + wrapped_txt)
        input("\nPress enter to continue...")

