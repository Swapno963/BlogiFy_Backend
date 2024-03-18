


import requests
import json

# for environmant variable 
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

baseUrl = os.environ['URL']
response = requests.get(f"{baseUrl}/auth/showProfile/2/")
    # response = requests.get("http://127.0.0.1:8000/auth/profile/")

response_json = response.json()
print(response_json)
# url = 'http://127.0.0.1:8000/auth/showProfile/1/'