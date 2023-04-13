#
#
from langchain import SerpAPIWrapper, PromptTemplate, LLMChain, OpenAI
from langchain.python import PythonREPL
from langchain.agents import Tool
import os

os.environ["OPENAI_API_KEY"] = "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"  # https://platform.openai.com (Thx Michael from Twitter)
os.environ['SERPAPI_API_KEY'] = '7f82b0d093d8f19a51883a154178c63fdd0013f55162b4433d12c5812c0532e6' # https://serpapi.com/
search = SerpAPIWrapper()
# todo_prompt = PromptTemplate.from_template(
#     """
#     You are a planner who is an expert at coming up with a todo list for a given objective.
#     Come up with a todo list for this objective: {objective}")
#     """ )
todo_prompt = PromptTemplate.from_template(
    """
    What time is it right now in EST?")
    """ )
todo_chain = LLMChain( llm=OpenAI( temperature=0 ), prompt=todo_prompt )
tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name = "TODO",
        func=todo_chain.run,
        description="useful for when you need to come up with todo lists. Input: an objective to create a todo list for. Output: a todo list for that objective. Please be very clear what the objective is!"
    ),
    Tool( name = "PythonREPL",
        func=PythonREPL().run,
        description="useful for when you need to run python code"
    ),
]