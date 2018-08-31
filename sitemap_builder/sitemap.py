#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Library to generate sitemaps
#
# Add urls and generate sitemaps when done.
# It will generate a main index with referring sitemaps in chunks of
# 50000 urls as specified in http://sitemaps.org
#

import os
from datetime import date
import gzip

from jinja2 import Environment, PackageLoader, select_autoescape

from .models import Item

TEMPLATE_ENVIRONMENT = Environment(
    loader=PackageLoader('sitemap_builder', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    extensions=['jinja2.ext.do'])


class Sitemap():
    """ """

    # set of Items to generate the Sitemap
    urls = set()
    
    def __init__(self,
                 output_dir='',
                 hostname=''):
        self.output_dir = output_dir
        self.hostname = hostname
        
    def add_item(self, item):
        """Adds an item to the sitemap
        Item can be:
        - url: add_item("https://example.com/foo")
        - item: add_item(Item(url="..", priority=0.0, ..))

        :param <str,Item> item:
        """
        if isinstance(item, str):
            item = Item(item)
        self.urls.add(item)

    def __contains__(self, url):
        """Checks if sitemap has an item with the url as loc
        https://docs.python.org/3/reference/datamodel.html#object.__contains__

        :param str url: The url to look for in sitemap's items
        :return boolean: 
        """
        urls = [url.loc for url in self.urls]
        result = url in urls
        return result
        
    def get_urls(self):
        return list(self.urls)
    
    def _sitemap_chunks(self, n=50000):
        """
        Yield successive n-sized chunks from urls list.
        http://stackoverflow.com/q/312443/1165509
        Each text file can contain a maximum of 50,000 URLs and 
        must be no larger than 50MB (52,428,800 bytes)
        """
        url_list = list(self.urls)
        for i in range(0, len(url_list), n):
            yield url_list[i:i + n]

    def create_folders(self):
        if sitemap_file_dir:
            os.makedirs(self.sitemap_file_dir)
        if sitemap_index_dir:
            os.makedirs(self.sitemap_index_dir)

    def generate(self):
        if not self.hostname:
            raise ValueError("Hostname required")
        filename_urls = []
        os.makedirs(os.path.join(self.output_dir, 'sitemaps'))
        for index,urls in enumerate(self._sitemap_chunks()):
            filename_url = self._create_sitemap_file(index, urls)
            filename_urls.append(filename_url)

        self._create_sitemap_index(filename_urls)

    def _create_sitemap_index(self, filename_urls):
        filename = "sitemap.xml"
        template_filename = 'sitemap_index.xml'
        context = {
            'filename_urls': filename_urls,
            'lastmod': date.today().isoformat(),
        }
        self._generate_file(filename, template_filename, context)


    def _create_sitemap_file(self, index, urls):
        filename = "sitemaps/sitemap-{}.xml.gz".format(index)
        filename_url = "{}/{}".format(self.hostname, filename)
        template_filename = 'sitemap_file.xml'
        context = {
            'urls': urls,
            'lastmod': date.today().isoformat(),
        }
        self._generate_file_compressed(filename, template_filename, context)
        return filename_url
    
    def _generate_file_compressed(self, filename, template_filename, context):
        fullpath = os.path.join(self.output_dir, filename)
        with gzip.open(fullpath, 'wb') as f:
            content = self._render_template(template_filename, context)
            #string object into bytes object
            f.write(content.encode())

    def _render_template(self, template_filename, context):
        return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

    def _generate_file(self, filename, template_filename, context):
        with open(os.path.join(self.output_dir, filename), 'w') as f:
            html = self._render_template(template_filename, context)
            f.write(html)
