#!/usr/bin/python3
'''
    Returns a list containing the titles of all hot
    articles for a given subreddit.
'''


def recurse(subreddit, hot_list=[]):
    '''
        Returns a list containing the titles of all hot
        articles for a given subreddit.
    '''
    import requests
    import sys

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        req = requests.get(url, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            req = req.json()
            for post in req['data']['children']:
                hot_list.append(post['data']['title'])
            if len(req['data']['children']) > 0:
                recurse(subreddit, hot_list)
            return hot_list
        else:
            return None
    except Exception:
        return None
