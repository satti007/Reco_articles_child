import sys
import re

with open(sys.argv[1]) as file:
    content = file.readlines()
content = [x.strip() for x in content]
file.close()
links = []
for line in content:
    links+=re.findall(r'/g56/(.*?)\"',line,re.DOTALL)

file = open('g56_links','w+')
for link in links:
    file.write('https://www.timeforkids.com/g56/'+link+'\n')
file.close()
