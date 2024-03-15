import requests
import json

# for environmant variable 
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()
token = os.environ['ACCESS_TOKEN']
print(token)
# Access environment variables



headers = {"Authorization": f"Bearer {token}"}




response = requests.post("http://127.0.0.1:8000/blog/tag/", headers=headers, data={
    "name": "Python"
})
# response = requests.get("http://127.0.0.1:8000/auth/profile/")

response_json = response.json()
print(response_json)