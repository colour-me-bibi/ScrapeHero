import scrapy
from ScrapeHero import constant

class ChorusSpider(scrapy.Spider):
    name = 'chorus-spider'
    start_urls = [constant.CHORUS_URL]

    def parse(self, response):
        songs = response.xpath("//div[@class='Song']").extract()

        yield {
            'songs': songs
        }
