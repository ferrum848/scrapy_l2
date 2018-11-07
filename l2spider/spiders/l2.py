import scrapy
from l2spider.items import L2SpiderItem
class BrickSetSpider(scrapy.Spider):
	name = "l2spider"
	start_urls = ['https://kanobu.ru/games/lineage-ii/screenshots/']
	def parse(self, response):
		NAME_SELECTOR = 'h1 ::text'
		EML_SELECTOR = 'div.gameContent a'

		test = 'a ::attr(rel)'
		yield {'my_test': response.css(test).extract_first()}
		
		next_page = 'div.holder li:nth-of-type(4) a ::attr(href)'
		yield {'next_page': response.css(next_page).extract_first()}
		page = 'https://kanobu.ru' + response.css(next_page).extract_first()

		yield scrapy.Request(page, self.parse_next)

		#next = 'div.holder a'
		#for j in response.css(next):
		#	yield {'next': j.css('a ::attr(href)').extract_first()}

		text = response.css(NAME_SELECTOR).extract_first()
		yield {'l2': text}

		for i in response.css(EML_SELECTOR):
			TEST = 'a ::attr(href)'
			link = i.css(TEST).extract_first()

			yield L2SpiderItem(file_urls=[link])

	def parse_next(self, response):
		for k in response.css('div.news-block img'):
			link = k.css('img ::attr(src)').extract_first()
			#yield {'next_imgs': link}
			yield L2SpiderItem(file_urls=[link])



