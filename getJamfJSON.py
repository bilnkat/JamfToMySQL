import requests
import urllib3

def getJSON(url, hdrs, usr, pw):

    urllib3.disable_warnings()
    r = requests.get(url, headers=hdrs, auth=(usr, pw), verify=False)
    return r