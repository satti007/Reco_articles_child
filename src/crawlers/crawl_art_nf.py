from bs4 import BeautifulSoup
import requests
import os.path

with open('links_new.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
f.close()
for link in content:
    r = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data)
    abc = link
    if len(abc)>42 and not '/page/' in abc:
        abc=link[42:-1]
        if not os.path.exists('child-refugees/'+abc):
            file = open('child-refugees/'+abc,'w+',0)
            div_content = soup.findAll("div",{"class":"small-12 large-10 large-centered columns"})
            for tag in div_content:
                for td_tag in tag.findAll("p"):
                    file.write(td_tag.text.encode('utf-8').strip()+'\n')
            file.close()
