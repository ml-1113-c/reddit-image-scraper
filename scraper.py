import requests
import json
import time

SUBREDDIT = "malaysia"
PAGES = 10
OUTPUT_FILE = "output.json"
HEADERS = {"User-Agent": "image-scraper"}