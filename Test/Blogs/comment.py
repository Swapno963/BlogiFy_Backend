import requests
import json

# for environmant variable 
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

baseUrl = os.environ['URL']
token = os.environ['ACCESS_TOKEN']
headers = {"Authorization": f"Bearer {token}"}
data = {
    'content':'good blog 2 ',
    'author':'1',
    'blog':'4'
    
}
response = requests.post(f"http://127.0.0.1:8000/blogs/comment/4/", headers=headers, data=data)
    # response = requests.get("http://127.0.0.1:8000/auth/profile/")

print(response)
response_json = response.json()
print(response_json)