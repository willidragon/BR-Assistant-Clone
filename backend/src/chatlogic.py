# chatlogic_modify.py


from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_openai import ChatOpenAI
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

from langchain_core.messages import HumanMessage, AIMessage

from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.schema.agent import AgentFinish

from langchain.memory import ConversationBufferMemory


from decouple import config
from operator import itemgetter
from src.custom_tools import *

tools = [get_recipe_field, change_field_data, list_all_product_ids]   
functions = [convert_to_openai_function(tool) for tool in tools]
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

model = ChatOpenAI(

    model_name = "gpt-3.5-turbo",
    openai_api_key = config("OPENAI_API_KEY"),
    temperature=0,
    functions=functions,

)


prompt = ChatPromptTemplate.from_messages([
    ("system", "你是個專業助理，會用系統提供給你的工具去幫用戶解決問題。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])


# result1 = chain.invoke({
#     "input": "可以顯示300@3_CPEUVCDU05MVIA000EM-F這個product ID 的 RECIPE_GROUP 嗎",
#     "agent_scratchpad": []
# })

agent_chain = RunnablePassthrough.assign(
    agent_scratchpad= lambda x: format_to_openai_functions(x["intermediate_steps"])
) | prompt | model | OpenAIFunctionsAgentOutputParser()

memory = ConversationBufferMemory(return_messages=True,memory_key="chat_history")

# Hardcoded chat history
# chat_history_hc = [
#     HumanMessage(content="我的名字是William"),
#     AIMessage(content="你好，William！"),
    
# ]
def run_agent(user_input):
    def get_formatted_history():
        memory_variables = memory.load_memory_variables({})
        chat_history = memory_variables.get("chat_history", [])

        # Ensure chat_history is a list of messages
        if isinstance(chat_history, list):
            return chat_history  # Return the list directly
        return []

    intermediate_steps = []
    tools_used = []

    while True:
        result = agent_chain.invoke({
            "input": user_input, 
            "intermediate_steps": intermediate_steps,
            "chat_history": get_formatted_history(),
        })
        
        if isinstance(result, AgentFinish):
            # Convert user input to string and record it
            memory.chat_memory.add_user_message(str(user_input))
            
            # Extract the AI response
            ai_response = result.return_values.get("output", "")
            
            # Record the AI response in the chat memory
            memory.chat_memory.add_ai_message(str(ai_response))
            
            logging.info(f"Formatted history: {get_formatted_history()}")
            return {
                "output": ai_response,
                "tools_used": ", ".join(tools_used) if tools_used else "No tools used"
            }
        
        tool_name = result.tool
        tools_used.append(tool_name)

        tool = {
            "get_recipe_field": get_recipe_field,
            "change_field_data": change_field_data,
            "list_all_product_ids": list_all_product_ids
        }[tool_name]
        observation = tool.run(result.tool_input)
        intermediate_steps.append((result, observation))

        # Record the tool's output (AI response) in the chat memory
        memory.chat_memory.add_ai_message(str(observation))



def get_answer(question: str):
    # Use the run_agent function to get the result
    result = run_agent(question)
    
    # Extract the final answer and tools used from the result
    answer = result.get("output", "No answer available")
    tools_used = result.get("tools_used", "No tools used")
    
    # Return the result in the expected format
    return { 
        "answer": answer,
        "tools_used": tools_used,
    }
