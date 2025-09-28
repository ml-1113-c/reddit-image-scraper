import json

with open("output.json", "r", encoding = "utf-8") as f:
    posts = json.load(f)

with open("index.html", "w", encoding="utf-8") as f:
    f.write("<!DOCTYPE html>\n<html>\n<head><title>Reddit Images</title></head>\n<body>\n")
    f.write("<h1>Reddit Image Posts</h1>\n")