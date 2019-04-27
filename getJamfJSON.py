import requests
import urllib3
import json

def getJSON(url, hdrs, usr, pw):

    urllib3.disable_warnings()
    r = requests.get(url, headers=hdrs, auth=(usr, pw), verify=False)
    d = json.loads(r.text)
    return d