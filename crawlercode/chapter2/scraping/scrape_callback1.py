# -*- coding:utf-8 -*-

import lxml.html
import re
from link_crawler import link_crawler


FIELDS = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code',
          'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages',
          'neighbours')


def scrape_callback(url, html):
    if re.search('/view/', url):
        tree = lxml.html.fromstring(html)
        row = [tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[0].text_content()
               for field in FIELDS]
        print url, row


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/places/default/(index|view)', max_depth=1,
                 scrape_callback=scrape_callback)
