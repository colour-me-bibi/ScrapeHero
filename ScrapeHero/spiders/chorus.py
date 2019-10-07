import scrapy
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ScrapeHero.items import SongItem
from ScrapeHero import constant

class ChorusSpider(scrapy.Spider):
    name = 'chorus-spider'
    start_urls = [constant.CHORUS_URL]

    # TODO click link "Gimme moar random" then parse again
    # TODO click on Random, scrape, then click more, scrape, repeat indefinitely
    # TODO implement pipeline to MongoDB database

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome(chrome_options=options)

    def parse(self, response):
        self.driver.get(response.url)

        randomLink = self.driver.find_element_by_link_text('Randomizer!')

        randomLink.click()

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//div[@class='{constant.SONG_DIV_CLASS}']"))
        )

        songs = self.driver.find_elements_by_xpath(f"//div[@class='{constant.SONG_DIV_CLASS}']")

        for song in songs:
            item = SongItem()

            item['md5_hash'] = song.find_element_by_xpath(
                "div[@class='Song__hash']").text.split(' ')[2]
            item['url'] = song.find_element_by_xpath(
                "div[@class='Song__charter']//a").get_attribute('href')

            yield item

        iterator = 0
        while iterator < 2:
            more = self.driver.find_element_by_link_text('Gimme moar random')

            try:
                more.click()

                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f"//div[@class='{constant.SONG_DIV_CLASS}']"))
                )

                songs = self.driver.find_elements_by_xpath(f"//div[@class='{constant.SONG_DIV_CLASS}']")

                for song in songs:
                    item = SongItem()
                    
                    item['md5_hash'] = song.find_element_by_xpath(
                        "div[@class='Song__hash']").text.split(' ')[2]
                    item['url'] = song.find_element_by_xpath(
                        "div[@class='Song__charter']//a").get_attribute('href')

                    yield item

                iterator = iterator + 1

            except:
                break
