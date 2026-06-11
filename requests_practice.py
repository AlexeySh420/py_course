import requests

#GET
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())
print(response.status_code)
print(response.headers["Content-Type"])

#POST
api_url = "https://jsonplaceholder.typicode.com/todos/"
todo = {"userId": 1, "title": "post_test", "completed": True}
response = requests.post(api_url, json=todo)
print(response.json())
print(response.status_code)