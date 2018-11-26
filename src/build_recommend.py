import numpy as np
np.random.seed(1234)

print '[INFO] Generating data..'
USERS = 10000 
BOOKS = 533
PATH  = '../data/r_files/'
idx_to_class = np.load('../data/r_files/idx_to_class.npy').item()

# randomly generate user and books relation 
USERS_AGE    = np.random.randint(7,16,[1,USERS])[0]
AGE_TO_CLASS = {7:1, 8:2, 9:3, 10:3, 11:4, 12:4, 13:4, 14:5, 15:5, 16:5}
AGE_BOOKS    = np.zeros([USERS,BOOKS],dtype = np.int8) 
for U in range(USERS):
	read_list = [k for k,v in idx_to_class.items() if v == AGE_TO_CLASS[USERS_AGE[U]]]
	AGE_BOOKS[U][read_list] = 1

INFO  = np.multiply(np.random.randint(0,2,[USERS,BOOKS]),AGE_BOOKS)
RATE  = np.multiply(np.random.randint(1,6,[USERS,BOOKS]),INFO) 

TRAIN_INFO = INFO[:8000] 
np.save(PATH + 'INFO.npy',INFO)
np.save(PATH + 'RATE.npy',RATE)
np.save(PATH + 'AGE.npy' , USERS_AGE)
np.save(PATH + 'AGE_BOOKS.npy',AGE_BOOKS)

print '[INFO] Generating data done!'

print '[INFO] Getting reps..'
# U @ np.diag(S) @ V = INFO -- SVD
U,S,V  = np.linalg.svd(TRAIN_INFO)
print '[INFO] SVD done!'

# get k values for the which data is reatined is b/w 80 & 90%
retain =  np.cumsum(S)/np.sum(S)
K = np.intersect1d(np.where(0.8<=retain)[0],np.where(retain<=0.9)[0])

# store the representations for each k value 
for k in K:
	USERS_REP = np.dot(U[:,:k],np.diag(S[:k]))
	BOOKS_REP = V.T[:,:k]
	np.save(PATH +'users_reps/USERS_REP_{}.npy'.format(k),USERS_REP)
	np.save(PATH +'books_reps/BOOKS_REP_{}.npy'.format(k),BOOKS_REP)

print '[INFO] Getting reps done!'