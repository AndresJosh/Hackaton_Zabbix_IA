from gpt4all import GPT4All

gpt = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
response = gpt.generate("Give me recommendations for optimizing network bandwidth.")
print(response)
