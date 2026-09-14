import os

from langchain_openai import ChatOpenAI
from pydantic import SecretStr

if __name__ == '__main__':

    llm = ChatOpenAI(
        model="qwen3.8-flash",
        api_key=SecretStr(os.environ["DASHSCOPE_API_KEY"]),
        base_url=os.environ["ALI_BAI_LIAN_URL"],
    )


    response = llm.invoke("你好，请介绍一下你自己")

    print(response.content)