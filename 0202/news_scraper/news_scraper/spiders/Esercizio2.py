import scrapy 

class TestLinkSpider(scrapy.Spider):
    name = "test_link"
    start_urls = ["https://it.wikipedia.org/wiki/Analisi_dei_dati"]
    def parse(self, response):
        links = response.css('a::attr(href)').getall()
        for link in links:
            yield {'link': link}
        #Salvarli in un file json/csv
        with open('links.json', 'w') as f:
            f.write('\n'.join(links))