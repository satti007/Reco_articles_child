import os

genres = ['christmas','fairy_tales','fiction','history','instructional','literature','school_stories']

for i in range(7):
    start=0
    end=0
    book_name=''
    path = './'+genres[i]
    for filename in os.listdir(path):
        path ='./'+genres[i]+'/'+filename
        if 'Language: English' in open(path).read():
            with open(path) as file:
                content = file.readlines()
            content = [x.strip() for x in content]
            file.close()
            for num,line in enumerate(content,1):
                if 'Title:' in line:
                    book_name = line
                elif 'START OF THE PROJECT GUTENBERG EBOOK' in line:
                    start=num
                elif 'END OF THE PROJECT GUTENBERG EBOOK' in line:
                    end=num
                elif 'START OF THIS PROJECT GUTENBERG EBOOK' in line:
                    start=num
                elif 'END OF THIS PROJECT GUTENBERG EBOOK' in line:
                    end=num
            # print start,end
            content = content[start+1:end-1]
            # print content
            book_name = book_name[7:]
            file = open('./books/'+str(i)+'_'+book_name,'w+')
            for line in content:
                file.write(line+'\n')
            file.close()
