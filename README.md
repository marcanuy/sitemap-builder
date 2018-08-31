# Sitemap Builder

Generate sitemaps from programmatically collected URLs.

# Features

- Adheres to Sitemap Protocal as defined at https://www.sitemaps.org/protocol.html
- Generates an index that points to compressed sitemaps files
- each generated sitemap won't have more than the allowed amount (50.000 URLs)
- jinja2 templates

# Install

~~~
pip install sitemap-builder
~~~

# Usage

1. Import 

~~~
from sitemap import Sitemap
~~~

2. Initialize

~~~
sitemap = Sitemap()
~~~

3. Add urls to process them later:

~~~
sitemap.add_item("dummy-page")
sitemap.add_item("another-page")
sitemap.add_item("category/foo-bar")
~~~

4. Generate sitemap index and files

~~~
sitemap.generate()
~~~

# Example:

Generated files:

~~~
.
├── sitemap.xml
└── sitemaps
    ├── sitemap-0.xml.gz
    ├── sitemap-1.xml.gz
    ├── sitemap-2.xml.gz
	└── sitemap-3.xml.gz
~~~

# Development

## Crete virtualenv

~~~
virtualenv -p /usr/bin/python3.6 ~/.virtualenvs/sitemap-builder
~~~

Activate it

~~~
workon sitemap-builder
make install
~~~

