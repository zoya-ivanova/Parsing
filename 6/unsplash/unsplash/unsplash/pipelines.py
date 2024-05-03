
import hashlib
from scrapy.pipelines.images import ImagesPipeline

class CustomImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(request.url.encode()).hexdigest()
        item['relative_path'] = f"images/{item['title']}-{image_guid}.jpg"
        return f"{item['title']}-{image_guid}.jpg"