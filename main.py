import discord
import http.client
import json
from Yeezy import *
from new import *
from Puma import *
from NIKE import *

intents = discord.Intents.default()
intents.typing = False
intents.presences = False


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author == self.user:
            return
        if "!1jordan" in message.content:
            shoe_name = data[0]['shoeName']
            colorway = data[0]['colorway']
            retailPrice = data[0]['retailPrice']
            releaseDate = data[0]['releaseDate']
            thumbnail = data[0]['thumbnail']

            await message.channel.send(f' {thumbnail}\n')
            await message.channel.send(f' {shoe_name} ')
            await message.channel.send(f'Colorway: {colorway}\n')
            await message.channel.send(f'Price: ${retailPrice}\n')
            await message.channel.send(f'Release:{releaseDate}\n')
        if "!jordan2" in message.content:
            shoe_name = data[1]['shoeName']
            colorway = data[1]['colorway']
            retailPrice = data[1]['retailPrice']
            releaseDate = data[1]['releaseDate']
            thumbnail = data[1]['thumbnail']

            await message.channel.send(f' {thumbnail}\n')
            await message.channel.send(f' {shoe_name} ')
            await message.channel.send(f'Colorway: {colorway}\n')
            await message.channel.send(f'Price: ${retailPrice}\n')
            await message.channel.send(f'Release:{releaseDate}\n')
        if "!jordan3" in message.content:
            shoe_name = data[2]['shoeName']
            colorway = data[2]['colorway']
            retailPrice = data[2]['retailPrice']
            releaseDate = data[2]['releaseDate']
            thumbnail = data[2]['thumbnail']

            await message.channel.send(f' {thumbnail}\n')
            await message.channel.send(f' {shoe_name} ')
            await message.channel.send(f'Colorway: {colorway}\n')
            await message.channel.send(f'Price: ${retailPrice}\n')
            await message.channel.send(f'Release:{releaseDate}\n')
        if "!jordan4" in message.content:
            shoe_name = data[3]['shoeName']
            colorway = data[3]['colorway']
            retailPrice = data[3]['retailPrice']
            releaseDate = data[3]['releaseDate']
            thumbnail = data[3]['thumbnail']

            await message.channel.send(f' {thumbnail}\n')
            await message.channel.send(f' {shoe_name} ')
            await message.channel.send(f'Colorway: {colorway}\n')
            await message.channel.send(f'Price: ${retailPrice}\n')
            await message.channel.send(f'Release:{releaseDate}\n')
        if "!jordan5" in message.content:
            shoe_name = data[4]['shoeName']
            colorway = data[4]['colorway']
            retailPrice = data[4]['retailPrice']
            releaseDate = data[4]['releaseDate']
            thumbnail = data[4]['thumbnail']

            await message.channel.send(f' {thumbnail}\n')
            await message.channel.send(f' {shoe_name} ')
            await message.channel.send(f'Colorway: {colorway}\n')
            await message.channel.send(f'Price: ${retailPrice}\n')
            await message.channel.send(f'Release:{releaseDate}\n')
        if "!jordan6" in message.content:
            shoe_name = data[5]['shoeName']
            colorway = data[5]['colorway']
            retailPrice = data[5]['retailPrice']
            releaseDate = data[5]['releaseDate']
            thumbnail = data[5]['thumbnail']

            await message.channel.send(f' {thumbnail}\n')
            await message.channel.send(f' {shoe_name} ')
            await message.channel.send(f'Colorway: {colorway}\n')
            await message.channel.send(f'Price: ${retailPrice}\n')
            await message.channel.send(f'Release:{releaseDate}\n')
        if "!jordan7" in message.content:
            shoe_name = data[6]['shoeName']
            colorway = data[6]['colorway']
            retailPrice = data[6]['retailPrice']
            releaseDate = data[6]['releaseDate']
            thumbnail = data[6]['thumbnail']

            await message.channel.send(f' {thumbnail}\n')
            await message.channel.send(f' {shoe_name} ')
            await message.channel.send(f'Colorway: {colorway}\n')
            await message.channel.send(f'Price: ${retailPrice}\n')
            await message.channel.send(f'Release:{releaseDate}\n')
        if "!jordan8" in message.content:
            shoe_name = data[7]['shoeName']
            colorway = data[7]['colorway']
            retailPrice = data[7]['retailPrice']
            releaseDate = data[7]['releaseDate']
            thumbnail = data[7]['thumbnail']

            await message.channel.send(f' {thumbnail}\n')
            await message.channel.send(f' {shoe_name} ')
            await message.channel.send(f'Colorway: {colorway}\n')
            await message.channel.send(f'Price: ${retailPrice}\n')
            await message.channel.send(f'Release:{releaseDate}\n')
        if "!jordan9" in message.content:
            shoe_name = data[8]['shoeName']
            colorway = data[8]['colorway']
            retailPrice = data[8]['retailPrice']
            releaseDate = data[8]['releaseDate']
            thumbnail = data[8]['thumbnail']

            await message.channel.send(f' {thumbnail}\n')
            await message.channel.send(f' {shoe_name} ')
            await message.channel.send(f'Colorway: {colorway}\n')
            await message.channel.send(f'Price: ${retailPrice}\n')
            await message.channel.send(f'Release:{releaseDate}\n')
        if "!jordan10" in message.content:
            shoe_name = data[9]['shoeName']
            colorway = data[9]['colorway']
            retailPrice = data[9]['retailPrice']
            releaseDate = data[9]['releaseDate']
            thumbnail = data[9]['thumbnail']

            await message.channel.send(f' {thumbnail}\n')
            await message.channel.send(f' {shoe_name} ')
            await message.channel.send(f'Colorway: {colorway}\n')
            await message.channel.send(f'Price: ${retailPrice}\n')
            await message.channel.send(f'Release:{releaseDate}\n')
