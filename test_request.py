import requests #Import requests to send to the api
import urllib
import os
import json

from dotenv import load_dotenv #Import to get items from the .env file

load_dotenv(override = True)

import google.auth.transport.requests
import google.oauth2.id_token

#Add a default article for testing
ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
2010 marriage license application, according to court documents.
Prosecutors said the marriages were part of an immigration scam.
On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
"""
audience = "https://equalizer-summarization-dwh7tpkipq-uw.a.run.app/"
url = "https://equalizer-summarization-dwh7tpkipq-uw.a.run.app/api/" #Add the link to the basic FastAPI landing
requ = {"grade_level":6, "text":ARTICLE} #Set the grade level and article to senf
data = json.dumps(requ)
data = data.encode()



try:
	req = urllib.request.Request(url, data = data, method = "POST")

	auth_req = google.auth.transport.requests.Request()
	id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)

	req.add_header('Content-Type', 'application/json')
	req.add_header("Authorization", f"Bearer {id_token}")
	response = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
	redirect = urllib.parse.urljoin(url, e.headers["location"])
	req_red = urllib.request.Request(redirect, data = data)
	print(redirect)

	auth_req = google.auth.transport.requests.Request()
	id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)

	req_red.add_header('Content-Type', 'application/json')
	req_red.add_header("Authorization", f"Bearer {id_token}")
	response = urllib.request.urlopen(req_red)

#summary = requests.post(url, json = req) #Send the request to the API
#summary_json = summary.json() #Get the response in JSON for easier usage

print(response.read().decode("utf-8")) #Print the returned message