# yahooscraper

Python utilities for scraping Yahoo pages

[![Build status](https://img.shields.io/travis/jbrudvik/yahooscraper.svg)](https://travis-ci.org/jbrudvik/yahooscraper)
[![PyPI version](https://img.shields.io/pypi/v/yahooscraper.svg)](https://pypi.python.org/pypi/yahooscraper/)
[![Supported Python versions](https://pypip.in/py_versions/yahooscraper/badge.svg?style=flat)](https://pypi.python.org/pypi/yahooscraper/)

The yahooscraper package is organized into modules and submodules. Each leaf
module (i.e., module without submodules) contains functions that take a single
argument — HTML text of the page represented by the module and its
namespacing — and return some data parsed from the page.

Additionally, each leaf module also includes a `url()` function, which returns
the URL of the page represented by the module. In cases where the module
represents a set of URLs, this function takes parameters.

If the data is not found, `None` is returned. Or, in cases where an iterable
should be returned, an empty iterable may be returned.

See more detailed API documentation using pydoc:

    $ pydoc yahooscraper
    $ pydoc yahooscraper.login
    $ pydoc yahooscraper.fantasy.team


## Examples

Log in to Yahoo:

    import requests
    import yahooscraper as ys
    from urllib.parse import urljoin

    DESKTOP_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'
    HEADERS = {
        'user-agent': DESKTOP_USER_AGENT
    }

    session = requests.Session()
    session.headers.update(HEADERS)

    response = session.get(ys.login.url())
    login_path = ys.login.path(response.text)
    login_url = urljoin(response.url, login_path)
    login_post_data = ys.login.post_data(response.text, username, password)

    session.post(login_url, data=login_post_data)


Output Fantasy NBA team name (continuing on from first example):

    LEAGUE_ID = 237834
    TEAM_ID = 8

    response = session.get(ys.fantasy.team.url('nba', LEAGUE_ID, TEAM_ID))
    team = ys.fantasy.team.team(response.text)
    print(team)


## Install

    $ pip install yahooscraper


## Test

    $ python tests.py
