
import sys

filename = sys.argv[1]

with open(filename) as file:
    content = file.readlines()
content = [x.strip() for x in content]
file.close()

title_of_book=''
begin=0
flag=0
for num,line in enumerate(content,1):
    if num==len(content)-1:
        file = open('./books/'+title_of_book,'w+')
        print begin,num
        for sen in content[begin:num]:
            file.write(sen+'\n')
        file.close()
    elif '_BOOK_TITLE_ :' in line:
        if flag==1:
            file = open('./books/'+title_of_book,'w+')
            print begin,num
            for sen in content[begin:num-1]:
                file.write(sen+'\n')
            file.close()
            title_of_book=line
            title_of_book = title_of_book[15:]
            begin=num
        elif flag==0:
            title_of_book=line
            title_of_book = title_of_book[15:]
            begin = num
            flag=1
