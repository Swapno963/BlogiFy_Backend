import requests
# for environmant variable 
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()
access_token = os.environ['ACCESS_TOKEN']
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get("http://127.0.0.1:8000/auth/profile/", headers=headers)
# response = requests.get("http://127.0.0.1:8000/auth/profile/")

response_json = response.json()
print(response_json)