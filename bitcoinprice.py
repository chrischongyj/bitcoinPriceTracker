import requests
from bs4 import BeautifulSoup

link = "https://coinmarketcap.com/currencies/bitcoin/"

header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}

data = requests.get(headers = header, url = link)

soup = BeautifulSoup(data.content, 'html.parser')

bitcoinPrice = soup.find(id="data-currency-value")

print(bitcoinPrice)