#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Library to generate sitemaps
#
# Add urls and generate sitemaps when done.
# It will generate a main index with referring sitemaps in chunks of
# 50000 urls as specified in http://sitemaps.org
#

from datetime import date
from .models import Item, Sitemap

from .writer import *

class SitemapManager():
    """ """

    def __init__(self,
                 output_dir='',
                 hostname=''):
        self.output_dir = output_dir
        self.hostname = hostname
        self.sitemaps_urls = []
        self.current_sitemap = None

    # def _sitemap_chunks(self, n=50000):
    #     """
    #     Yield successive n-sized chunks from urls list.
    #     http://stackoverflow.com/q/312443/1165509
    #     Each text file can contain a maximum of 50,000 URLs and 
    #     must be no larger than 50MB (52,428,800 bytes)
    #     """
    #     url_list = list(self.urls)
    #     for i in range(0, len(url_list), n):
    #         yield url_list[i:i + n]

    def _new_sitemap(self):
        filename = "sitemaps/sitemap-{}.xml.gz".format(len(self.sitemaps_urls))
        url = "{}/{}".format(self.hostname, filename)
        self.current_sitemap = Sitemap(filename=filename, url=url)
        self.sitemaps_urls.append(url)        

    def add_item(self, item):
        # creates a new Sitemap instance if there is none
        if not self.current_sitemap:
            self._new_sitemap()
        self.current_sitemap.add_item(item)
    
    def create_folders(self):
        if sitemap_file_dir:
            os.makedirs(self.sitemap_file_dir)
        if sitemap_index_dir:
            os.makedirs(self.sitemap_index_dir)

    def generate(self):
        if not self.hostname:
            raise ValueError("Hostname required")
    #     filename_urls = []
    #     os.makedirs(os.path.join(self.output_dir, 'sitemaps'))
    #     for index,urls in enumerate(self._sitemap_chunks()):
    #         filename_url = self._create_sitemap_file(index, urls)
    #         filename_urls.append(filename_url)

        self._create_sitemap_index()

    def _create_sitemap_index(self):
        filename = "sitemap.xml"
        template_filename = 'sitemap_index.xml'
        context = {
            'filename_urls': self.sitemaps_urls,
            'lastmod': date.today().isoformat(),
        }
        generate_file(filename, template_filename, context, self.output_dir)
