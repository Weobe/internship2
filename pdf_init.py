#c7
from format_helper import *

from langchain import HuggingFacePipeline
from langchain import PromptTemplate,  LLMChain


llm = HuggingFacePipeline(pipeline = pipe, model_kwargs = {'temperature':0})
llm2 = HuggingFacePipeline(pipeline = pipe2, model_kwargs = {'temperatue':0})


