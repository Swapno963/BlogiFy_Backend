import requests

# Define your API endpoint URL
register_url = "http://127.0.0.1:8000/auth/register/"

# Define the login credentials (username and password)
credentials ={
    # 'username':'b',
 'first_name':'swapno2', 'last_name':'mondol2', 'email':'swapnoms7d3@gmail.com', 'password':'12345678n', 'confirm_password':'12345678n'
}

# Make a POST request to the login endpoint with the credentials
response = requests.post(register_url, data=credentials)

# Check the response status code
if response.status_code == 200:
    # If the login was successful, print the response content (token)
    print("Login successful!")
    # print(dir(response))
    response_json = response.json()
    print(response_json)
    # print("Access Token:", response.json()["access"])
    # print("Refresh Token:", response.json()["refresh"])
else:
    # If the login failed, print the error message
    # print("Login failed:", response.json()["error"])
    print("Login failed:", response)