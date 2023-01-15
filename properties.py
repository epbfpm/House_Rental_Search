from bs4 import BeautifulSoup as Bs
import requests

zillo = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.51506972346323%2C%22east%22%3A-122.39130187068002%2C%22south%22%3A37.72955283506448%2C%22north%22%3A37.81463065438208%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A607185%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22sche%22%3A%7B%22value%22%3Afalse%7D%2C%22schm%22%3A%7B%22value%22%3Afalse%7D%2C%22schh%22%3A%7B%22value%22%3Afalse%7D%2C%22schp%22%3A%7B%22value%22%3Afalse%7D%2C%22schr%22%3A%7B%22value%22%3Afalse%7D%2C%22schc%22%3A%7B%22value%22%3Afalse%7D%2C%22schu%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept-language': 'en-GB,en;q=0.9,pt;q=0.8'
}


# =================== get the site data =================== #
class Zillo():
    def __init__(self):
        self.addresses = {}

    def get_entries(self):
        html = requests.get(zillo, headers=header).text
        soup = Bs(html, 'html.parser')
        address = soup.select('address')
        price = soup.select('.hRqIYX')
        link = soup.select('.property-card-link')
        link_correct = []
        for i in link:
            if 'http' not in i['href']:
                link_correct.append(f'https://www.zillow.com{i["href"]}')
        self.addresses = {i: {'address': address[i].text, 'price': price[i].text, 'link': link_correct[i]} for i in range(0, len(address))}
        return self.addresses
