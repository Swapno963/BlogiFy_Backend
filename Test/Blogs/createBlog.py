import requests
import json

# for environmant variable 
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()
token = os.environ['ACCESS_TOKEN']
baseUrl = os.environ['URL']
# print(token)
# Access environment variables



headers = {"Authorization": f"Bearer {token}"}
image_path ="./blogImg/download (1).jpg"

# Open the image file
with open(image_path, 'rb') as file:
    # Prepare the files parameter with the image file
    files = {'thumbnail': file}

    blogData = {
        "title": "This is new blog",
        "content": "hello everyone ",
        "likes": 1,
        "author": 1,
        # "author": 'gfdg',
        "comments": 1,
        "tag": [1]
    }

    response = requests.post(f"{baseUrl}/blog/blog/", headers=headers, data=blogData, files=files)
    # response = requests.get("http://127.0.0.1:8000/auth/profile/")

    # response_json = response.json()
    # print(response_json)
    print(response)