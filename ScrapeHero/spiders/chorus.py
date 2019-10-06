import scrapy

class ChorusSpider(scrapy.Spider):
    name = 'chorus-spider'
    start_urls = ['https://chorus.fightthe.pw/']

    def parse(self, response):
        title = response.xpath('//title/text()').extract()

        yield {
            'title': title
        }
