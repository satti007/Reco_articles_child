from bs4 import BeautifulSoup
import requests

file = open('links.txt','w+')
for i in range(1,3):
    url_str = 'https://live.firstnews.co.uk/child-refugees/page/'+str(i)+'/'
    r = requests.get(url_str)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        abc = link.get('href')
        if abc:file.write(abc.encode('utf-8').strip()+'\n')
file.close()
