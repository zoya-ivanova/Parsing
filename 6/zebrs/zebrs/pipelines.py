# import scrapy
# import hashlib
# from scrapy.pipelines.images import ImagesPipeline

# class CustomImagesPipeline(ImagesPipeline):
#     def file_path(self, request, response=None, info=None, *, item=None):
#         image_guid = hashlib.sha1(request.url.encode()).hexdigest()
#         return f"{item['name']}-{image_guid}.jpg"
from itemadapter import ItemAdapter


class ZebrsPipeline:
    def process_item(self, item, spider):
        return item
