import requests
from bs4 import BeautifulSoup

from latest_news.models import Forex

currency_url = "https://kurs.com.ua/#main_table"


def get_currency(url):
    response = requests.get(url)
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, 'html.parser')
        table = bs.find(id="main_table")
        table = table.find(class_="text-right")
        rows = table.find_all("tr")
        for row in rows:
            tds = row.find_all("td")
            forex = Forex()
            for index, td in enumerate(tds):
                match index:
                    case 0:
                        forex.currency = td.find_next("a").text
                    case 1:
                        forex.buy = td.find_next("div", class_="course").text.split()[0]
                    case 2:
                        forex.sell = td.find("div", class_="course").text.split()[0]
                    case _:
                        pass
            forex.save()


def delete_currency():
    forex = Forex.objects.all()
    forex.delete()

#
# if __name__ == "__main__":
#     get_currency(currency_url)
