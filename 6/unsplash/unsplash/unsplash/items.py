
import scrapy

class UnsplashItem(scrapy.Item):
    title = scrapy.Field()
    publication_date = scrapy.Field()
    author = scrapy.Field()
    # category = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    relative_path = scrapy.Field()
