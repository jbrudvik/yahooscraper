# yahooscraper

Python utilities for scraping Yahoo pages

[![Build status](https://img.shields.io/travis/jbrudvik/yahooscraper.svg)](https://travis-ci.org/jbrudvik/yahooscraper)
[![PyPI version](https://img.shields.io/pypi/v/yahooscraper.svg)](https://pypi.python.org/pypi/yahooscraper/)

The yahooscraper package is organized into modules and submodules. Each leaf
module (i.e., module without submodules) contains functions that take a single
argument -- HTML text of the page represented by the module and its
namespacing -- and return some data parsed from the page.

If the data is not found, `None` is returned. Or, in cases where an iterable
should be returned, an empty iterable may be returned.

Each leaf module also includes a `url()` function, which returns the URL of
the page represented by the module. In cases where the module represents a set
of URLs, this function takes parameters.

To get data from pages that require authentication, first obtain an
authenticated session using the `login` module's `authenticated_session()`
method function.

See more detailed API documentation using pydoc:

    $ pydoc yahooscraper
    $ pydoc yahooscraper.login
    $ pydoc yahooscraper.fantasy.team


## Examples

Output Fantasy NBA team name:

```python
import yahooscraper as ys

LEAGUE_ID = 237834
TEAM_ID = 8

session = ys.login.authenticated_session()
response = session.get(ys.fantasy.team.url('nba', LEAGUE_ID, TEAM_ID))
team = ys.fantasy.team.team(response.text)
print(team)
```

## Install

    $ pip install yahooscraper


## Development

### Test

    $ python tests.py

### Deploy

- Bump version in `setup.py`
- `$ python setup.py register`
- `$ python setup.py sdist upload`
