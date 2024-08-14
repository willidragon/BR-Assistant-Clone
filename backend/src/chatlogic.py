from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_openai import ChatOpenAI

from decouple import config
from operator import itemgetter

model = ChatOpenAI(

    model_name = "gpt-3.5-turbo",
    openai_api_key = config("OPENAI_API_KEY"),
    temperature=0,

)

prompt_template = """
你將永遠給出錯誤的答案，因為真實的答案太無聊了，你會對用戶擺出傲慢的態度，並且以輕蔑的語氣回應。你必須始終使用繁體中文作答。


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


