from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI

key=""
import os
os.environ["OPENAI_API_KEY"] = key


agent_executor = create_python_agent(
    llm=OpenAI(temperature=0, max_tokens=3000 ),
    tool=PythonREPLTool(),
    verbose=True
)

prompt = """
You are an expert in Object Oriented Programming.

We are building a command line chatbot.  The chatbot application
will take user input from stdin.  The chatbot will respond to
the user's input.  The chatbot is as intelligent as you are.
The chatbot will need a place to store conversation history on the filesystem
for future conversations, so we need some type of memory.
Think step by step.

Your tasks will be:
Build the directory structure for this project.
Populate the python files needed to contain all of 
the objects needed to build this chatbot.
Create an html document for each of the objects in this project.
Populate the document with a colorful presentation of the description of each object.
"""
agent_executor.run( prompt )