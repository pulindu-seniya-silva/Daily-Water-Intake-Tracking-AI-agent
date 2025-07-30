import os 
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4", temperature=0.5)

class WaterIntakeAgent:

    def __init__(self):
        self.hostory = []
    
    def analyze_intake(self, intake_ml):

        prompt = f"""
        you are a hydration assistant. The user has consumed {intake_ml} ml of water today
        provide a hydration status and sugest if they need to drink more water
        """
        response = llm.invoke([HumanMessage(content=prompt)])

        return response.content
        
if __name__ == "__main__":
    agent = WaterIntakeAgent()
    intake = 1500
    feedback = agent.analyze_intake(intake)
    print(f"Hydration Analysis: {feedback}")
    

