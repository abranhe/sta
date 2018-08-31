import setuptools
import sys

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name = "sta",
    packages = ["sta"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    version = "2.0.0",
    description = "Parse tokens from an string into an array",
    author = "Carlos Abraham",
    author_email = "abraham@abranhe.com",
    url = "https://abranhe.com",
    classifiers = (
        "Programming Language :: Python",
        "Natural Language :: English",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
    project_urls = {
        'Source': 'https://github.com/abranhe/sta',
    },
)
