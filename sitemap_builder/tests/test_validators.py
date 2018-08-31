import unittest

from ..validators import valid_uri, valid_uri_length, valid_change_frequency, valid_priority_value, valid_priority_len

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

class TestValidUriLength(unittest.TestCase):
    
    def test_length_url_longer_is_invalid(self):
        uri = "a" * 2049

        result = valid_uri_length(uri)

        self.assertFalse(result)

    def test_length_url_valid(self):
        uri = "a" * 2040

        result = valid_uri_length(uri)

        self.assertTrue(result)

@unittest.skip("Not yet implemented")
class TestValidLastModification(unittest.TestCase):

    def test_date_without_hyphens_and_time(self):
        date = "19811021"
        
        result = valid_datetime(date)

        self.assertTrue(result)

    def test_date_without_time(self):
        date = "1981-10-21"
        
        result = valid_datetime(date)

        self.assertTrue(result)

    def test_datetime_is_iso8601_compliant(self):
        date = "19811021"
        valid_datetime(date)

class TestValidChangeFrequency(unittest.TestCase):
        
    def test_valid_value(self):
        changefreq = "always"

        result = valid_change_frequency(changefreq)

        self.assertTrue(result)

    def test_invalid_value(self):
        changefreq = "foobar"

        result = valid_change_frequency(changefreq)

        self.assertFalse(result)

class TestValidPriority(unittest.TestCase):
        
    def test_valid_value(self):
        priority = "foobar"

        result = valid_priority_value(priority)

        self.assertFalse(result)

    def test_invalid_value_letters(self):
        priority = "foobar"

        result = valid_priority_value(priority)

        self.assertFalse(result)

    def test_invalid_value_numeric(self):
        priority = 10

        result = valid_priority_value(priority)

        self.assertFalse(result)

    def test_invalid_value_float(self):
        priority = 0.333

        result = valid_priority_len(priority)

        self.assertFalse(result)
                

if __name__ == '__main__':
    unittest.main()
