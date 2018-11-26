from bs4 import BeautifulSoup
import requests

genres = ["christmas","verse","fiction","history","instructional","literature","fairy_tales","picture_books","school_stories"]

for g in genres:
    with open(g+"_links.txt") as f:
        content = f.readlines()
    f.close()
    content = [x.strip() for x in content]
    content = set(content)
    for n in content:
        url_str = "http://www.gutenberg.org/cache/epub/"+n+"/pg"+n+".txt"
        r = requests.get(url_str)
        data = r.text
        file = open("./"+g+"/"+n,"w+")
        file.write(data.encode('utf-8').strip())
        file.close()
