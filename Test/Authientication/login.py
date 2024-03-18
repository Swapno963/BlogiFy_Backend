import requests

# Define your API endpoint URL
login_url = "http://127.0.0.1:8000/auth/login/"

# Define the login credentials (username and password)
credentials ={
"email":"swapnoms7d3@gmail.com",
"password":"12345678n"
}

# Make a POST request to the login endpoint with the credentials
response = requests.post(login_url, data=credentials)

# Check the response status code
if response.status_code == 200:
    # If the login was successful, print the response content (token)
    # print("Login successful!")
    # print(dir(response))
    response_json = response.json()
    print(response_json)
    # print("Access Token:", response.json()["access"])
    # print("Refresh Token:", response.json()["refresh"])
else:
    # If the login failed, print the error message
    print("Login failed:", response.json())