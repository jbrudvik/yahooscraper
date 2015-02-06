"""
Login page
"""

from bs4 import BeautifulSoup


URL = 'https://login.yahoo.com'
DESKTOP_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'


def url():
    """
    Return the URL for the login page
    """
    return URL


def headers():
    """
    Return the headers necessary to get expected version of the login page
    """
    return {
        'user-agent': DESKTOP_USER_AGENT
    }


def path(page):
    """
    Return the required path for login
    """
    soup = BeautifulSoup(page)
    try:
        return soup.find(id='mbr-login-form')['action']
    except:
        return None


def post_data(page, username, password):
    """
    Given username and password, return the post data necessary for login
    """
    soup = BeautifulSoup(page)
    try:
        inputs = soup.find(id='hiddens').findAll('input')
        post_data = {input['name']: input['value'] for input in inputs}
        post_data['username'] = username
        post_data['passwd'] = password
        return post_data
    except:
        return None
