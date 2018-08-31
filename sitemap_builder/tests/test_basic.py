import unittest

from ..factories import ItemFactory
from ..sitemap import Sitemap
from ..models import Item

class TestSitemapClassMethods(unittest.TestCase):

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
