import tensorflow as tf
import numpy as np

'''
自定义一个模型

'''

def model(features,lables,mode):
    W = tf.get_variable("W",[1],dtype=tf.float64)
    b = tf.get_variable("b",[1],dtype=tf.float64)
    y = W*features['x'] + b

    