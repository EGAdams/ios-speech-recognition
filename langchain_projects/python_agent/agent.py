from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI

key="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"
import os
os.environ["OPENAI_API_KEY"] = key


agent_executor = create_python_agent(
    llm=OpenAI(temperature=0, max_tokens=1000 ),
    tool=PythonREPLTool(),
    verbose=True
)

prompt = "Please write the contents of this conversation in json format to ./temp.json"
agent_executor.run( prompt )