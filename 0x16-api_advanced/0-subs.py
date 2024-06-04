#!/usr/bin/python3
"""Module that consumes the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers (not
    active users, total subscribers) for a given subreddit.

    If not a valid subreddit, return 0.
    Invalid subreddits may return a redirect to search results. Ensure that
    you are not following redirects.

    Args:
        subreddit (str): subreddit

    Returns:
        int: number of subscribers
    """
    base_url = 'https://www.reddit.com/r/'
    url = f"{base_url}{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1)'
    }
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
    except requests.RequestException:
        # Handle any request exceptions (e.g., network issues)
        return 0
