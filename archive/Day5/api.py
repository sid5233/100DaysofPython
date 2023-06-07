from urllib import response
import requests

response = requests.get("https://reqres.in/api/users?page=2")
print(response.json())
print(type(response.json()))

