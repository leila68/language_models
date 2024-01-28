from gpt4all import GPT4All
# model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
model = GPT4All("gpt4all-falcon-newbpe-q4_0.gguf")
output = model.generate("what is the capital of Canada? ", max_tokens=10)
print(output)
