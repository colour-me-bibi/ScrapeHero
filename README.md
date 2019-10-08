# ScrapeHero
Scrape and download Clone Hero charts from chorus.fightthe.pw

I use it to continuously push information of song charts from the website [Chorus](https://chorus.fightthe.pw/) into a MongoDB database. The database I'm using has a unique index for each song's md5 checksum hash to avoid inserting duplicates. This webscraper has two spiders, one which scrapes the latest songs and the other which scrapes random songs.
