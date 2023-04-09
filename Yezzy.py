import http.client
import json

conn = http.client.HTTPSConnection("sneaker-database-stockx.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "insert  your key "
    'X-RapidAPI-Host': "sneaker-database-stockx.p.rapidapi.com"
    }

conn.request("GET", "/getproducts?keywords=Yeezy&limit=10", headers=headers)

res = conn.getresponse()
data = res.read()

data = json.loads(data.decode("utf-8"))

shoe_nameyezzy1 = data[0]['shoeName']
colorwayyeezy1 = data[0]['colorway']
retailPriceyeezy1 = data[0]['retailPrice']
releaseDateyeezy1 = data[0]['releaseDate']
thumbnailyezzy1 = data[0]['thumbnail']


shoe_nameyezzy2 = data[1]['shoeName']
colorwayyeezy2 = data[1]['colorway']
retailPriceyeezy2 = data[1]['retailPrice']
releaseDateyeezy2 = data[1]['releaseDate']
thumbnailyezzy2 = data[1]['thumbnail']

shoe_nameyezzy3 = data[2]['shoeName']
colorwayyeezy3 = data[2]['colorway']
retailPriceyeezy3 = data[2]['retailPrice']
releaseDateyeezy3 = data[2]['releaseDate']
thumbnailyezzy3 = data[2]['thumbnail']

shoe_nameyezzy4 = data[3]['shoeName']
colorwayyeezy4 = data[3]['colorway']
retailPriceyeezy4 = data[3]['retailPrice']
releaseDateyeezy4 = data[3]['releaseDate']
thumbnailyezzy4 = data[3]['thumbnail']

shoe_nameyezzy5 = data[4]['shoeName']
colorwayyeezy5 = data[4]['colorway']
retailPriceyeezy5 = data[4]['retailPrice']
releaseDateyeezy5 = data[4]['releaseDate']
thumbnailyezzy5 = data[4]['thumbnail']

shoe_nameyezzy6 = data[5]['shoeName']
colorwayyeezy6 = data[5]['colorway']
retailPriceyeezy6 = data[5]['retailPrice']
releaseDateyeezy6 = data[5]['releaseDate']
thumbnailyezzy6 = data[5]['thumbnail']

shoe_nameyezzy7 = data[6]['shoeName']
colorwayyeezy7 = data[6]['colorway']
retailPriceyeezy7 = data[6]['retailPrice']
releaseDateyeezy7 = data[6]['releaseDate']
thumbnailyezzy7 = data[6]['thumbnail']


shoe_nameyezzy8 = data[7]['shoeName']
colorwayyeezy8 = data[7]['colorway']
retailPriceyeezy8 = data[7]['retailPrice']
releaseDateyeezy8 = data[7]['releaseDate']
thumbnailyezzy8 = data[7]['thumbnail']


shoe_nameyezzy9 = data[8]['shoeName']
colorwayyeezy9 = data[8]['colorway']
retailPriceyeezy9 = data[8]['retailPrice']
releaseDateyeezy9 = data[8]['releaseDate']
thumbnailyezzy9 = data[8]['thumbnail']

shoe_nameyezzy10 = data[9]['shoeName']
colorwayyeezy10 = data[9]['colorway']
retailPriceyeezy10 = data[9]['retailPrice']
releaseDateyeezy10 = data[9]['releaseDate']
thumbnailyezzy10 = data[9]['thumbnail']