import scrapy 


class NewsTitleSpider(scrapy.Spider):  
     name = "NewsTitleSpider"
     start_urls = ['https://books.toscrape.com/']

     def parse(self, response):
        titles = response.css('h1::text').getall() 
        for title in titles:
            yield {'title': title}

                       
        #Salvarli in un file json:
        #with open('titles.json', 'w') as f:
            #f.write('\n'.join(titles))

        # Salvarli in un file CSV:
        #with open('titles.csv', 'w') as f:
            #f.write('Title\n')
            #for title in titles:
                # f.write(f'{title}\n')    
            
   
  
