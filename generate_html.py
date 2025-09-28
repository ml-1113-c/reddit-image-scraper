import json

with open("output.json", "r", encoding = "utf-8") as f:
    posts = json.load(f)

with open("image.html", "w", encoding="utf-8") as f:
    f.write("<!DOCTYPE html>\n<html>\n<head><title>Reddit Images</title></head>\n<body>\n")
    f.write("<h1>Reddit Image Posts</h1>\n")

    for post in posts:
        f.write(f"<h2>{post['post_title']}</h2>\n")
        f.write(f"<img src = '{post['image_url']}' style = 'max-width:400px;'><br>\n")
    
    f.write("</body>\n</html>")