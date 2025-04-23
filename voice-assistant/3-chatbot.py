from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load model & tokenizer
model_id = "openchat/openchat-3.5-1210"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype="auto", trust_remote_code=True)

# Set up a basic chat prompt
#prompt = "<|system|>\nYou are a helpful AI assistant.\n<|user|>\nHow do I check if an object is an instance of a class in Python?\n<|assistant|>"
prompt = "what is the world population?"
# Generate a response
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
output = model.generate(
    **inputs,
    max_new_tokens=200,
    do_sample=True,
    top_p=0.9,
    pad_token_id=tokenizer.eos_token_id,
)

# Decode and print
response = tokenizer.decode(output[0], skip_special_tokens=True)
print(response)
