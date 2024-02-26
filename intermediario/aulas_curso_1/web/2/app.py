import requests

url = 'http://localhost:3333/'

response = requests.get(url)

print(response.status_code)
print(response.headers)
#print(response.content)
print(response.text)
