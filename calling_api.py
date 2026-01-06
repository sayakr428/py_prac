#calling api

import requests

url = "https://api.sampleapis.com/"

beverages = "coffee"
type = "hot"

query = f"{beverages}/{type}"

print(url + query)

def fetch_data():
    print("Fetching data...")
    resposnse = requests.get(url=url + query)
    for item in resposnse.json()[1:5]:
        print(item)
       
    data = resposnse.json()
    for item in data:
        print(set(item["title"]))
    print("Data fetched successfully.")


fetch_data()      
