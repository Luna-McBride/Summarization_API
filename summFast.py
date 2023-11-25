import os
from pydantic import BaseModel
from fastapi import FastAPI

from dotenv import load_dotenv

load_dotenv(override = True)

from openai import OpenAI
client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

app = FastAPI()

class Summary(BaseModel):
	grade_level: int
	text: str

@app.get("/")
async def root():
	return {"message":"Hello, please use /api/"}

@app.post("/api/")
async def api(summary: Summary):
	PREFACE = f"Summarize this at a grade {summary.grade_level} level: "
	dual = PREFACE + summary.text

	response = client.chat.completions.create(
  		model="gpt-3.5-turbo",
  		messages=[{"role": "user", "content":dual}],
  		temperature=0,
  		max_tokens=1024
	)

	return {"message":response.choices[0].message.content}