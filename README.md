# Sitemap Builder

Generate sitemaps from programmatically collected URLs.

# Features

- Generates an index that points to compressed sitemaps files
- each generated sitemap won't have more than the allowed amount of
  50.000 URLs

# Install

~~~
pip install sitemap-builder
~~~

# Usage

Import 

~~~
from sitemap import Sitemap
~~~

Initialize

~~~
sitemap = Sitemap()
~~~

Add urls to process them later:

~~~
sitemap.add_url("dummy-page")
sitemap.add_url("another-page")
sitemap.add_url("category/foo-bar")
~~~

Generate sitemap index and files

~~~
sitemap.generate()
~~~
