# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from PoliceReports.items import ReportItem


class ReportsSpider(scrapy.Spider):
    name = 'reports'
    allowed_domains = ['berlin.de']
    start_urls = ['https://www.berlin.de/polizei/polizeimeldungen/archiv/2018/',
                  'https://www.berlin.de/polizei/polizeimeldungen/archiv/2017/',
                  'https://www.berlin.de/polizei/polizeimeldungen/archiv/2016/',
                  'https://www.berlin.de/polizei/polizeimeldungen/archiv/2015/',
                  'https://www.berlin.de/polizei/polizeimeldungen/archiv/2014/',
                  ]

    def parse(self, response):
        links = response.xpath('//ul[@class="list-autoteaser"]/li[@class="row-fluid"]/div[2]/a/@href').extract()

        i = 1
        for link in links:
            abs_url = response.urljoin(link)

            if i <= len(links):
                i = i + 1
            yield scrapy.Request(abs_url, callback=self.parse_indetail)

        next_page = response.css('li.pager-item-next a::attr(href)').extract_first().split('/')[5]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_indetail(self, response):
        for report in response.xpath("//div[@class='span7 column-content']"):
            lo = ItemLoader(item=ReportItem(), selector=report)
            lo.add_xpath('date', "//div[@class='html5-section body']", re='(\d+\.\d+\.\d+)')
            lo.add_xpath('title', "//h1[@class='title']")
            lo.add_xpath('location', "//div[@class='polizeimeldung'][2]")
            lo.add_xpath('text', "//div[@class='textile']/p")
            lo.add_xpath('number', "//div[@class='html5-section body']")
            yield lo.load_item()

