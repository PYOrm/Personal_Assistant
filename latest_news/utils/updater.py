from latest_news.utils.currency_parser import get_currency, delete_currency, currency_url
from latest_news.utils.news_parser import get_news, delete_news, news_url
from background_task import background
import time 

@background()
def run_parsers():
    delete_currency()
    delete_news()
    get_news(news_url, 1)
    get_currency(currency_url)

