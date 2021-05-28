import scrapy
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import urljoin
from itemadapter import ItemAdapter
import requests

class webnovel(scrapy.Spider):
    name = "novel"
    url = "https://www.worldnovel.online/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = bs(html, "html.parser")

    soup.find_all("url")
    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def Recently(soup):
        return soup.find("a", text="Recently Added Chapters")
    
    def extract_links(soup):
        return [a['title'] for a in soup.select("#mw-pages li a")]
    
    with requests.Session() as session:
        content = session.get(url).content
        soup = bs(content, 'lxml')

        links = extract_links(soup)
        next_link = Recently(soup)

    while next_link is not None:  # while there is a Next Page link
        url = urljoin(url, next_link['href'])
        content = session.get(url).content
        soup = bs(content, 'lxml')
        links += extract_links(soup)
        next_link = Recently(soup)
        print(links)