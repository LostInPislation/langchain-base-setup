from langchain.llms import Ollama

llm = Ollama(model="orca2")

def start():
    response = llm("Tell me a joke")
    print(response)

