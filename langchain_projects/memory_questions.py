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
You are my programming assistant.
Please create the python file for the chatbot interface.
"""
history.add_user_message(prompt)

history.add_ai_message( agent_executor.run( prompt ))
# save dicts to json file
with open("temp.json", "w") as f:
    json.dump(messages_to_dict(history.messages), f)