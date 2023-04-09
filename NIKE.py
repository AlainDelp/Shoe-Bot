import http.client
import json

conn = http.client.HTTPSConnection("sneaker-database-stockx.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "insert  your key "
  ,
    'X-RapidAPI-Host': "sneaker-database-stockx.p.rapidapi.com"
    }

conn.request("GET", "/getproducts?keywords=nike&limit=10", headers=headers)

res = conn.getresponse()
data = res.read()
data = json.loads(data.decode("utf-8"))

shoe_nameNIKE1 = data[0]['shoeName']
colorwayNIKE1 = data[0]['colorway']
retailPriceNIKE1 = data[0]['retailPrice']
releaseDateNIKE1 = data[0]['releaseDate']
thumbnailNIKE1 = data[0]['thumbnail']

shoe_nameNIKE2 = data[1]['shoeName']
colorwayNIKE2 = data[1]['colorway']
retailPriceNIKE2 = data[1]['retailPrice']
releaseDateNIKE2 = data[1]['releaseDate']
thumbnailNIKE2 = data[1]['thumbnail']

shoe_nameNIKE3 = data[2]['shoeName']
colorwayNIKE3 = data[2]['colorway']
retailPriceNIKE3 = data[2]['retailPrice']
releaseDateNIKE3 = data[2]['releaseDate']
thumbnailNIKE3 = data[2]['thumbnail']

shoe_nameNIKE4 = data[3]['shoeName']
colorwayNIKE4 = data[3]['colorway']
retailPriceNIKE4 = data[3]['retailPrice']
releaseDateNIKE4 = data[3]['releaseDate']
thumbnailNIKE4 = data[3]['thumbnail']

shoe_nameNIKE5 = data[4]['shoeName']
colorwayNIKE5 = data[4]['colorway']
retailPriceNIKE5 = data[4]['retailPrice']
releaseDateNIKE5 = data[4]['releaseDate']
thumbnailNIKE5 = data[4]['thumbnail']

shoe_nameNIKE6 = data[5]['shoeName']
colorwayNIKE6 = data[5]['colorway']
retailPriceNIKE6 = data[5]['retailPrice']
releaseDateNIKE6 = data[5]['releaseDate']
thumbnailNIKE6 = data[5]['thumbnail']

shoe_nameNIKE7 = data[6]['shoeName']
colorwayNIKE7 = data[6]['colorway']
retailPriceNIKE7 = data[6]['retailPrice']
releaseDateNIKE7 = data[6]['releaseDate']
thumbnailNIKE7 = data[6]['thumbnail']


shoe_nameNIKE8 = data[7]['shoeName']
colorwayNIKE8 = data[7]['colorway']
retailPriceNIKE8 = data[7]['retailPrice']
releaseDateNIKE8 = data[7]['releaseDate']
thumbnailNIKE8 = data[7]['thumbnail']




