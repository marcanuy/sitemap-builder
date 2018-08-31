import unittest

from ..validators import valid_uri

class TestValidUri(unittest.TestCase):

    def test_valid_uri(self):
        uri = "http://example.com/some/page/"

        result = valid_uri(uri)

        self.assertTrue(result)

    def test_invalid_url_without_protocol(self):
        uri = "example.com/some/page/"

        result = valid_uri(uri)

        self.assertFalse(result)

    def test_invalid_url_without_domain(self):
        uri = "example/some/page/"

        result = valid_uri(uri)

        self.assertFalse(result)

    def test_length_url(self):
        2048

if __name__ == '__main__':
    unittest.main()
