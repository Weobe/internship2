#c2
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM


# set quantization configuration to load large model with less GPU memory
# this requires the `bitsandbytes` library
bnb_config = transformers.BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type='nf4',
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16
)


tokenizer2 = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf",
                                          use_auth_token=True,)

model2 = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf",
                                            quantization_config=bnb_config,
                                             device_map='auto',
                                             torch_dtype=torch.float16,
                                             use_auth_token=True,
                                            #  load_in_8bit=True,
                                            #  load_in_4bit=True
                                            )





tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-13b-chat-hf",
                                          use_auth_token=True,)

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-13b-chat-hf",
                                             quantization_config=bnb_config,
                                             device_map='auto',
                                             torch_dtype=torch.float16,
                                             use_auth_token=True,
                                            #  load_in_8bit=True,
                                            #  load_in_4bit=True
                                             )

