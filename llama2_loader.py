import transformers
import torch
import accelerate

from transformers import AutoTokenizer

LLAMA2_MODEL_PATH = '../llama/llama-2-7b-chat-hf' 
TOKENIZER=AutoTokenizer.from_pretrained(LLAMA2_MODEL_PATH)
PIPELINE=transformers.pipeline(
    "text-generation",
    model=LLAMA2_MODEL_PATH,
    return_full_text=True,  # langchain expects the full text
    tokenizer=TOKENIZER,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    #device="cuda:0",
    device_map="auto",
    max_length=2048,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=TOKENIZER.eos_token_id,
    repetition_penalty=1.1  # without this output begins repeating
    )