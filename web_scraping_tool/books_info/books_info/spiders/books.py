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
        writer.writerow(["Book name","Book price"])
        for child in response.xpath('//article'):
            try:
                book_name = child.xpath('//img/@alt/text()').extract()
                book_price = child.xpath('//article//p[@class = "price_color"]/text()').extract()
                writer.writerow([book_name,book_price])
            except IndexError:
                pass
        cvs_file.close()


