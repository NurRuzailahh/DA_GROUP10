import scrapy

class NewSpider(scrapy.Spider):
  name = "new_spider"
  start_urls = ['https://brickset.com/sets/year-2009']

  def parse(self,response):
   xpath_selector = '//img'
   for x in response.xpath(xpath_selector):
     newsel = '@src'
     yield {
       'Image Link':x.xpath(newsel).extract_first()
     }