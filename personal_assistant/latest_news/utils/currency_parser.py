import requests
from bs4 import BeautifulSoup

# from personal_assistant.latest_news.models import Forex

currency_url = "https://kurs.com.ua/#main_table"
news_url = "#"


class Forex():
    currency = None
    buy = None
    sell = None

    def __str__(self):
        return f' {self.currency}; {self.buy}; {self.sell} '


def get_currency(url):
    response = requests.get(url)
    currency_list = list()
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, 'html.parser')
        table = bs.find(id="main_table")
        table = table.find(class_="text-right")
        rows = table.find_all("tr")
        # print(rows)
        for row in rows:
            tds = row.find_all("td")
            # print(tds)
            for index, td in enumerate(tds):
                forex = Forex()
                print(index)
                match index:
                    case 0:
                        print(td.find_next("a").text)
                        forex.currency = td.find_next("a").text
                    case 1:
                        print(td.find_next("div", class_="course").text)
                        forex.buy = td.find_next("div", class_="course").text
                    case 2:
                        print(td.find_next("div", class_="course").text)
                        forex.sell = td.find("div", class_="course").text
                    case _:
                        pass
                currency_list.append(forex)
        for el in currency_list:
            print(el)


if __name__ == "__main__":
    get_currency(currency_url)
