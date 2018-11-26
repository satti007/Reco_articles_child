import sys
import pickle
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

num_epochs = 5000
model,T_acc,V_acc = train(19,10,1e-2,0.01,num_epochs)
print 'T_acc:{},V_acc:{}'.format(T_acc,V_acc)

filename = 'models/MLP.sav'
pickle.dump(model,open(filename,'wb'))
print 'Model saved as {}'.format(filename)