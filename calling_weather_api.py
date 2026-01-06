#calling weather API and printing result
import requests

url ="http://goweather.xyz/weather/"
input_city = input("Enter city name: ")

query_url = f"{input_city}"

response = requests.get(url + query_url)
print(response.json())
print(response.status_code)
print(type(response.json()))

for key, value in response.json().items():
    print(f"{key}: {value}")