#the code above takes the most popular jordan on stockx when you put in a comand
        if "!1yeezy" in message.content:

            await message.channel.send(f' {thumbnailyezzy1}\n')
            await message.channel.send(f' {shoe_nameyezzy1} ')
            await message.channel.send(f'Colorway: {colorwayyeezy1}\n')
            await message.channel.send(f'Price: ${retailPriceyeezy1}\n')
            await message.channel.send(f'Release:{releaseDateyeezy1}\n')
        if "!yeezy2" in message.content:

            await message.channel.send(f' {thumbnailyezzy2}\n')
            await message.channel.send(f' {shoe_nameyezzy2} ')
            await message.channel.send(f'Colorway: {colorwayyeezy2}\n')
            await message.channel.send(f'Price: ${retailPriceyeezy2}\n')
            await message.channel.send(f'Release:{releaseDateyeezy2}\n')
        if "!yeezy3" in message.content:

            await message.channel.send(f' {thumbnailyezzy3}\n')
            await message.channel.send(f' {shoe_nameyezzy3} ')
            await message.channel.send(f'Colorway: {colorwayyeezy3}\n')
            await message.channel.send(f'Price: ${retailPriceyeezy3}\n')
            await message.channel.send(f'Release:{releaseDateyeezy3}\n')
        if "!yeezy4" in message.content:
            await message.channel.send(f' {thumbnailyezzy4}\n')
            await message.channel.send(f' {shoe_nameyezzy4} ')
            await message.channel.send(f'Colorway: {colorwayyeezy4}\n')
            await message.channel.send(f'Price: ${retailPriceyeezy4}\n')
            await message.channel.send(f'Release:{releaseDateyeezy4}\n')
        if "!yeezy5" in message.content:
            await message.channel.send(f' {thumbnailyezzy5}\n')
            await message.channel.send(f' {shoe_nameyezzy5} ')
            await message.channel.send(f'Colorway: {colorwayyeezy5}\n')
            await message.channel.send(f'Price: ${retailPriceyeezy5}\n')
            await message.channel.send(f'Release:{releaseDateyeezy5}\n')
        if "!yeezy6" in message.content:
            await message.channel.send(f' {thumbnailyezzy6}\n')
            await message.channel.send(f' {shoe_nameyezzy6} ')
            await message.channel.send(f'Colorway: {colorwayyeezy6}\n')
            await message.channel.send(f'Price: ${retailPriceyeezy6}\n')
            await message.channel.send(f'Release:{releaseDateyeezy6}\n')
        if "!yeezy7" in message.content:
            await message.channel.send(f' {thumbnailyezzy7}\n')
            await message.channel.send(f' {shoe_nameyezzy7} ')
            await message.channel.send(f'Colorway: {colorwayyeezy7}\n')
            await message.channel.send(f'Price: ${retailPriceyeezy7}\n')
            await message.channel.send(f'Release:{releaseDateyeezy7}\n')
        if "!yeezy8" in message.content:
            await message.channel.send(f' {thumbnailyezzy8}\n')
            await message.channel.send(f' {shoe_nameyezzy8} ')
            await message.channel.send(f'Colorway: {colorwayyeezy8}\n')
            await message.channel.send(f'Price: ${retailPriceyeezy8}\n')
            await message.channel.send(f'Release:{releaseDateyeezy8}\n')
        if "!yeezy9" in message.content:
            await message.channel.send(f' {thumbnailyezzy9}\n')
            await message.channel.send(f' {shoe_nameyezzy9} ')
            await message.channel.send(f'Colorway: {colorwayyeezy9}\n')
            await message.channel.send(f'Price: ${retailPriceyeezy9}\n')
            await message.channel.send(f'Release:{releaseDateyeezy9}\n')
        if "!yeezy10" in message.content:
            await message.channel.send(f' {thumbnailyezzy10}\n')
            await message.channel.send(f' {shoe_nameyezzy10} ')
            await message.channel.send(f'Colorway: {colorwayyeezy10}\n')
            await message.channel.send(f'Price: ${retailPriceyeezy10}\n')
            await message.channel.send(f'Release:{releaseDateyeezy10}\n')
