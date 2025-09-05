import requests

url = "http://127.0.0.1:5000/ask"
payload = {"question": "What are the library timings?"}
response = requests.post(url, json=payload)

print(response.json())
