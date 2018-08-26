import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sitemap-builder",
    version="0.0.1",
    author="Marcelo Canina",
    author_email="me@marcanuy.com",
    description="Generate sitemaps from programmatically collected URLs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcanuy/sitemap-builder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
