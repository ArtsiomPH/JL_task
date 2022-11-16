# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JlTaskPipeline:
    COUNTER = 0

    def process_item(self, item, spider):
        self.COUNTER += 1
        if self.COUNTER <= 100:
            return item
