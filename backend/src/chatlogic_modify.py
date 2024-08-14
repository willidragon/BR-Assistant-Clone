# chatlogic_modify.py

from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_openai import ChatOpenAI
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.prompts import MessagesPlaceholder
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.schema.agent import AgentFinish


from decouple import config
from operator import itemgetter
from src.custom_tools import *

tools = [get_recipe_field, change_field_data]
functions = [convert_to_openai_function(tool) for tool in tools]

model = ChatOpenAI(

    model_name = "gpt-3.5-turbo",
    openai_api_key = config("OPENAI_API_KEY"),
    temperature=0,
    functions=functions,

)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是個幫助助理，可以回答有半導體製程的問題。你會用input同樣的語言回答"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

chain = prompt | model | OpenAIFunctionsAgentOutputParser()

# result1 = chain.invoke({
#     "input": "可以顯示300@3_CPEUVCDU05MVIA000EM-F這個product ID 的 RECIPE_GROUP 嗎",
#     "agent_scratchpad": []
# })

agent_chain = RunnablePassthrough.assign(
    agent_scratchpad= lambda x: format_to_openai_functions(x["intermediate_steps"])
) | chain

def run_agent(user_input):
    intermediate_steps = []
    while True:
        result = agent_chain.invoke({
            "input": user_input, 
            "intermediate_steps": intermediate_steps
        })
        if isinstance(result, AgentFinish):
            return result
        tool = {
            "get_recipe_field": get_recipe_field,
            "change_field_data": change_field_data
        }[result.tool]
        observation = tool.run(result.tool_input)
        intermediate_steps.append((result, observation))


def get_answer(question: str):
    # Use the run_agent function to get the result
    result = run_agent(question)
    
    # Extract the final answer from the result
    answer = result.return_values.get("output", "No answer available")
    
    # Return the result in the expected format
    return {
        "answer": answer,
    }

