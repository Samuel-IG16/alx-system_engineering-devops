#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """returns total subs"""
    header = {"User-Agent": "Holberton"}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        return r.json().get("data", None).get("subscribers", None)
    else:
        return 0

if __name__ == "__main__":
    pass
