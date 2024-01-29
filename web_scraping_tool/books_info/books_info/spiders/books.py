import scrapy
import os
from os.path import dirname
import csv

current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir,'index.html')

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    # start_urls = ["https://books.toscrape.com"]
    start_urls = [f"file://{url}"]

    def parse(self, response):
        cvs_file = open('books_name_price.csv','w')
        writer = csv.writer(cvs_file)
        writer.writerow(['Book name','Book price'])
        i = 0
        for child in response.xpath('//article'):
            try:
                book_names = child.xpath('//a//img/@alt')[i].extract()
                book_prices = child.xpath('//p[@class = "price_color"]/text()')[i].extract()
                writer.writerow([book_names,book_prices])
                i += 1
            except IndexError:
                pass
        cvs_file.close()


