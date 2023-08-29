#c6
from langchain.embeddings import HuggingFaceEmbeddings

#replace model name to use another model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {}
encode_kwargs = {'normalize_embeddings': False}

hf = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
)
