import os

from langchain.chat_models import init_chat_model
from pydantic import SecretStr

model = init_chat_model(
    model="qwen3.8-flash",
    model_provider="openai",
    api_key=SecretStr(os.environ["DASHSCOPE_API_KEY"]),
    base_url=os.environ["ALI_BAI_LIAN_URL"],
)