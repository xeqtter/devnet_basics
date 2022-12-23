import token
import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_PORT, DNAC_USER, DNAC_PASSWORD

# Get the deviceId you need to send to retrieve the interface. You loop through the list in the response.
def get_device_id(device_json):
    for device in device_json['response']: 
        print("Fetching Interfaces for Device Id ----> {}".format(device['id']))
        print('\n')
        get_device_int(device['id'])
        print('\n')

# Define the function and write the GET request for the interface. 
# This builds on the function that you wrote earlier in this Learning Lab for retrieving a list of devices.
def get_device_int(device_id):
    
    # Building out function to retrieve device interface. Using requests.get
    # to make a call to the network device Endpoint
    url = "https://sandboxdnac.cisco.com/api/v1/interface"
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    querystring = {"macAddress": device_id} 
    resp = requests.get(url, headers=hdr, params=querystring) 
    interface_info_json = resp.json()
    print_interface_info(interface_info_json)

    
    # Once again you need to make sure you write the get_auth_token() function 
    # that is referenced for both the GET request and the later filtering.
def get_auth_token():
    
    # Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'       # Endpoint URL
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD))  # Make the POST Request
    token = resp.json()['Token']    # Retrieve the Token 
    return token    # Create a return statement for the Token

# Here you want to make the printed output easy to read.
def print_interface_info(interface_info):
    print("{0:42}{1:17}{2:12}{3:18}{4:17}{5:10}{6:15}".
        format("portName", "vlanId", "portMode", "portType", "duplex", "status", "lastUpdated"))
    for int in interface_info['response']:
        print("{0:42}{1:10}{2:12}{3:18}{4:17}{5:10}{6:15}".
            format(str(int['portName']),
                    str(int['vlanId']),
                    str(int['portMode']),
                    str(int['portType']),
                    str(int['duplex']),
                    str(int['status']),
                    str(int['lastUpdated'])))

# These last two lines run the function.
if __name__ == "__main__":
    get_device_int()
    
