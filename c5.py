from c4 import *
from langchain import HuggingFacePipeline
from langchain import PromptTemplate,  LLMChain
import os
from text import wrap_text
from pdf import *

llm = HuggingFacePipeline(pipeline = pipe, model_kwargs = {'temperature':0.3})
llm2 = HuggingFacePipeline(pipeline = pipe2, model_kwargs = {'temperature':0})

while True:
    os.system("clear")
    domain = input("Please specify a domain for your question: ")
    if domain == "pdf":
        read_pdf()
    else:
        system_prompt = "You are an honest, helpful and advanced assistant that excels at the domain of {}".format(domain)

        if (domain == "general chat"):
            instruction = "{text}"
        else:
            instruction = "Please answer this question in the context of " + domain + ". {text}. "#Your answer should depend solely on mathematical modeling"
        
        print(instruction)
        print(system_prompt)
        template = get_prompt(instruction, system_prompt)
        print(template)
        prompt = PromptTemplate(template=template, input_variables=["text"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        while True:
            os.system("clear")
            text = input("Enter question: ")
            if text == "exit":
                break
            output = llm_chain.run(text)
            parse_text(output)
            input("Press Enter to continue...")
