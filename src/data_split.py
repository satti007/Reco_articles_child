import os
import random


def dataSpilt(path,path1):
	class_map = {
	'BitGCSE'   : 1,
	'BitKS3'    : 2,
	'WRLevel2'  : 3,
	'WRLevel3'  : 4,
	'WRLevel4'  : 5
	}
	
	TRAIN = 450
	TEST  = 125
	VALID = 50
	
	folders = os.listdir(path)
	for f in folders:
		print '[INFO]: Spiltting {} ...'.format(f)
		label = class_map[f]
		files = os.listdir(path+f)
		random.shuffle(files)
		train,test,valid = files[:TRAIN],files[TRAIN:TRAIN+TEST],files[TRAIN+TEST:TRAIN+TEST+VALID]
		for t in train:
			os.system('cp {} {}'.format(path+f+'/'+t,path1+'train/'+str(label)+'_'+t))
		for t in test:
			os.system('cp {} {}'.format(path+f+'/'+t,path1+'test/'+str(label)+'_'+t))
		for v in valid:
			os.system('cp {} {}'.format(path+f+'/'+v,path1+'valid/'+str(label)+'_'+v))

path  = '../data/WeeBit/'
path1 = '../data/files/'
dataSpilt(path,path1)
print '[INFO]: Num of train,test,valid files:{},{},{}'.format(len(os.listdir(path1+'train/')),len(os.listdir(path1+'test/')),len(os.listdir(path1+'valid/')))