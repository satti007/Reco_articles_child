from bs4 import BeautifulSoup
import requests
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
        file = open('child-refugees/'+abc,'w+',0)
        for para in soup.findAll("span",{"class":"s1"}):
            file.write(para.text.encode('utf-8').strip()+'\n')
        file.close
