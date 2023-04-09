import http.client
import json

conn = http.client.HTTPSConnection("sneaker-database-stockx.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "insert  your key "
  
    'X-RapidAPI-Host': "sneaker-database-stockx.p.rapidapi.com"
    }

conn.request("GET", "/getproducts?keywords=Air%20Jordan&limit=10", headers=headers)

res = conn.getresponse()
data = res.read()

data = json.loads(data.decode("utf-8"))



for item in data:
    print(item['shoeName'], '\n', item['brand'], '\n', item['silhoutte'], '\n', item['styleID'], '\n', item['make'],'\n', item['colorway'], '\n', item['retailPrice'], '\n', item['releaseDate'],'\n',item['thumbnail'])


