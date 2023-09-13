"""
ConnectALL Robot framework listener. 
"""
import requests
# api to call a rest api using basic authentication

# Set the API endpoint URL
url = "https://api.example.com/endpoint"

# Set the basic authentication credentials
username = "your_username"
password = "your_password"

def restApiCall():
    # Create a session object and set the basic authentication
    session = requests.Session()
    session.auth = (username, password)

    # Make a GET request to the API endpoint
    response = session.get(url)

    # Check if the request was successful (200 status code)
    if response.status_code == 200:
        data = response.json()
        # Do something with the response data
    else:
        print("Request failed with status code:", response.status_code)
    
# A Class for capturing TestResult
class TestResult:
    """
        TestResult datastructure to hold the test status
    """
    def __init__(self,name):
        self.name = name

# Init function on main to call execute the rest api call
def init():
    restApiCall()
    
