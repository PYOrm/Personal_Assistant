
from apscheduler.schedulers.background import BackgroundScheduler
from latest_news.utils.currency_parser import get_currency, delete_currency, currency_url
from latest_news.utils.news_parser import get_news, delete_news, news_url


def run_parsers():
    delete_currency()
    delete_news()
    get_news(news_url, 1)
    get_currency(currency_url)


def start():
    # run_parsers()
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_parsers, 'interval', minutes=1440)
    scheduler.start()
    print("1")

