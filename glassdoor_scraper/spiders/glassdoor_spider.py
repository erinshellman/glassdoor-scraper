from scrapy.spider import Spider
from scrapy.selector import Selector
from glassdoor_scraper.items import GlassdoorItem

class GlassdoorSpider(Spider):
  name = "glassdoor"
  allowed_domains = ["glassdoor.com"]
  start_urls = [
    "http://www.glassdoor.com/Salaries/data-scientist-salary-SRCH_KO0,14.htm",
    "http://www.glassdoor.com/Salaries/data-engineer-salary-SRCH_KO0,13.htm"
    #"http://www.glassdoor.com/Salaries/software-developer-salary-SRCH_KO0,18.htm",
    #"http://www.glassdoor.com/Salaries/software-engineer-salary-SRCH_KO0,17.htm",
    #"http://www.glassdoor.com/Salaries/programmer-salary-SRCH_KO0,10.htm"
  ]

  def parse(self, response):
    sel = Selector(response)
    sites = sel.xpath('//ul/li')
    items = []

    for site in sites:
      item = GlassdoorItem()
      item['title'] = site.xpath('a/text()').extract()
      item['link'] = site.xpath('a/@href').extract()
      item['desc'] = site.xpath('text()').extract()
      items.append(item)

    return items

