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
sitemap.add_url("dummy-page")
sitemap.add_url("another-page")
sitemap.add_url("category/foo-bar")
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
