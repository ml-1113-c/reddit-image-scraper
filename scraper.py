import requests
import json

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
    data = r.json()

    posts = data["data"]["children"]
    for post in posts:
        d = post["data"]
        title = d["title"]
        url = d.get("url_overridden_by_dest", "")

        if url.endswith((".jpg", ".jpeg", ".png")):
            results.append(
                {"post_title": title,
                 "image_url": url})
        
    # If after is None, there are no more pages and the loop is stopped
    after = data["data"]["after"]
    if not after:
        break

with open(OUTPUT_FILE, "w", encoding = "utf-8") as f:
    json.dump(results, f, indent = 2) 

print(f"Saved {len(results)} posts to {OUTPUT_FILE}")



    
