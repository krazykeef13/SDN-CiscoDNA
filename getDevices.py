import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import urllib3

urllib3.disable_warnings()

username = input("Please enter a username: ")
password = getpass("Please enter a password: ")

BASE_URL = 'https://sandboxdnac.cisco.com'
AUTH_URL = '/dna/system/api/v1/auth/token'
USERNAME = '<USERNAME>'
PASSWORD = '<PASSWORD>'

response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(username, PASSWORD), verify=False)
Token = response.json() ['Token']

headers = {'X-Auth-Token': 'Token', 'Accept': 'application/json', 'Content-Type': 'application/json'}
DEVICES_COUNT_URL = '/dna/intent/api/v1/network-device/count'
response = requests.get(BASE_URL + DEVICES_COUNT_URL,
                        headers=headers, verify=False)

print(response.json()['response'])
