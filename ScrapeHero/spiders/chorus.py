import scrapy
from ScrapeHero import constant

class ChorusSpider(scrapy.Spider):
    name = 'chorus-spider'
    start_urls = [constant.CHORUS_URL]

    def parse(self, response):
        songs = response.xpath(f"//div[@class='{constant.SONG_DIV_CLASS}']").extract()

        for song in songs:
            yield {
                'song': song
            }

