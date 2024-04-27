#1. load dữ liệu và chia train, validation and test

from numpy import loadtxt
from tensorflow import keras
from keras import Sequential
import numpy
from keras.layers import Dense
from keras.models import load_model
from sklearn.model_selection import train_test_split 
from matplotlib import pyplot


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
model = Sequential()
model.add(Dense(16, input_dim=8, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))
model.summary()

#compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#train model
history = model.fit(x_train, y_train, epochs=100, batch_size=8, validation_data=(x_val, y_val))

#save model
model.save("mymodel.h5")

#load model
model = load_model("mymodel.h5")

#test, đánh giá model
loss, acc = model.evaluate(x_test, y_test)
print("Loss = ", loss)
print("Acc = ", acc)

#test phần tử 10
x_new = x_test[10]
y_new = y_test[10]

# bien gia tri number thanh Dense thì dùng numpy, thêm chìu thì axis = 0
x_new = numpy.expand_dims(x_new, axis=0)


# dự đoán y_predict, giá trị chuẩn y_new
y_predict = model.predict(x_new)

result = "Tieu duong (1)"
if y_predict <= 0.5:
    result =  "K Tieu duong (0)"
print("Gia tri du doan = ", result)
print("Gia tri dung la = ", y_new)


# Vẽ đồ thị hàm loss
pyplot.subplot(211)
pyplot.title('Loss')
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
# Vẽ đồ thị độ chính xác
pyplot.subplot(212)
pyplot.title('Accuracy')
pyplot.plot(history.history['accuracy'], label='train')
pyplot.plot(history.history['val_accuracy'], label='test')
pyplot.legend()
pyplot.show()