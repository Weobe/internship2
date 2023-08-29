from format_helper import *
from langchain import HuggingFacePipeline
from langchain import PromptTemplate,  LLMChain
import os
from text import wrap_text
from pdf import *

llm = HuggingFacePipeline(pipeline = pipe, model_kwargs = {'temperature':0.3})
llm2 = HuggingFacePipeline(pipeline = pipe2, model_kwargs = {'temperature':0})

while True:
    os.system("clear")

    #ask for the domain of the chat and add it to system prompt for higher quality answers
    #pdf option to use the document understanding feature
    
    domain = input("Please specify a domain for your question: ")
    if domain == "pdf":
        read_pdf()
    else:
        system_prompt = "You are an honest, helpful and advanced assistant that excels at the domain of {}".format(domain)

        if (domain == "general chat"):
            instruction = "{text}"
        else:
            instruction = "Please answer this question in the context of " + domain + ". {text}. "#Your answer should depend solely on mathematical modeling"

        #print the instruction and system prompt for transparency
        print(instruction)
        print(system_prompt)

        #create a template that merges instruction and system prompt
        template = get_prompt(instruction, system_prompt)
        print(template)
        prompt = PromptTemplate(template=template, input_variables=["text"])

        #create a chain with the template
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        #answer questions in the current domain until user types 'exit'
        while True:
            os.system("clear")
            text = input("Enter question: ")
            if text == "exit":
                break
            output = llm_chain.run(text)
            parse_text(output)
            input("Press Enter to continue...")
