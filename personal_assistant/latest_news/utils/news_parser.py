import datetime

import requests
from bs4 import BeautifulSoup

from latest_news.models import News

date = datetime.date.today()
month = ("0" + date.month.__str__())[len("0" + date.month.__str__()) - 2::]
day = ("0" + (date.day).__str__())[len("0" + date.day.__str__()) - 2::]

news_url = f"https://podrobnosti.ua/archive/important/{date.year}/{month}/{day}/all/all/page"
base_url = "https://podrobnosti.ua"


# class New:
#     img_link = None
#     title = None
#     date = None
#     fulltext = None


def get_news(url, page):
    response = requests.get(url + str(page))
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, 'html.parser')
        table = bs.find(class_="news-list news-table")
        rows = table.find_all("li")
        if rows:
            for row in rows:
                new = News()
                new.fulltext, new.img_url = get_new_detail(base_url + row.find("a")["href"])
                det = row.find('div', class_="info")
                new.title = det.find("span").text
                new.date = det.find("em").text
                new.save()
                # print(new.title)
            get_news(url, page + 1)


def get_new_detail(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, 'html.parser')
        article = bs.find("div", id="article_content")
        img = bs.find(class_="article_picture")["src"]
        return article.text, base_url + img

def delete_news():
    forex = News.objects.all()
    forex.delete()


# if __name__ == "__main__":
#     get_news(news_url, 1)
