#!/usr/bin/python3
"""
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given, the function
    should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
        Return the numbre of suscribers for reddit Api
        according to a subreddit.
    """
    header = {'User-Agent': 'Chrome/90.0.4430.212 Safari/537.36'}
    req = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), allow_redirects=False,
                       headers=header)
    if req.status_code == 200:
        subscribers = req.json().get('data').get('subscribers')
        return subscribers
    else:
        return 0
