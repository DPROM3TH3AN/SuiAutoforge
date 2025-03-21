# tests/test_chatbot.py

from src.chatbot import get_chatbot_response

def test_get_chatbot_response():
    prompt = "Test prompt for a smart contract"
    response = get_chatbot_response(prompt)
    # Ensure that the response is a non-empty string
    assert isinstance(response, str)
    assert len(response.strip()) > 0