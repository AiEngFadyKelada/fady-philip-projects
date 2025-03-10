# -*- coding: utf-8 -*-
"""Keras Example Number Classification and Recognition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y89Rc8XRv_ZVPDu6P1Q3nXSN6cHDrm5H
"""

# Commented out IPython magic to ensure Python compatibility.
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

plt.imshow(x_train[0],cmap=plt.cm.binary)
plt.show()

print(y_train[0])

mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()
print(x_train[0])

x_train=tf.keras.utils.normalize(x_train,axis=1) # normalization reduces training time and increases model accuracy
x_test=tf.keras.utils.normalize(x_test,axis=1)
print(x_train[0])

plt.imshow(x_train[0],cmap=plt.cm.binary)

model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=3)

val_loss,val_acc=model.evaluate(x_test,y_test) # loss value in test is higher than in train
print(val_loss)
print(val_acc)

y_pred=model.predict(x_test)
print(np.argmax(y_pred[0]))
plt.imshow(x_test[0],cmap=plt.cm.binary)



