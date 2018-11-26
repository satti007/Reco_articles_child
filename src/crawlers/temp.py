
with open('links.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
f.close()
content = set(content)
print len(content)
final = []
for link in content:
    if 'https://live.firstnews.co.uk/child-refugees/' in link:
        final.append(link)
print len(final)
f = open('links_new.txt','w+')
for link in final:
    f.write(link+'\n')
