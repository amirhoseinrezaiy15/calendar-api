import requests

url = "http://127.0.0.1:5003/api/calendar/add"
data = {"date": "1404-01-18", "event": "ملاقات"}
response = requests.post(url, json=data)
print(response.text)