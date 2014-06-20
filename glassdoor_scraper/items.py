from scrapy.item import Item, Field

class GlassdoorItem(Item):
    title = Field()
    link = Field()
    desc = Field()
    pass
