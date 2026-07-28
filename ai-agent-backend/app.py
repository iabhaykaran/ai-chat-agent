#pip install google-genai python-dotenv

#pip install fastapi uvicorn python-dotenv google-genai


# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# while True:
#     user = input("You: ")

#     if user.lower() == "exit":
#         break

#     try:
#         response = client.models.generate_content(
#             model="gemini-3.6-flash",
#             contents=user
#         )

#         print("\nAgent:", response.text)

#     except Exception as e:
#         print("\nError:", e)
#upper one for terminal run using py app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(req: ChatRequest):
    print("Received:", req.message)

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=req.message
    )

    print("Gemini Response:", response.text)

    return {
        "reply": response.text
    }

#run using py -m uvicorn app:app --reload
    