from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI

key="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"
import os
os.environ["OPENAI_API_KEY"] = key


agent_executor = create_python_agent(
    llm=OpenAI(temperature=0,
               model_name="gpt-4",
               max_tokens=10000 ),
    tool=PythonREPLTool(),
    verbose=True
)

prompt = """
You are an expert in Object Oriented Programming.

AI, please create a Python-based command line chatbot application that 
takes user input from stdin and provides responses based on the user's input. 
The chatbot should store conversation history on the filesystem for future 
conversations. To accomplish this, please follow these steps:

Create a directory structure:

|-chatbot
|-src
 -- chatbot.py
 -- memory.py
|-data
|-conversations

In the memory.py file, create a class named Memory to manage conversation 
storage. Implement the following methods:
__init__(self, file_path: str): Initialize the file_path attribute.
load_conversations(self) -> List[Dict[str, str]]: Load conversation history from the file and return it as a list of dictionaries, each containing 'user_input' and 'bot_response' keys.
save_conversation(self, user_input: str, bot_response: str): Save the current 
conversation to the file by appending a dictionary with 'user_input' and 
'bot_response' keys.

Ensure that the class can handle creating the file if it does not exist and 
can read and write JSON data.

In the chatbot.py file, create a class named Chatbot to handle the chatbot 
logic. Implement the following methods:
__init__(self, memory: Memory): Initialize the memory attribute using an instance of the Memory class.
get_response(self, user_input: str) -> str: Process the user_input and return a string as the chatbot's response. For now, you can return a simple hardcoded response, such as "I am still learning. Please try again later."
run(self): Implement a loop that reads user input from stdin, processes the input, and prints the chatbot's response. The loop should continue until the user types "exit" or "quit". Additionally, save the conversation to the memory after each interaction.

In the chatbot.py file, add a main function to instantiate and run the chatbot:
``` python
def main():
    memory = Memory("data/conversations/conversations.json")
    chatbot = Chatbot(memory)
    print("Welcome to the Chatbot! Type 'exit' or 'quit' to end the conversation.")
    chatbot.run()

if __name__ == "__main__":
    main()
```

Please ensure that the application has proper error handling, logging, 
and follows SOLID principles and GoF design patterns where appropriate.
"""
agent_executor.run( prompt )