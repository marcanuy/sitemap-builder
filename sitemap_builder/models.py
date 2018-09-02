from .validators import (valid_uri, valid_uri_length,
                         valid_change_frequency, valid_priority_value,
                         valid_priority_len)

CHANGE_FREQ = [
    'always',
    'hourly',
    'daily',
    'weekly',
    'monthly',
    'yearly',
    'never'
]

class Item():
    """Model representing a single Sitemap item (data in <url> tag) with all optional tags

    :param str loc: URL of the page. 
    :param str last_mod: The date of last modification of the file.
    :param str change_freq: How frequently the page is likely to change.
    :param float priority: The priority of this URL relative to other 
                         URLs on your site. 
    """

    def __init__(self, loc="", last_modification=None, change_frequency=None, priority=None):
        self.loc = loc
        self.last_modification = last_modification
        self.change_frequency = change_frequency
        self.priority = priority

    @property
    def loc(self):
        """URL of the page.
        This URL must begin with the protocol (such as http) and end with
        a trailing slash, if your web server requires it. This value
        must be less than 2,048 characters.
        (<loc>http://www.example.com/</loc>)
        """
        return self._loc

    @loc.setter
    def loc(self, value):
        if not value:
            raise Exception("loc cannot be empty")
        if not valid_uri(value):
            raise ValueError("loc must contain a valid URI. Currently: {}".format(value))
        if not valid_uri_length(value):
            raise ValueError("loc must be less than 2048 characters")
        self._loc = value

    @property
    def last_modification(self):
        """The date of last modification of the file.  This date should be in
        W3C Datetime format.  https://www.w3.org/TR/NOTE-datetime (ISO
        8601) This format allows you to omit the time portion, if
        desired, and use YYYY-MM-DD.  <lastmod>2005-01-01</lastmod>

        :return str:
        """
        return self._last_modification

    @last_modification.setter
    def last_modification(self, value):
        # if not valid_datetime(value):
        #     raise ValueError("last_modification must contain a valid iso8601 datetime")
        self._last_modification = value

    @property
    def change_frequency(self):
        """How frequently the page is likely to change.
        <changefreq>monthly</changefreq> 
        Valid values: always, hourly, daily, weekly, monthly, yearly, never

        :return str:

        """
        return self._change_frequency

    @change_frequency.setter
    def change_frequency(self, value):
        if value and not valid_change_frequency(value):
            raise ValueError("Changefreq value is not valid")
        self._change_frequency = value

    @property
    def priority(self):
        """The priority of this URL relative to other 
                         URLs on your site. 
                         Valid values range from 0.0 to 1.0.
                         <priority>0.8</priority>

        :return float:

        """
        return self._priority

    @priority.setter
    def priority(self, value):
        if value and not valid_priority_value(value):
            raise ValueError("Priority value is not valid")
        if value and not valid_priority_len(value):
            raise ValueError("Priority should have a single significant digit")
        self._priority = value



    def __str__(self):
        """Object String representation"""
        return "{} - {} - {} - {}".format(self.loc,self.last_modification, self.change_frequency, self.priority)

class Sitemap():

    def __init__(self, filename=None, url=None):
        # set of Items to generate the Sitemap
        self.urls = set()
        self.filename = filename
        self.url = url
            
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

    def count(self):
        return len(self.urls)
    
    def create_sitemap_file(self, index, urls):
        # filename = "sitemaps/sitemap-{}.xml.gz".format(index)
        # filename_url = "{}/{}".format(self.hostname, filename)
        template_filename = 'sitemap_file.xml'
        context = {
            'urls': urls,
            'lastmod': date.today().isoformat(),
        }
        self._generate_file_compressed(filename, template_filename, context)
        return filename_url

    def generate(self):
        if not self.filename:
            raise ValueError("Hostname required")
