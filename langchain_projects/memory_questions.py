from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI

import json

from langchain.memory import ChatMessageHistory
from langchain.schema import messages_from_dict, messages_to_dict

# create a history object
history = ChatMessageHistory()

# load dicts from json file
with open("temp.json", "r") as f:
    dicts = json.load(f)

previous_messages = messages_from_dict(dicts)
#add previous messages to history
history.messages = previous_messages

key="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"
import os
os.environ["OPENAI_API_KEY"] = key

agent_executor = create_python_agent(
    llm=OpenAI(temperature=0, max_tokens=3000 ),
    tool=PythonREPLTool(),
    memory=previous_messages,
    verbose=True
)

prompt = """
You are an expert in Object Oriented Programming.
You love to use SOLID programming principles.
You love to use GoF design patterns even when it is not even necessary.

We are building a command line chatbot.  The chatbot application
will take user input from stdin.  The chatbot will respond to
the user's input.  The chatbot is as intelligent as you are.
The chatbot will need a place to store conversation history on the filesystem
for future conversations, so we need some type of memory.
Think step by step.

Your tasks will be:
Create an html page with a list of all of the objects needed to build this chatbot.
Include descriptions and code examples in the html page.
Style the html page with CSS.  Use Blue, Yellow, Green, Gray, White, Black, and Red.
Style the example python code in code blocks.
Write the output of the html page to a file called chatbot.html.
"""
history.add_user_message(prompt)

history.add_ai_message( agent_executor.run( prompt ))
# save dicts to json file
with open("temp.json", "w") as f:
    json.dump(messages_to_dict(history.messages), f)