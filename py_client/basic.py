import requests


endpoint = "http://localhost:8000/api/"

get_response = requests.post(
    endpoint,
    json={"title": "KeyChrome k8", "content": "Awesome keyboard", "price": 40.99},
)
print(get_response.json())
print(get_response.status_code)
