import env_lab
import json
import requests
from requests.auth import HTTPBasicAuth
import urllib3

# Disable the SSL warning on the DevNet Sandbox; never do this in production
# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings()

#The code in this snippet first authenticates to the Cisco Always On DNA Center Sandbox host.
def get_token(host=env_lab.DNA_CENTER['host'],
            username=env_lab.DNA_CENTER['username'],
            password=env_lab.DNA_CENTER['password'],
            port=env_lab.DNA_CENTER['port']):
    """
    Use the REST API to log into an DNA_CENTER and retrieve a token
    """
    url = "https://{}:{}/dna/system/api/v1/auth/token".format(host,port)
    # Make Login request and return the response body
    response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), verify=False)
    token = response.json()["Token"]
    return token

# Now you have a token so you can use it as a header to make your next API call, 
# this time to find out what commands are available using GET /v1/network-device-poller/cli/legit-reads. 
# Once you have retrieved the JSON data from the response, have your code print the response with nice four-space indentation.
def get_commands(token, host=env_lab.DNA_CENTER['host'], port=env_lab.DNA_CENTER['port']):
    url = "https://{}:{}/api/v1/network-device-poller/cli/legit-reads".format(host,port)
    headers = {
        "X-Auth-Token": token
        }
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    print("Exec commands supported:")
    print(json.dumps(response.json()['response'], indent=4))
    
# For the last part of your code, you create the entry point for your program and have Python run 
# the two functions you wrote:
if __name__ == '__main__':

    get_commands(get_token())
    
    
