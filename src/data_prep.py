import os
import re
import sys
import pyphen
import numpy as np
import pandas as pd 
from lexical_feat import *
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,RegexpTokenizer
import pickle

NUM_F = 19
PATH  = '../data/files/'
tokenizer = RegexpTokenizer(r'\w+')
dict = pyphen.Pyphen(lang='en')

def classify_books(weights):
	data    = pd.read_csv('../data/files/articles.csv')
	data_X  = data.iloc[:,0:19]
	model   = pickle.load(open(weights, 'rb'))
	pred    = model.predict(data_X)
	
	return pred

def get_features(folder,file,book_f):
	feats     = np.zeros([1,NUM_F]) 
	text      = open(PATH+folder+'/'+file).read().decode('utf8','ignore')
	sentences = sent_tokenize(text)
	Tot_sens  = len(sentences)
	Words     = tokenizer.tokenize(text)
	Words     = [re.sub('\W','', W) for W in Words]
	# Words     = [W for W in Words if not W in stopwords.words('english')]
	Words     = [W for W in Words if len(W)>1]
	Tot_words = len(Words)
	Tot_chars = sum([len(W) for W in Words])
	Tot_sylls = sum([len(dict.inserted(W).split('-')) for W in Words])
	
	feats[0][0] = round(float(Tot_chars)/Tot_words,3)
	feats[0][1] = round(float(Tot_sylls)/Tot_words,3)
	feats[0][2] = round(float(Tot_words)/Tot_sens ,3)
	feats[0][3] = round(0.39*float(Tot_words)/Tot_sens + 11.8*float(Tot_sylls)/Tot_words -15.59,3)
	feats[0][4] = round(5.58*float(Tot_chars)/Tot_words - 29.6*float(Tot_sens)/Tot_words - 15.8,3)
	feats[0][5:19] = get_lexical_feat(Words)
	
	return feats

train_f,test_f,valid_f =  os.listdir(PATH+'train/'),os.listdir(PATH+'test/'),os.listdir(PATH+'valid/')
folders = [train_f,test_f,valid_f]

def get_model_features():
	for folder in folders:
		X = len(folder)
		if  X == 2250:
		  name = 'train'
		elif X == 625:
		  name = 'test'
		else:
		  name = 'valid'
		
		labels   = np.zeros([X,1])
		features = np.zeros([X,NUM_F])
		for index,file in  enumerate(folder):
		  print '[INFO] count:{}, Processing {} in {} folder'.format(index+1,file,name)
		  labels[index]   = int(file.split('_')[0])
		  features[index] = get_features(name,file,False)
		data    = np.hstack((features,labels))
		data_df = pd.DataFrame(data)
		data_df[NUM_F] = data_df[NUM_F].astype(int)
		data_df.to_csv(PATH+name+'.csv',index=False)
		print '[INFO] Processing {} folder done, {}_data shape:{}'.format(name,name,data.shape) 

def get_book_features(weights):
	books    = os.listdir(PATH +'articles/')
	features = np.zeros([len(books),NUM_F])
	idx_to_title = {}
	
	for index,file in enumerate(books):
		print '[INFO] count:{}, Processing {}'.format(index+1,file)
		idx_to_title[index] = file
		features[index]     = get_features('articles',file,True)
	
	data    = features
	data_df = pd.DataFrame(data)
	data_df[0] = data_df[0].astype(int)
	data_df.to_csv(PATH+'articles.csv',index=False)
	np.save('../data/r_files/idx_to_title.npy',idx_to_title)
	print '[INFO] Processing articles folder done, articles_data shape:{}'.format(data.shape) 

	return classify_books(weights)

# get_model_features()
book_class   = get_book_features('models/MLP.sav')
idx_to_class = {i:book_class[i] for i in range(len(book_class))}
np.save('../data/r_files/idx_to_class.npy',idx_to_class)
print 'Class\tNum_of_books'
print pd.Series(book_class).value_counts()
