# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from policecrawler.items import ReportItem
from urllib.parse import urljoin


class ReportsSpider(scrapy.Spider):
    name = 'reports'
    allowed_domains = ['polizei.brandenburg.de']
    start_urls = ['https://polizei.brandenburg.de/suche/typ/Meldungen/kategorie/null/1',
                  'https://polizei.brandenburg.de/suche/typ/Meldungen/kategorie/null/2',
                  'https://polizei.brandenburg.de/suche/typ/Meldungen/kategorie/null/3',
                  ]

    def parse(self, response):
        links = response.xpath(
            '//ul[@class="pbb-table-list pbb-table-list-medium pbb-locationlist pbb-searchlist"]/li/a[@class="pbb-image-container pbb-image-small"]/@href').extract()
        url = 'https://polizei.brandenburg.de'
        i = 1
        for link in links:
            # abs_url = response.urljoin(url, link)
            if i <= len(links):
                i = i + 1
            yield scrapy.Request(url+link, callback=self.detailParse)

    # next_page = response.css('li.pager-item-next a::attr(href)').extract_first().split('/')[5]

    # if next_page is not None:
    #   next_page = response.urljoin(next_page)
    #  yield scrapy.Request(next_page, callback=self.parse)

    def detailParse(self, response):
        for report in response.xpath("//article[@id='pbb-article']"):
            lo = ItemLoader(item=ReportItem(), selector=report)
            lo.add_xpath('date', "//dd[@data-iw-widget]", re='(\d+\.\d+\.\d+)')
            lo.add_xpath('title', "//h1[@class='pbb-mainheadline']")
            lo.add_xpath('location', "//p[@class='pbb-ort']")
            lo.add_xpath('text', "//div[@class='pbb-article-text']/p")
            lo.add_xpath('number', "/html/head/meta[5]", re='(\d+)')
            yield lo.load_item()

