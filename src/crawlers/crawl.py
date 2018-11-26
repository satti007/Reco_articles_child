from bs4 import BeautifulSoup
import requests

book_links = []
book_links.append("http://www.gutenberg.org/wiki/Christmas_(Bookshelf)")
book_links.append("http://www.gutenberg.org/wiki/Children%27s_Verse_(Bookshelf)")
book_links.append("http://www.gutenberg.org/wiki/Children%27s_Fiction_(Bookshelf)")
book_links.append("http://www.gutenberg.org/wiki/Children%27s_History_(Bookshelf)")
book_links.append("http://www.gutenberg.org/wiki/Children%27s_Instructional_Books_(Bookshelf)")
book_links.append("http://www.gutenberg.org/wiki/Children%27s_Literature_(Bookshelf)")
book_links.append("http://www.gutenberg.org/wiki/Children%27s_Myths,_Fairy_Tales,_etc._(Bookshelf)")
book_links.append("http://www.gutenberg.org/wiki/Children%27s_Picture_Books_(Bookshelf)")
book_links.append("http://www.gutenberg.org/wiki/School_Stories_(Bookshelf)")

genres = ["christmas","verse","fiction","history","instructional","literature","fairy_tales","picture_books","school_stories"]
for i in range(len(book_links)):
    r = requests.get(book_links[i])
    data = r.text
    soup = BeautifulSoup(data)
    file = open(genres[i]+"_links.txt","w+")

    for link in soup.find_all('a'):
        file.write(str(link.get('href'))+"\n")
    file.close()
