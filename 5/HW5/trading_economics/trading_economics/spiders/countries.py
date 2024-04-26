import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["tradingeconomics.com"]
    start_urls = ["http://tradingeconomics.com/"]

    def parse(self, response):
        pass
