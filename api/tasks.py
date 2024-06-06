from celery import shared_task
from .scraper import CoinMarketCapScraper

@shared_task
def scrape_coin_data(coin_acronyms):
    scraper = CoinMarketCapScraper()
    results = []
    for coin in coin_acronyms:
        data = scraper.get_coin_data(coin)
        results.append({"coin": coin, "output": data})
    scraper.close()
    return results
