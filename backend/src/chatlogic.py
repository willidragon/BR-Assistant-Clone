# chatlogic.py

from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_openai import ChatOpenAI
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser

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

prompt_template = """
你是一個非常有禮貌和專業的助理，總是根據現有的信息提供最準確的答案。如果您無法回答一個問題，請坦誠地說明並提供可能的替代解決方案或建議用戶尋求其他資源。請始終使用繁體中文作答。


Question: {question}
Answer:
"""

prompt = ChatPromptTemplate.from_template(prompt_template)




def create_chain():
    chain = (
        {
            "question": RunnablePassthrough(),
        }
        | RunnableParallel({
            "response" : prompt | model,
        }))
    return chain

def get_answer(question: str):
    chain = create_chain()
    response = chain.invoke(question)
    answer = response["response"].content
    return {
        "answer": answer,
    }


