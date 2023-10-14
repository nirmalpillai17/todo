import requests
import json

# function to send request to baceknd api
def send_request(url, method, data={}):
    resp = requests.Response()
    if method == "GET":
        resp = requests.get(url)
    elif method == "POST":
        resp = requests.post(url, json=data)
    elif method == "PUT":
        resp = requests.put(url, json=data)
    elif method == "DELETE":
        resp = requests.delete(url)
    else:
        raise Exception("Invalid HTTP method")
 
    return json.loads(resp.text) if resp.text else {}
