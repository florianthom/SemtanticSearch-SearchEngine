# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from policecrawler.items import ReportItem
from urllib.parse import urljoin


class ReportsSpider(scrapy.Spider):
    name = 'reports'
    allowed_domains = ['polizei.brandenburg.de']
    start_urls = ['https://polizei.brandenburg.de/suche/typ/null/kategorie/null/1',
                  'https://polizei.brandenburg.de/suche/typ/null/kategorie/null/2',
                  'https://polizei.brandenburg.de/suche/typ/null/kategorie/null/3',
                  ]


    def parse(self, response):
        links = response.xpath("//h4/a/@href").extract()
        url = 'https://polizei.brandenburg.de'
    
        for report in links:
            yield response.follow(url + report, self.detailParse)
    
        next_page = response.xpath("//a[@class='pbb-nobg']/@href")
    
        for page in next_page:
            yield response.follow(page, self.parse)
    
    
    def detailParse(self, response):
        for report in response.xpath("//article[@id='pbb-article']"):
            lo = ItemLoader(item=ReportItem(), selector=report)
            lo.add_xpath('date', "//dd[@data-iw-widget]", re='(\d+\.\d+\.\d+)')
            lo.add_xpath('title', "//h1[@class='pbb-mainheadline']")
            lo.add_xpath('location', "//p[@class='pbb-ort']")
            lo.add_xpath('text', "//div[@class='pbb-article-text']/p")
            lo.add_xpath('number', "/html/head/meta[5]", re='(\d+)')
            yield lo.load_item()

