import unittest
import shutil, tempfile
import os

from ..factories import ItemFactory, SitemapFactory
from ..models import Item, Sitemap
from ..sitemap import SitemapManager

class TestSitemapModel(unittest.TestCase):

    def setUp(self):
        self.sitemap = Sitemap()

    def test_add_item(self):
        item = ItemFactory.build()

        self.sitemap.add_item(item)

        self.assertIn(item, self.sitemap.urls)

    def test_contains_url(self):
        item = ItemFactory.build()

        self.sitemap.urls.add(item)

        self.assertTrue(item.loc, self.sitemap)

    def test_not_contains_url(self):
        item = ItemFactory.build()
        self.sitemap.urls.add(item)

        self.assertNotIn("https://a.com/b", self.sitemap)

    def test_add_item_url(self):
        url = "https://example.com/foo/bar"

        self.sitemap.add_item(url)

        self.assertIn(url, self.sitemap)

    def test_count(self):
        item = ItemFactory.build()

        self.sitemap.add_item(item)

        self.assertEqual(self.sitemap.count(), 1)
    
    # def test_generate_sitemap(self):
    #     sitemap = SitemapFactory()

    #     sitemap.generate()

    def test_generate_requires_filename(self):
        sitemap = Sitemap()
        with self.assertRaises(ValueError):
            sitemap.generate()


class TestSitemapManager(unittest.TestCase):

    def setUp(self):
        self.sitemap_manager = SitemapManager(hostname="https://example.com")


    # def tearDown(self):
    #     # Remove the directory after the test
    #     shutil.rmtree(self.test_dir)


    def test_generate_requires_hostname(self):
        sitemap = SitemapManager(hostname=None)
        with self.assertRaises(ValueError):
            sitemap.generate()

    def create_tmp_dir(self):
        test_dir = tempfile.mkdtemp()
        return test_dir
    
    def test_generate_index(self):
        test_dir = self.create_tmp_dir()
        sitemap = SitemapManager(hostname="https://example.com",
                                 output_dir=test_dir)

        sitemap.generate()


    def test_add_item_instantiates_sitemap(self):
        self.assertIsNone(self.sitemap_manager.current_sitemap)
        self.sitemap_manager.add_item("http://foo.com/")
        self.assertIsInstance(self.sitemap_manager.current_sitemap, Sitemap)

    def test_add_item_adds_sitemap_url_to_sitemaps_urls(self):
        url = "http://foo.com/"

        self.sitemap_manager.add_item(url)

        self.assertTrue(self.sitemap_manager.current_sitemap.url in self.sitemap_manager.sitemaps_urls)


    def test_add_item_to_sitemap(self):
        item = ItemFactory()
        self.sitemap_manager.add_item(item)

        sitemap = self.sitemap_manager.current_sitemap
        self.assertEqual(sitemap.count(), 1)
        self.assertEqual(sitemap.get_urls()[0], item)

class TestItemModel(unittest.TestCase):

    def test_url_can_not_be_empty(self):
        with self.assertRaises(Exception):
            Item(loc="")

    def test_url_should_be_valid(self):
        with self.assertRaises(ValueError):
            Item(loc="bad/url/")

    def test_loc_less_than_limit_length(self):
        url = "http://example.com/{}".format(" " * 2048)

        with self.assertRaises(ValueError):
            Item(loc=url)

    @unittest.skip("to do")
    def test_lastmod_can_be_empty(self):
        item = ItemFactory.build(last_modification=None)

        self.assertIsNone(item.last_modification)
        
    @unittest.skip("to do")
    def test_lastmod_invalid(self):
        lastmod = "123456789019811021"

        with self.assertRaises(ValueError):
            ItemFactory.build(last_modification=lastmod)

    @unittest.skip("to do")
    def test_lastmod_can_omit_time_part(self):
        lastmod = "1981-10-21"
        
        item = ItemFactory.build(last_modification=lastmod)
        
        self.assertEqual(lastmod, item.last_modification)

    def test_changefreq_invalid_value(self):
        changefreq = "foobar"

        with self.assertRaises(ValueError):
            item = ItemFactory.build(change_frequency=changefreq)
        
    def test_changefreq_can_be_empty(self):
        item = ItemFactory.build(change_frequency=None)
        
        self.assertEqual(None, item.change_frequency)

    def test_priority_can_be_empty(self):
        item = ItemFactory.build(priority=None)
        
        self.assertEqual(None, item.priority)
        
    def test_priority_valid_value(self):
        priority = 0.2

        item = ItemFactory.build(priority=priority)
        
        self.assertEqual(priority, item.priority)
        
    def test_priority_invalid_value(self):
        priority = 2

        with self.assertRaises(ValueError):
            item = ItemFactory.build(priority=priority)

if __name__ == '__main__':
    unittest.main()
