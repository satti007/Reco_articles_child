import sys
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
np.random.seed(1234)

train_data = pd.read_csv('../data/files/train.csv')
valid_data = pd.read_csv('../data/files/valid.csv')
test_data  = pd.read_csv('../data/files/test.csv')

label = str(train_data.shape[1] - 1)

def test_model(model,X,y_true):
	y_pred = model.predict(X)
	return  round(accuracy_score(y_true,y_pred),3)

def train(NUM_F,sizes,lr,l2,num_epochs):
	T_X,T_y  = train_data.iloc[:,0:NUM_F],train_data[label]
	V_X,V_y  = valid_data.iloc[:,0:NUM_F],valid_data[label]
	model = MLPClassifier(activation='tanh',solver='adam',shuffle=True,verbose=False,tol=1e-10,random_state=1234,
						  hidden_layer_sizes=sizes,learning_rate_init=lr,alpha=l2,max_iter=num_epochs)
	model.fit(T_X,T_y)
	T_acc = test_model(model,T_X,T_y)
	V_acc = test_model(model,V_X,V_y)
	
	return model,T_acc,V_acc

NUM_F_exp = [5]
lr_exp    = [1e-2,1e-3,1e-4]
l2_exp    = [1e-1,1e-2,1e-3,1e-4,1e-5]
sizes_exp = [(10),(15),(20),(25),(5,5),(10,10),(15,15),(20,20),(5,5,5),(10,10,10)]
num_epochs = 5000

lr_exp_fine    = [1e-2,5e-2,7e-2,1e-1]
l2_exp_fine    = [1e-2,1e-1]
sizes_exp_fine = [5,7,10]

train_acc = []
valid_acc = []
params = {}
count = 0
logger = open('exp.log','a',0)

for f in NUM_F_exp:
	for lr in lr_exp:
		for l2 in l2_exp:
			for sizes in sizes_exp:
				params[count] = [f,sizes,lr,l2,num_epochs]
				model,T_acc,V_acc = train(f,sizes,lr,l2,num_epochs)
				train_acc.append(T_acc)
				valid_acc.append(V_acc)
				print 'index:{},NUM_F:{},lr:{},l2:{},sizes:{},T_acc:{},V_acc:{}'.format(count,f,lr,l2,sizes,T_acc,V_acc)
				logger.write('index:{},NUM_F:{},lr:{},l2:{},sizes:{},T_acc:{},V_acc:{}\n'.format(count,f,lr,l2,sizes,T_acc,V_acc))
				count = count+1
		
best = valid_acc.index(max(valid_acc))
print '\nbest_model is at [f,sizes,lr,l2,num_epochs]:',params[best]
logger.write('\nbest_model is at [f,sizes,lr,l2,num_epochs]:{}\n'.format(params[best]))
f,sizes,lr,l2,num_epochs = params[best][0],params[best][1],params[best][2],params[best][3],params[best][4]
model,T_acc,V_acc        = train(f,sizes,lr,l2,num_epochs)
t_X,t_y                  = test_data.iloc[:,0:f],test_data[label]
t_acc                    = test_model(model,t_X,t_y)
print 'For best_model, Train_acc:{},Valid_acc:{},Test_acc:{}'.format(T_acc,V_acc,t_acc)
logger.write('For best_model, Train_acc:{},Valid_acc:{},Test_acc:{}\n'.format(T_acc,V_acc,t_acc))

