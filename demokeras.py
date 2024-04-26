#1. load dữ liệu và chia train, validation and test

from numpy import loadtxt
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split 


dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=',')
print(dataset)
#x from 0 to 8 but real life 0-> 7
#y only get 8
x = dataset [:,0:8] 
y = dataset [:,8]

#80% for x_train_val, y_train_val
#20% for x_test, y_test
x_train_val, x_test, y_train_val, y_test = train_test_split(x, y, test_size=0.2)

#80% for x_train, y_train
#20% for x_val, y_val
x_train, x_val,  y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=0.2)

#sequential
# 16, 8, 1 number unit of dense
# 6,148,72,35,0,33.6,0.627,50,1
#input_dim = 8 => x = 6,148,72,35,0,33.6,0.627,50
# y = 1
# relu: ham khu tinh tuyen , sigmoid: đồ thị
model = Sequential
model.add(Dense(16, input_dim=8, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))
model.summary()