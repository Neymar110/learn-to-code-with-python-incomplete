import json
file = open('C:/Users/ADMIN/Documents/learn-to-code-with-python-incomplete/learn-to-code-with-python/31-Web-Scraping-with-Scrapy/book_scrape/book_scrape/Json_file_scrapy_hub.json',)

data = json.load(file)

for item in data:
    for key, value in item.items():
        print(key, value)
