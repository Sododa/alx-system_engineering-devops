#!/usr/bin/python3
"""
0-main
"""
import requests


def number_of_subscribers(subreddit):
    # Define the base URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set the custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the subreddit is valid and the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # Invalid subreddit or request error
            return 0
