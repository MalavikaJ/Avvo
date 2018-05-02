import scrapy


class Places(scrapy.Spider):
    name = "location"
    start_urls = [
        'https://www.avvo.com/all-lawyers/ny/new_york.html',
    ]

    def parse(self, response):
        for place in response.css('ol.unstyled-list'):
            yield {
                  
                 'Place':response.xpath('//li[@class = "u-margin-bottom-half"]/a/text()').extract() 


                  }

       

