try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='yahooscraper',
    version='0.0.1',
    description='Utilities for scraping Yahoo pages',
    license='MIT',
    author='Jeremy Brudvik',
    author_email='jeremy@brudvik.me',
    url='https://github.com/jbrudvik/yahooscraper',
    keywords=['scrape', 'screen', 'web', 'Yahoo', 'login', 'fantasy'],
    packages=['yahooscraper', 'yahooscraper.fantasy'],
    classifiers=[
        'Programming Language :: Python :: 3.4'
    ],
    install_requires=[
        'beautifulsoup4 >= 4.3.2'
    ])
