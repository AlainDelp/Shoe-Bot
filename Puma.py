import http.client
import json
conn = http.client.HTTPSConnection("sneaker-database-stockx.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "insert  your key",
    'X-RapidAPI-Host': "sneaker-database-stockx.p.rapidapi.com"
    }

conn.request("GET", "/getproducts?keywords=Puma&limit=10", headers=headers)

res = conn.getresponse()
data = res.read()

data = json.loads(data.decode("utf-8"))

shoe_namePUMA1 = data[0]['shoeName']
colorwayPUMA1 = data[0]['colorway']
retailPricePUMA1 = data[0]['retailPrice']
releaseDatePUMA1 = data[0]['releaseDate']
thumbnailPUMA1 = data[0]['thumbnail']

shoe_namePUMA2 = data[1]['shoeName']
colorwayPUMA2 = data[1]['colorway']
retailPricePUMA2 = data[1]['retailPrice']
releaseDatePUMA2 = data[1]['releaseDate']
thumbnailPUMA2 = data[1]['thumbnail']

shoe_namePUMA3 = data[2]['shoeName']
colorwayPUMA3 = data[2]['colorway']
retailPricePUMA3 = data[2]['retailPrice']
releaseDatePUMA3 = data[2]['releaseDate']
thumbnailPUMA3 = data[2]['thumbnail']

shoe_namePUMA4 = data[3]['shoeName']
colorwayPUMA4 = data[3]['colorway']
retailPricePUMA4 = data[3]['retailPrice']
releaseDatePUMA4 = data[3]['releaseDate']
thumbnailPUMA4 = data[3]['thumbnail']

shoe_namePUMA5 = data[4]['shoeName']
colorwayPUMA5 = data[4]['colorway']
retailPricePUMA5 = data[4]['retailPrice']
releaseDatePUMA5 = data[4]['releaseDate']
thumbnailPUMA5 = data[4]['thumbnail']

shoe_namePUMA6 = data[5]['shoeName']
colorwayPUMA6 = data[5]['colorway']
retailPricePUMA6 = data[5]['retailPrice']
releaseDatePUMA6 = data[5]['releaseDate']
thumbnailPUMA6 = data[5]['thumbnail']

shoe_namePUMA7 = data[6]['shoeName']
colorwayPUMA7 = data[6]['colorway']
retailPricePUMA7 = data[6]['retailPrice']
releaseDatePUMA7 = data[6]['releaseDate']
thumbnailPUMA7 = data[6]['thumbnail']


shoe_namePUMA8 = data[7]['shoeName']
colorwayPUMA8 = data[7]['colorway']
retailPricePUMA8 = data[7]['retailPrice']
releaseDatePUMA8 = data[7]['releaseDate']
thumbnailPUMA8 = data[7]['thumbnail']


shoe_namePUMA9 = data[8]['shoeName']
colorwayPUMA9 = data[8]['colorway']
retailPricePUMA9 = data[8]['retailPrice']
releaseDatePUMA9 = data[8]['releaseDate']
thumbnailPUMA9 = data[8]['thumbnail']

shoe_namePUMA10 = data[9]['shoeName']
colorwayPUMA10 = data[9]['colorway']
retailPricePUMA10 = data[9]['retailPrice']
releaseDatePUMA10 = data[9]['releaseDate']
thumbnailPUMA10 = data[9]['thumbnail']