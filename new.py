import http.client
import json

conn = http.client.HTTPSConnection("sneaker-database-stockx.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "insert  your key "
  ,
    'X-RapidAPI-Host': "sneaker-database-stockx.p.rapidapi.com"
    }

conn.request("GET", "/getproducts?keywords=NEW%20Balance%20&limit=10", headers=headers)

res = conn.getresponse()
data = res.read()

data = json.loads(data.decode("utf-8"))

shoe_nameNEW1 = data[0]['shoeName']
colorwayNEW1 = data[0]['colorway']
retailPriceNEW1 = data[0]['retailPrice']
releaseDateNEW1 = data[0]['releaseDate']
thumbnailNEW1 = data[0]['thumbnail']

shoe_nameNEW2 = data[1]['shoeName']
colorwayNEW2 = data[1]['colorway']
retailPriceNEW2 = data[1]['retailPrice']
releaseDateNEW2 = data[1]['releaseDate']
thumbnailNEW2 = data[1]['thumbnail']

shoe_nameNEW3 = data[2]['shoeName']
colorwayNEW3 = data[2]['colorway']
retailPriceNEW3 = data[2]['retailPrice']
releaseDateNEW3 = data[2]['releaseDate']
thumbnailNEW3 = data[2]['thumbnail']

shoe_nameNEW4 = data[3]['shoeName']
colorwayNEW4 = data[3]['colorway']
retailPriceNEW4 = data[3]['retailPrice']
releaseDateNEW4 = data[3]['releaseDate']
thumbnailNEW4 = data[3]['thumbnail']

shoe_nameNEW5 = data[4]['shoeName']
colorwayNEW5 = data[4]['colorway']
retailPriceNEW5 = data[4]['retailPrice']
releaseDateNEW5 = data[4]['releaseDate']
thumbnailNEW5 = data[4]['thumbnail']

shoe_nameNEW6 = data[5]['shoeName']
colorwayNEW6 = data[5]['colorway']
retailPriceNEW6 = data[5]['retailPrice']
releaseDateNEW6 = data[5]['releaseDate']
thumbnailNEW6 = data[5]['thumbnail']

shoe_nameNEW7 = data[6]['shoeName']
colorwayNEW7 = data[6]['colorway']
retailPriceNEW7 = data[6]['retailPrice']
releaseDateNEW7 = data[6]['releaseDate']
thumbnailNEW7 = data[6]['thumbnail']


shoe_nameNEW8 = data[7]['shoeName']
colorwayNEW8 = data[7]['colorway']
retailPriceNEW8 = data[7]['retailPrice']
releaseDateNEW8 = data[7]['releaseDate']
thumbnailNEW8 = data[7]['thumbnail']


shoe_nameNEW9 = data[8]['shoeName']
colorwayNEW9 = data[8]['colorway']
retailPriceNEW9 = data[8]['retailPrice']
releaseDateNEW9 = data[8]['releaseDate']
thumbnailNEW9 = data[8]['thumbnail']

shoe_nameNEW10 = data[9]['shoeName']
colorwayNEW10 = data[9]['colorway']
retailPriceNEW10 = data[9]['retailPrice']
releaseDateNEW10 = data[9]['releaseDate']
thumbnailNEW10 = data[9]['thumbnail']
