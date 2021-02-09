import scrapy

class Scrapy_hub_spider(scrapy.Spider):
    name = 'scrapy_hub'
    def start_requests(self):
        return [scrapy.Request(url = "https://blog.scrapinghub.com", callback = self.parse)]

    def parse(self, response):
        titles = response.css("div.post-listing div.post-item div.post-header h2 a::text").getall()
        dates = response.css("div.post-item div.post-header div.byline span.date a::text").getall()
        count = 0
        while (count < len(titles)):
            yield {"title": titles[count], "date":dates[count]}
            count += 1


