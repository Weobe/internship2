from c2 import *

# Use a pipeline for later
from transformers import pipeline

pipe = pipeline("text-generation",
                model=model,
                tokenizer= tokenizer,
                torch_dtype=torch.bfloat16,
                device_map="auto",
                max_new_tokens = 1024,
                do_sample=True,
                top_k=30,
                num_return_sequences=1,
                eos_token_id=tokenizer.eos_token_id
                )



pipe2 = pipeline("text-generation",
                model = model2,
                tokenizer=tokenizer2,
                torch_dtype=torch.bfloat16,
                device_map="auto",
                max_new_tokens = 1024,
                do_sample=True,
                top_k=30,
                num_return_sequences=1,
                eos_token_id=tokenizer2.eos_token_id
                )
