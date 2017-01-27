# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from functools import *
import scrapy

attr = lambda attribute, element: element.css("::attr({0})".format(attribute)).extract_first()
#text = lambda element: " ".join(element.css("::text").extract())
text = lambda element: element.extract()
itemprop = partial(attr, "itemprop")

class MailsSpider(CrawlSpider):
    name = "mails"
    allowed_domains = ["lkml.org"]
    start_urls = ['https://lkml.org/lkml/']

    rules = [
        Rule(LinkExtractor(allow='/lkml/\d{4}/\d{1,2}/\d{1,2}/\d+'), callback='parse_mail'),
        Rule(LinkExtractor(allow=['/lkml[0-9/]+']), follow=True),
    ]

    def parse_mail(self, response):
        mail = {itemprop(p): text(p) for p in response.css("*[itemprop]")}
        mail["url"] = response.url
        yield mail
