# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class GlassdoorItem(Item):
    job_title = Field()
    salary = Field()
    bonus_salary = Field()
    company = Field()
    city = Field()
    state = Field()
    pass
