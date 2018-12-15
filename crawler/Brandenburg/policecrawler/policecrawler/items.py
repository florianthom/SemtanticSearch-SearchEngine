# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
import re
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags



#RegEx geschichte von Marcel
def remove_whitespace(value):
    return value.strip()

#def get_number(value):
#    return re.findall('(Nr. \d+)|(Nr.\d+)', value, re.MULTILINE)

#def get_text(value):
#    return re.sub(r'(Nr. \d+)|(Nr.\d+)', '', value, re.MULTILINE)


class ReportItem(scrapy.Item):
    # defining our item fields
    number = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
    )

    title = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
    )

    text = scrapy.Field(
        input_processor=MapCompose(remove_tags,remove_whitespace),
        output_processor=TakeFirst()
    )

    location = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
    )

    date = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
    )
