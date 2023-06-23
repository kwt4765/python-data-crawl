import requests
from bs4 import BeautifulSoup

for Stocks in [("225570","넥슨 게임즈"),("036570", "NC소프트"),("251270", "넷마블")] : 
    url = f"https://finance.naver.com/item/sise.naver?code={Stocks[0]}"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    price = soup.select_one("strong#_nowVal.tah.p11")
    print(Stocks[1] + "의 가격은 : ", end="")
    print(price.text)