#the code above takes the most popular Yezzys on stockx when you put in a comand
        if "!1NEW" in message.content:
            await message.channel.send(f' {thumbnailNEW1}\n')
            await message.channel.send(f' {shoe_nameNEW1}\n')
            await message.channel.send(f'Colorway: {colorwayNEW1}\n')
            await message.channel.send(f'Price: ${retailPriceNEW1}\n')
            await message.channel.send(f'Release:{releaseDateNEW1}\n')
        if "!NEW2" in message.content:
            await message.channel.send(f' {thumbnailNEW2}\n')
            await message.channel.send(f' {shoe_nameNEW2}\n')
            await message.channel.send(f'Colorway: {colorwayNEW2}\n')
            await message.channel.send(f'Price: ${retailPriceNEW2}\n')
            await message.channel.send(f'Release:{releaseDateNEW2}\n')
        if "!NEW3" in message.content:
            await message.channel.send(f' {thumbnailNEW3}\n')
            await message.channel.send(f' {shoe_nameNEW3}\n')
            await message.channel.send(f'Colorway: {colorwayNEW3}\n')
            await message.channel.send(f'Price: ${retailPriceNEW3}\n')
            await message.channel.send(f'Release:{releaseDateNEW3}\n')
        if "!NEW4" in message.content:
            await message.channel.send(f' {thumbnailNEW4}\n')
            await message.channel.send(f' {shoe_nameNEW4}\n')
            await message.channel.send(f'Colorway: {colorwayNEW4}\n')
            await message.channel.send(f'Price: ${retailPriceNEW4}\n')
            await message.channel.send(f'Release:{releaseDateNEW4}\n')
        if "!NEW5" in message.content:
            await message.channel.send(f' {thumbnailNEW5}\n')
            await message.channel.send(f' {shoe_nameNEW5}\n')
            await message.channel.send(f'Colorway: {colorwayNEW5}\n')
            await message.channel.send(f'Price: ${retailPriceNEW5}\n')
            await message.channel.send(f'Release:{releaseDateNEW5}\n')
        if "!NEW6" in message.content:
            await message.channel.send(f' {thumbnailNEW6}\n')
            await message.channel.send(f' {shoe_nameNEW6}\n')
            await message.channel.send(f'Colorway: {colorwayNEW6}\n')
            await message.channel.send(f'Price: ${retailPriceNEW6}\n')
            await message.channel.send(f'Release:{releaseDateNEW6}\n')
        if "!NEW7" in message.content:
            await message.channel.send(f' {thumbnailNEW7}\n')
            await message.channel.send(f' {shoe_nameNEW7}\n')
            await message.channel.send(f'Colorway: {colorwayNEW7}\n')
            await message.channel.send(f'Price: ${retailPriceNEW7}\n')
            await message.channel.send(f'Release:{releaseDateNEW7}\n')
        if "!NEW8" in message.content:
            await message.channel.send(f' {thumbnailNEW8}\n')
            await message.channel.send(f' {shoe_nameNEW8}\n')
            await message.channel.send(f'Colorway: {colorwayNEW8}\n')
            await message.channel.send(f'Price: ${retailPriceNEW8}\n')
            await message.channel.send(f'Release:{releaseDateNEW8}\n')
        if "!NEW9" in message.content:
            await message.channel.send(f' {thumbnailNEW9}\n')
            await message.channel.send(f' {shoe_nameNEW9}\n')
            await message.channel.send(f'Colorway: {colorwayNEW9}\n')
            await message.channel.send(f'Price: ${retailPriceNEW9}\n')
            await message.channel.send(f'Release:{releaseDateNEW9}\n')
        if "!NEW10" in message.content:
            await message.channel.send(f' {thumbnailNEW10}\n')
            await message.channel.send(f' {shoe_nameNEW10}\n')
            await message.channel.send(f'Colorway: {colorwayNEW10}\n')
            await message.channel.send(f'Price: ${retailPriceNEW10}\n')
            await message.channel.send(f'Release:{releaseDateNEW10}\n')
