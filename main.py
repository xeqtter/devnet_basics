import requests
from requests.auth import HTTPBasicAuth
import env_lab

requests.packages.urllib3.disable_warnings()

def get_auth_token():
    # Endpoint URL
    endpoint = '/dna/system/api/v1/auth/token'
    url = 'https://' + env_lab.DNA_CENTER['host'] + endpoint
    # Make the POST Request
    resp = requests.post(url, auth=HTTPBasicAuth(env_lab.DNA_CENTER['username'], env_lab.DNA_CENTER['password']), verify=False)
    # Retrieve the Token from the returned JSON
    token = resp.json()['Token']
    # Print out the Token
    print("Token Retrieved: {}".format(token))
    # Create a return statement to send the token back for later use
    return token

if __name__ == "__main__":
    get_auth_token()
    
    