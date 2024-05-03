import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from itemloaders.processors import MapCompose
from ..items import UnsplashItem
from urllib.parse import urljoin


class UnsplashImgsSpider(CrawlSpider):
    name = "unsplash_imgs"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='h9Kv0']/ul//li/a"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@itemprop='contentUrl']"), callback="parse_img_page", follow=False),
    )

    def parse_img_page(self, response):
        loader = ItemLoader(item=UnsplashItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)

        title = response.xpath("//h1/text()").get()
        loader.add_value("title", title)

        publication_date = response.xpath("//time/@title").get()
        loader.add_value("publication_date", publication_date)

        author = response.xpath("//a[@class='BkSVh FEdrY SfGU7 ZR5jm jQEvX ZR5jm']/text()").get()
        loader.add_value("author", author)

        # categories_list = response.xpath('//span[@class="jmdKh"]//a/text()').getall()
        # category = response.xpath('//div[@class="zDHt2 N9mmz"]/text()').getall()
        # loader.add_value("category", category)
        
        # if not categories_list:
        #     categories_list = response.xpath('//span[@class="gS_hS ZR5jm"]//a/text()').getall()
        # category = " ".join(categories_list)
        # loader.add_value("category", category)

        # url = response.xpath('//div[@class="fwf5M"]//img[@class="ApbSI vkrMA"]/@src').get()
        url = response.xpath('//div[@class="ac7XH"]//img[@class="ApbSI vkrMA"]/@src').get()
        loader.add_value("image_urls", [url])

        yield loader.load_item()
