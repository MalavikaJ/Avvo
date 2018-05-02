import scrapy

class Accord(scrapy.Spider):
   name = "accord"
   start_urls=['https://www.avvo.com/all-lawyers/ny/new_york.html',]
   
   def parse(self, response):
      for place in response.css('ol.unstyled-list'):
         yield{'Place':place.xpath('//li[@class = "u-margin-bottom-half"]/a/text()').extract_first()}

      next_page = response.css('li.u-margin-bottom-half a::attr("href")').extract_first()
      print("URL=",next_page)
      if next_page is not None:
         yield response.follow(next_page,self.print_results)
         print("success"),
         
   def print_results(self,response):
      for result in response.css('h1.u-margin-top-0'):
         yield {'Results':result.xpath('//span[@class="text-muted u-font-size-large"]/text()').extract_first()}
      for req in self.accord_lawyers(response):
         yield from self.accord_lawyers(response)

            
   def accord_lawyers(self,response):
      for name in response.css('div.col-xs-8'):
         yield {'Lawyer_name':name.xpath('//a[@class="v-serp-block-link"]/strong/text()').extract()}
   
      next_page_url = response.css('li.pagination-next a::attr(href)').extract_first()
      print("URL=",next_page_url)
      if next_page_url is not None:
         print("URL=",next_page_url)
         next_page_url = response.urljoin(next_page_url)    
         yield scrapy.Request(next_page_url, callback=self.accord_lawyers)
     
