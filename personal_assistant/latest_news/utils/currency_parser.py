import requests
from bs4 import BeautifulSoup

currency_url = "https://kurs.com.ua/#main_table"
news_url = "#"


def get_currency(url):
    response = requests.get(url)
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, 'html.parser')
        table = bs.find(id="main_table")
        rows = table.find_all(class=" ")


if __name__ == "__main__":
    get_currency(currency_url)
