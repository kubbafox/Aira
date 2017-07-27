import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "flyer"

    def start_requests(self):
        urls = [
            'http://www.flyertalk.com/forum/credit-card-programs/1463793-barclays-usa-lufthansa-mastercard-revived-50k-after-5k-spend-1.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for message in response.css('div.page'):
            yield {
                'author': message.css('a.bigusername::text').extract_first(),
                'postDate': re.sub('\r|\n|\t|<.*?>', '', message.css('td.thead:nth-child(1)').extract_first()),
                'text': re.sub('\r|\n|\t|<.*?>', '', message.css('td.alt1 > div').extract_first())
            }