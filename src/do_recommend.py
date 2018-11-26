import os
import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# np.random.seed(1234)

PATH  = '../data/r_files/'
idx_to_class = np.load('../data/r_files/idx_to_class.npy').item()
idx_to_title = np.load('../data/r_files/idx_to_title.npy').item()

INFO       = np.load(PATH + 'INFO.npy')
RATE       = np.load(PATH + 'RATE.npy')
USERS_AGE  = np.load(PATH + 'AGE.npy' )
AGE_BOOKS  = np.load(PATH + 'AGE_BOOKS.npy')

USERS = INFO.shape[0]
BOOKS = INFO.shape[1]

TRAIN_INFO = INFO[:8000]
TRAIN_RATE = RATE[:8000]

TOP    = 20
COLLAB = 5

AGE_TO_CLASS = {7:1, 8:2, 9:3, 10:3, 11:4, 12:4, 13:4, 14:5, 15:5, 16:5}

user_count = np.sum(TRAIN_INFO,axis=0)
rate_count = np.sum(TRAIN_RATE,axis=0)
rate_avg   = rate_count/user_count.astype(float)
rate_avg_fame      = np.unique(rate_avg)[::-1]
book_to_fame       = {b:np.where(rate_avg_fame==rate_avg[b])[0][0]+1 for b in range(0,BOOKS)}
book_to_rate_avg   = {b:rate_avg[b] for b in range(0,BOOKS)}

def popular(read_list):
	read_list.sort(key=lambda b: book_to_fame[b])
	
	return read_list

def collaborative(books_rep,books_dist,books_sim,user_info,rate_info):
	user_books = np.where(user_info==1)[0].tolist()
	user_books.sort(key=lambda b: rate_info[b])
	user_books.reverse()
	X = rate_info/float(np.sum(rate_info))
	user_top_books = np.random.choice(BOOKS,int(min(COLLAB,np.sum(user_info))),p=X,replace=False)
	user_top_books_to_sug = {b:books_sim[b] for b in user_top_books}
	
	return user_top_books_to_sug

# books_reps_files = os.listdir(PATH+'books/')
r = 'BOOKS_REP_377.npy'
books_rep  = np.load(PATH+'books_reps/'+r)
books_dist = cosine_similarity(books_rep,books_rep)
books_sim  = np.flip(np.argsort(books_dist,axis=1),1)[:,1:]


cmd1 = ''
print 'Recommedation system started..\n'
while cmd1 != 'EXIT':
	new_f = int(raw_input('Enter 1/0 for new/old user:'))
	cmd2 = ''
	while cmd2 != 'exit':
		if new_f:
			age = int(raw_input('Enter your age:'))
			if age < 7:
				print 'Sorry!! no books in your age group are avaliable in the library'
				break
			else:
				USERS = USERS+1
				print 'Your customer id is:{}'.format(USERS)
				read_list = [k for k,v in idx_to_class.items() if v == AGE_TO_CLASS[age]] 
				top_books = popular(read_list)[:TOP]
				print 'Recommeding popular choices in your reading list,'
				print '#','ID','Title\t\t','Rating'
				for i,b in enumerate(top_books):
					print i+1,b,idx_to_title[b],round(book_to_rate_avg[b],2)
				b  = np.zeros([1,BOOKS])
				r  = np.zeros([1,BOOKS])
				rb = np.zeros([1,BOOKS])
				br  = raw_input('Enter the book you have read followed by rating:')
				while br !='':
					i,s = int(br.split()[0]), float(br.split()[1])
					b[0][i] = 1
					r[0][i] = s
					br  = raw_input('Enter the book you have read followed by rating:')
				rb[0][read_list] = 1
				INFO      = np.vstack((INFO,b))
				RATE      = np.vstack((RATE,r))
				AGE_BOOKS = np.vstack((AGE_BOOKS,rb)) 
				USERS_AGE = np.insert(USERS_AGE,0,age)
				new_f = 0
			cmd2 = raw_input('Enter exit to signout or press any button to further recommed for you:')
		else:
			idx = int(raw_input('Enter user id:')) 
			if idx > USERS:
				print 'Sorry!! no user exists with the id:{}'.format(idx)
				break
			else:
				user_info  = INFO[idx-1]
				rate_info  = RATE[idx-1]
				books_info = AGE_BOOKS[idx-1]
				top_books = collaborative(books_rep,books_dist,books_sim,user_info,rate_info)
				for b in top_books:
					print 'Similar books to {}({})'.format(idx_to_title[b],rate_info[b])
					count = 0
					for i,s in enumerate(top_books[b]):
						if count == 4:
							break
						else:
							if not user_info[s]:
								if books_info[s]:
									print count+1,s,idx_to_title[s],round(book_to_rate_avg[b],2)
									count = count + 1
				br  = raw_input('Enter the book you have read followed by rating:')
				while br !='':
					i,s = int(br.split()[0]), float(br.split()[1])
					INFO[idx-1][i] = 1
					RATE[idx-1][i] = s
					br  = raw_input('Enter the book you have read followed by rating:')
			cmd2 = raw_input('Enter exit to signout or press any button to further recommed for you:')
	cmd1 = raw_input('Enter EXIT to leave program or press any button to recommed for other users:')

np.save(PATH + 'INFO.npy',INFO)
np.save(PATH + 'RATE.npy',RATE)
np.save(PATH + 'AGE.npy',USERS_AGE)
np.save(PATH + 'AGE_BOOKS.npy',AGE_BOOKS)

print 'Data base updated'
print 'Recommedation system closed..'