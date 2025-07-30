import os 
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMEssage
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4", temperature=0.5)
