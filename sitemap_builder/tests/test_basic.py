import unittest

from ..factories import ItemFactory
from ..sitemap import Sitemap
from ..models import Item

class TestSitemapClassMethods(unittest.TestCase):

    def test_add_item(self):
        item = ItemFactory.build()
        sitemap = Sitemap()

        sitemap.add_item(item)

        self.assertIn(item, sitemap.urls)

    def test_url_can_not_be_empty(self):
        with self.assertRaises(Exception):
            Item(loc="")

    def test_url_should_be_valid(self):
        with self.assertRaises(ValueError):
            Item(loc="bad/url/")
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
