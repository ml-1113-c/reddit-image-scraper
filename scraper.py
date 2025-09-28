import requests
import json
import time

SUBREDDIT = "malaysia"
PAGES = 10
OUTPUT_FILE = "output.json"
HEADERS = {"User-Agent": "image-scraper"}

results = []
# start at first page
after = None

for i in range(PAGES):
    url = f"https://www.reddit.com/r/malaysia/.json"
    params = {"limit": 25}
    if after:
        params["after"] = after

    r = requests.get(url, headers = HEADERS, params = params)
    data = r.json

