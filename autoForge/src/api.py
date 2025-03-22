from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from chatbot import get_chatbot_response
from contract_generator import generate_contract
import os

router = APIRouter()

class GenerationRequest(BaseModel):
    prompt: str

class GenerationResponse(BaseModel):
    contract_code: str
    message: str

@router.post("/generate_contract", response_model=GenerationResponse)
async def generate_smart_contract(request: GenerationRequest):
    try:
        chatbot_response = get_chatbot_response(request.prompt)
        contract_code = generate_contract(chatbot_response)
        return GenerationResponse(contract_code=contract_code, message="Contract generated successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

port = int(os.environ.get("PORT", 8000))
# When starting with uvicorn, you can use: uvicorn src.api:app --host 0.0.0.0 --port $PORT