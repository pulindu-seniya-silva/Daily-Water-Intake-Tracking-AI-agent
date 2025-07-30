from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import WaterIntakeAgent
from src.database import lo_intake, get_intake_history
from src.logger import log_message

app = FastAPI()
agent = WaterIntakeAgent()

class WaterIntakeRequest(BaseModel):
    user_id: str
    intake_ml: int

