try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

README = 'README.md'

try:
    import pypandoc
    long_description = pypandoc.convert(README, 'rst')
except:
    long_description = ''

setup(
    name='yahooscraper',
    version='0.1.1',
    description='Utilities for scraping Yahoo pages',
    long_description=long_description,
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
