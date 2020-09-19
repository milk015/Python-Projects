import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.ca/gp/product/B084TFH4BN?pf_rd_r=1W47VV5WS0ZV31NY205E&pf_rd_p=05326fd5-c43e-4948-99b1-a65b129fdd73'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}


def price_checker():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    itemTitle = soup.find(id="productTitle").get_text()
    itemPrice = soup.find(id="price_inside_buybox").get_text()

    priceToFloat = float(itemPrice[0:5])

    if(priceToFloat < 1.1999):
        sendAlert()

    print(itemTitle.strip())
    print(priceToFloat)

def sendAlert():
    print("Item Price has dropped!!!!")

