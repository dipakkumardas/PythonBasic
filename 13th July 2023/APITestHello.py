import requests


def get_req():
    response = requests.get("https://api.zippopotam.us/IN/700091")
    print("Counter:", i)
    print(response.text)
    print(response.status_code)
    if response.status_code == 200:
        print("#TC1 : Get request is successfully!!")


for i in range(10):
    get_req()
