# -*- coding: utf-8 -*-
"""tensorflow_fundamentals.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q1EAMcYIvBS7nAN83DUCBvgiWtayZa0B

## **fundametnal concepts of tensors using tensorflow**
"""

import tensorflow as tf
import numpy as np
print(tf.__version__)

scalar=tf.constant(7)
print(scalar)

scalar.ndim

vector=tf.constant([10,10])
vector

vector.ndim

matrix=tf.constant([[10,7]
                    ,[7,10]])
matrix

matrix.ndim

another_matrix=tf.constant([[10.,7.],[3.,4.],[8.,6.]],dtype=tf.float16)
another_matrix.ndim

n_tensor=tf.constant([ [[1,2,3,]
                        ,[1,2,6],
                        [63,2,5]],

                           [[16,7,3],
                           [4,1,6],
                           [8,5,3]] ])
n_tensor

n_tensor.ndim

changeable_tensor=tf.Variable([1,2,3])
unchangeable_tensor=tf.constant([1,2,3])
changeable_tensor,unchangeable_tensor

changeable_tensor[0].assign(6)
changeable_tensor

#creating random tensors
random1=tf.random.Generator.from_seed(42)
random1=random1.normal(shape=(3,2))
random2=tf.random.Generator.from_seed(42)
random2=random2.normal(shape=(3,2))
random1,random2,random1==random2

unshuffeled=tf.constant([[10,7],
                         [3,4],
                         [2,5]])
shuffeled1=tf.random.shuffle(unshuffeled)
print(shuffeled1)

shuffeled2=tf.random.shuffle(unshuffeled,seed=42)
shuffeled2

tf.random.set_seed(42)
shuffeled3=tf.random.shuffle(unshuffeled,seed=42)
shuffeled3

tf.random.set_seed(42)
shuffeled4=tf.random.shuffle(unshuffeled)
shuffeled4

ones1=tf.ones(shape=(3,2))
ones1

tf.zeros([3,2])

A=np.arange(1,25,dtype=np.int32)
A

tensor1=tf.constant(A,shape=(3,2,4))
tensor1

tensor2=tf.constant(A)
  tensor2

T=tf.zeros(shape=(2,3,4,5))

T.shape,T.ndim,T.dtype,tf.size(T),tf.size(T).numpy(),T.shape[0],T.shape[1],T.shape[-1]

T[:2,:2,:2,:2]

Y=T[:1,:1,:1,:]
Y

Rank2_tensor=tf.constant([[10,7],
                         [3,4]])
Rank2_tensor.shape,Rank2_tensor.ndim

Rank2_tensor[:,-1]