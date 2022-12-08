from datetime import datetime
import requests
print(datetime.now())

def send():
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return "There was an error"

if __name__ == "__main__":
    res = send()
    print(res)