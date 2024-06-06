import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class CoinMarketCapScraper:
    def __init__(self):
        self.base_url = 'https://coinmarketcap.com/currencies/'
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def get_coin_data(self, coin_acronym):
        url = f"{self.base_url}{coin_acronym}/"
        self.driver.get(url)
        data = {
            "price": self.get_element_text(By.XPATH, '//div[@class="priceValue"]'),
            "price_change": self.get_element_text(By.XPATH, '//span[@class="sc-15yy2pl-0 feeyND"]'),
            "market_cap": self.get_element_text(By.XPATH, '//div[@class="statsValue"]'),
            "market_cap_rank": self.get_element_text(By.XPATH, '//div[@class="namePillPrimary"]'),
            "volume": self.get_element_text(By.XPATH, '//div[@class="statsValue"][2]'),
            "volume_rank": self.get_element_text(By.XPATH, '//div[@class="namePillPrimary"][2]'),
            "volume_change": self.get_element_text(By.XPATH, '//span[@class="sc-15yy2pl-0 gEePkg"]'),
            "circulating_supply": self.get_element_text(By.XPATH, '//div[@class="statsValue"][3]'),
            "total_supply": self.get_element_text(By.XPATH, '//div[@class="statsValue"][4]'),
            "diluted_market_cap": self.get_element_text(By.XPATH, '//div[@class="statsValue"][5]'),
            "contracts": [
                {
                    "name": self.get_element_text(By.XPATH, '//div[@class="name"]'),
                    "address": self.get_element_text(By.XPATH, '//div[@class="address"]')
                }
            ],
            "official_links": [
                {
                    "name": "website",
                    "link": self.get_element_text(By.XPATH, '//a[@class="link-button"]')
                }
            ],
            "socials": [
                {
                    "name": "twitter",
                    "url": self.get_element_text(By.XPATH, '//a[@class="twitter"]')
                },
                {
                    "name": "telegram",
                    "url": self.get_element_text(By.XPATH, '//a[@class="telegram"]')
                }
            ]
        }
        return data

    def get_element_text(self, by, value):
        try:
            element = self.driver.find_element(by, value)
            return element.text
        except Exception:
            return None

    def close(self):
        self.driver.quit()