#the code above takes the most popular NEWBLANCES on stockx when you put in a comand
        if "!1PUMA" in message.content:
            await message.channel.send(f' {thumbnailPUMA1}\n')
            await message.channel.send(f' {shoe_namePUMA1}\n')
            await message.channel.send(f'Colorway: {colorwayPUMA1}\n')
            await message.channel.send(f'Price: ${retailPricePUMA1}\n')
            await message.channel.send(f'Release:{releaseDatePUMA1}\n')
        if "!PUMA2" in message.content:
            await message.channel.send(f' {thumbnailPUMA2}\n')
            await message.channel.send(f' {shoe_namePUMA2}\n')
            await message.channel.send(f'Colorway: {colorwayPUMA2}\n')
            await message.channel.send(f'Price: ${retailPricePUMA2}\n')
            await message.channel.send(f'Release:{releaseDatePUMA2}\n')
        if "!PUMA3" in message.content:
            await message.channel.send(f' {thumbnailPUMA3}\n')
            await message.channel.send(f' {shoe_namePUMA3}\n')
            await message.channel.send(f'Colorway: {colorwayPUMA3}\n')
            await message.channel.send(f'Price: ${retailPricePUMA3}\n')
            await message.channel.send(f'Release:{releaseDatePUMA3}\n')
        if "!PUMA4" in message.content:
            await message.channel.send(f' {thumbnailPUMA4}\n')
            await message.channel.send(f' {shoe_namePUMA4}\n')
            await message.channel.send(f'Colorway: {colorwayPUMA4}\n')
            await message.channel.send(f'Price: ${retailPricePUMA4}\n')
            await message.channel.send(f'Release:{releaseDatePUMA4}\n')
        if "!PUMA5" in message.content:
            await message.channel.send(f' {thumbnailPUMA5}\n')
            await message.channel.send(f' {shoe_namePUMA5}\n')
            await message.channel.send(f'Colorway: {colorwayPUMA5}\n')
            await message.channel.send(f'Price: ${retailPricePUMA5}\n')
            await message.channel.send(f'Release:{releaseDatePUMA5}\n')
        if "!PUMA6" in message.content:
            await message.channel.send(f' {thumbnailPUMA6}\n')
            await message.channel.send(f' {shoe_namePUMA6}\n')
            await message.channel.send(f'Colorway: {colorwayPUMA6}\n')
            await message.channel.send(f'Price: ${retailPricePUMA6}\n')
            await message.channel.send(f'Release:{releaseDatePUMA6}\n')
        if "!PUMA7" in message.content:
            await message.channel.send(f' {thumbnailPUMA7}\n')
            await message.channel.send(f' {shoe_namePUMA7}\n')
            await message.channel.send(f'Colorway: {colorwayPUMA7}\n')
            await message.channel.send(f'Price: ${retailPricePUMA7}\n')
            await message.channel.send(f'Release:{releaseDatePUMA7}\n')
        if "!PUMA8" in message.content:
            await message.channel.send(f' {thumbnailPUMA8}\n')
            await message.channel.send(f' {shoe_namePUMA8}\n')
            await message.channel.send(f'Colorway: {colorwayPUMA8}\n')
            await message.channel.send(f'Price: ${retailPricePUMA8}\n')
            await message.channel.send(f'Release:{releaseDatePUMA8}\n')
        if "!PUMA9" in message.content:
            await message.channel.send(f' {thumbnailPUMA9}\n')
            await message.channel.send(f' {shoe_namePUMA9}\n')
            await message.channel.send(f'Colorway: {colorwayPUMA9}\n')
            await message.channel.send(f'Price: ${retailPricePUMA9}\n')
            await message.channel.send(f'Release:{releaseDatePUMA9}\n')
        if "!PUMA10" in message.content:
            await message.channel.send(f' {thumbnailPUMA10}\n')
            await message.channel.send(f' {shoe_namePUMA10}\n')
            await message.channel.send(f'Colorway: {colorwayPUMA10}\n')
            await message.channel.send(f'Price: ${retailPricePUMA10}\n')
            await message.channel.send(f'Release:{releaseDatePUMA10}\n')
