import os #Import the operating system to get env variables
from pydantic import BaseModel #Import a base model to make passing text information easier
from fastapi import FastAPI #Import the API being used

from dotenv import load_dotenv #Import to get items from the .env file

load_dotenv(override = True) #Pull the api key from the .env file

from openai import OpenAI #Import OpenAI for GPT-3 use
client = OpenAI(api_key = os.getenv("OPEN_API_KEY")) #Build the client to use GPT-3

app = FastAPI() #Build the FastAPI app

#Build a base model of the expected pass-ins to the summarizer API
class Summary(BaseModel):
	grade_level: int #Get the grade level it should be summarized in
	text: str #Get the text to summarize

#Build a base message at / to describe usage
@app.get("/")
async def root():
	return {"message":"Hello, please use /api/ and pass in the grade level + text"} #Return the usage

#Build the API call itself
@app.post("/api/")
async def api(summary: Summary):
	#Create a preface telling the model to summarize it at a lower grade level
	PREFACE = f"Summarize this at a grade {summary.grade_level} level: "
	dual = PREFACE + summary.text #Add the preface to the text to summarize

	response = client.chat.completions.create( #Call the OpenAPI module
  		model="gpt-3.5-turbo", #Set the gpt model to gpt-3.5-turbo
  		messages=[{"role": "user", "content":dual}], #Set the role and pass in the text to summarize
  		temperature=0, #Send a temperature of 0 so the results do not get funky
  		max_tokens=1024 #Set the max token size so it does not get too big
	)

	return {"message":response.choices[0].message.content} #Return the text in JSON format