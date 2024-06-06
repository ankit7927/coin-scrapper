from celery import shared_task
from .scraper import CoinMarketCapScraper
import time

@shared_task
def scrape_coin_data(coin_acronyms):
    time.sleep(30)
    # scraper = CoinMarketCapScraper()
    # results = []
    # for coin in coin_acronyms:
    #     data = scraper.get_coin_data(coin)
    #     results.append({"coin": coin, "output": data})
    # scraper.close()
    return {"resutl": "result"}


@shared_task
def create_task():
    time.sleep(10)
    return True