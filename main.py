import requests
import scraper as sc
import lxml.html


class Scraping:

    def __init__(self):
        self.default_url = 'https://www.justdial.com/Chennai/Restaurants-in-Ambattur/page-'
        self.links = []
        self.names = []

    def get_links(self):
        for number in range(1, 11):
            self.url = self.default_url+str(number)
            self.source = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
            self.tree = lxml.html.fromstring(self.source.content)
            self.links += sc.get_href(self.tree.xpath('//ul[@class="rsl col-md-12 padding0"]/li//span[@class="jcn"]/a[@href]'))
            print(self.links)

    def get_data(self):
        for link in self.links:
            self.source = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
            self.tree = lxml.html.fromstring(self.source.content)
            self.name = self.tree.xpath('//h1[@class="rstotle"]/span/span/text()')
            self.names.append(self.name)
        print(self.names)
        sc.Excel(['name']).excel(self.names)


Scraping = Scraping()
Scraping.get_links()
Scraping.get_data()