# the code above takes the most popular NEWBLANCES on stockx when you put in a comand
        if "!1NIKE" in message.content:
            await message.channel.send(f' {thumbnailNIKE1}\n')
            await message.channel.send(f' {shoe_nameNIKE1}\n')
            await message.channel.send(f'Colorway: {colorwayNIKE1}\n')
            await message.channel.send(f'Price: ${retailPriceNIKE1}\n')
            await message.channel.send(f'Release:{releaseDateNIKE1}\n')
        if "!NIKE2" in message.content:
            await message.channel.send(f' {thumbnailNIKE2}\n')
            await message.channel.send(f' {shoe_nameNIKE2}\n')
            await message.channel.send(f'Colorway: {colorwayNIKE2}\n')
            await message.channel.send(f'Price: ${retailPriceNIKE2}\n')
            await message.channel.send(f'Release:{releaseDateNIKE2}\n')
        if "!NIKE3" in message.content:
            await message.channel.send(f' {thumbnailNIKE3}\n')
            await message.channel.send(f' {shoe_nameNIKE3}\n')
            await message.channel.send(f'Colorway: {colorwayNIKE3}\n')
            await message.channel.send(f'Price: ${retailPriceNIKE3}\n')
            await message.channel.send(f'Release:{releaseDateNIKE3}\n')
        if "!NIKE4" in message.content:
            await message.channel.send(f' {thumbnailNIKE4}\n')
            await message.channel.send(f' {shoe_nameNIKE4}\n')
            await message.channel.send(f'Colorway: {colorwayNIKE4}\n')
            await message.channel.send(f'Price: ${retailPriceNIKE4}\n')
            await message.channel.send(f'Release:{releaseDateNIKE4}\n')
        if "!NIKE5" in message.content:
            await message.channel.send(f' {thumbnailNIKE5}\n')
            await message.channel.send(f' {shoe_nameNIKE5}\n')
            await message.channel.send(f'Colorway: {colorwayNIKE5}\n')
            await message.channel.send(f'Price: ${retailPriceNIKE5}\n')
            await message.channel.send(f'Release:{releaseDateNIKE5}\n')
        if "!NIKE6" in message.content:
            await message.channel.send(f' {thumbnailNIKE6}\n')
            await message.channel.send(f' {shoe_nameNIKE6}\n')
            await message.channel.send(f'Colorway: {colorwayNIKE6}\n')
            await message.channel.send(f'Price: ${retailPriceNIKE6}\n')
            await message.channel.send(f'Release:{releaseDateNIKE6}\n')
        if "!NIKE7" in message.content:
            await message.channel.send(f' {thumbnailNIKE7}\n')
            await message.channel.send(f' {shoe_nameNIKE7}\n')
            await message.channel.send(f'Colorway: {colorwayNIKE7}\n')
            await message.channel.send(f'Price: ${retailPriceNIKE7}\n')
            await message.channel.send(f'Release:{releaseDateNIKE7}\n')
        if "!NIKE8" in message.content:
            await message.channel.send(f' {thumbnailNIKE8}\n')
            await message.channel.send(f' {shoe_nameNIKE8}\n')
            await message.channel.send(f'Colorway: {colorwayNIKE8}\n')
            await message.channel.send(f'Price: ${retailPriceNIKE8}\n')
            await message.channel.send(f'Release:{releaseDateNIKE8}\n')




conn = http.client.HTTPSConnection("sneaker-database-stockx.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': 
,
    'X-RapidAPI-Host': "sneaker-database-stockx.p.rapidapi.com"
    }
conn.request("GET", "/getproducts?keywords=Air%20Jordan&limit=10", headers=headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data.decode("utf-8"))


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)


client.run('discord token')

