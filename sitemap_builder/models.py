from .validators import valid_uri

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
                         This date should be in W3C Datetime format. 
                         https://www.w3.org/TR/NOTE-datetime (ISO 8601)
                         This format allows you to omit the time 
                         portion, if desired, and use YYYY-MM-DD.
                         <lastmod>2005-01-01</lastmod>
    :param str change_freq: How frequently the page is likely to change.
                            <changefreq>monthly</changefreq>
                            Valid values: always, hourly, daily, weekly,
                            monthly, yearly, never
    :param str priority: The priority of this URL relative to other 
                         URLs on your site. 
                         Valid values range from 0.0 to 1.0.
                         <priority>0.8</priority>
    """

    def __init__(self, loc="", last_mod=None, change_freq=None, priority=None):
        self.loc = loc
        self.last_mod = last_mod
        self.change_freq = change_freq
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
            raise ValueError("loc must contain a valid URI")
        self._loc = value
        
    def __str__(self):
        return "{} - {} - {} - {}".format(self.loc,self.last_mod, self.change_freq, self.priority)
