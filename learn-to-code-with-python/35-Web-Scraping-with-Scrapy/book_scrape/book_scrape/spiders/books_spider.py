import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'
    def start_requests(self):
        return [scrapy.Request(url = "http://books.toscrape.com", callback = self.parse)]

    def parse(self, response):
        titles = response.css("article.product_pod h3 a::attr(title)").getall()
        prices = response.css("article.product_pod div.product_price p.price_color::text").getall()   
        for title in titles:
            print({"title": title, "price":prices})


