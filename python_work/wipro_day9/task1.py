"""Task 1: Use the requests library in Python to make a GET request to a public API and print the response.

"""
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status Code: ", response.status_code)
print("Response Body: ",response.json())
