import datetime

import requests
from bs4 import BeautifulSoup

# from personal_assistant.latest_news.models import Forex
date = datetime.date.today()
month = ("0" + date.month.__str__())[len("0" + date.month.__str__())-2::]
day = ("0" + date.day.__str__())[len("0" + date.day.__str__())-2::]
print(month)
print(day)
page = 1
news_url = f"https://podrobnosti.ua/archive/important/{date.year}/{month}/{day}/all/all/page{page}"


class Forex:
    currency = None
    buy = None
    sell = None

    def __str__(self):
        return f' {self.currency}; {self.buy}; {self.sell} '


def get_currency(url) -> list[Forex]:
    response = requests.get(url)
    currency_list = list()
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
            currency_list.append(forex)
    return currency_list


if __name__ == "__main__":
    get_currency(news_url)
