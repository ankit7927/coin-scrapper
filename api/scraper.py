
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CoinMarketCapScraper:
    def __init__(self):
        self.base_url = 'https://coinmarketcap.com/currencies/'
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        #options.set_capability("proxy", self.get_proxy_data())
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        

    def get_coin_data(self, coin_acronym):
        url = f"{self.base_url}{coin_acronym}/"

        self.driver.delete_network_conditions()
        self.driver.delete_all_cookies()
        
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)
        self.coin_state_section = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-module-name='Coin-stats' and @class='sc-4c05d6ef-0 sc-55349342-0 dlQYLv gELPTu coin-stats']")))

        ranks = self.get_rank()

        statics = self.get_statics_value()

        link_data = self.get_links()

        data = {
            "price": self.get_element_text(By.XPATH, './/span[@class="sc-d1ede7e3-0 fsQm base-text"]'),
            "price_change": statics[0].split("\n")[0],
            "market_cap_rank": ranks[0],
            "volume_rank": ranks[1],

            "market_cap": statics[0].split("\n")[1],
            "volume": statics[1].split("\n")[1],
            "volume_market_cap": statics[2],
            "circulating_supply":statics[3],
            "total_supply":statics[4],
            "diluted_market_cap": statics[6],
            "contracts": link_data[0],
            "website": link_data[1],
            "socials":link_data[2]
        }
        return data

    def get_element_text(self, by, value):
        try:
            element = self.coin_state_section.find_element(by, value)
            return element.text
        except Exception:
            return None
        
    def get_statics_value(self):
        eles = self.coin_state_section.find_elements(by=By.XPATH, value='.//dd[@class="sc-d1ede7e3-0 hPHvUM base-text"]')
        return [ele.text for ele in eles]
    
    def get_rank(self):
        eles = self.coin_state_section.find_elements(by=By.XPATH, value='.//span[@class="text slider-value rank-value"]')

        return [ele.text for ele in eles]
    
    def get_links(self):
        eles = self.coin_state_section.find_elements(by=By.XPATH, value=".//div[@class='sc-d1ede7e3-0 sc-7f0f401-2 bwRagp kXjUeJ']")[:3]
        contracts = []
        weblink = []
        socials = []

        for con in eles[0].find_elements(by=By.TAG_NAME, value="a"):
            contracts.append({
                "name": con.text.split("\n")[0],
                "address": con.get_attribute("href").split("/")[-1]
            })

        for soc in eles[1].find_elements(by=By.TAG_NAME, value="a"):
            weblink.append({
                "name": soc.text,
                "link": soc.get_attribute("href")
            })

        for soc in eles[2].find_elements(by=By.TAG_NAME, value="a"):
            socials.append({
                "name": soc.text,
                "link": soc.get_attribute("href")
            })
        return contracts, weblink, socials
        
    def get_proxy_data():
        proxy = "http://ankitproxy:ankit@PROXYMESH@us-ca.proxymesh.com:31280"
        return {
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy,
            "noProxy": None,
            "proxyType": "manual"
        }


    def close(self):
        self.driver.quit()


scraper = CoinMarketCapScraper()
results = []
for coin in ["dogecoin", "shiba-inu"]:
    data = scraper.get_coin_data(coin.lower())
    results.append({"coin": coin, "output": data})
scraper.close()


print(results)