import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import DataPreprocessing as DP

(X_train, X_test, Y_train, Y_test, scaler) = DP.trainDataSet()

p=np.sum(Y_train)
total = np.shape(Y_train)[0]
weight0 = (1/(total-p)*total/2.0)
weight1 = ((1/p)*total/2.0)
class_weights = { 0: weight0, 1: weight1}

X_train = tf.convert_to_tensor(X_train, dtype=tf.float64)
Y_train = tf.convert_to_tensor(Y_train, dtype=tf.float64)
X_test = tf.convert_to_tensor(X_test, dtype=tf.float64)
Y_test = tf.convert_to_tensor(Y_test, dtype=tf.float64)

def getModel():
        model = keras.Sequential(
        [ keras.Input(shape=(23,)),
        layers.Dense(15, activation = "sigmoid"),
        layers.Dense(8, activation = "sigmoid"),
        layers.Dense(6, activation = "sigmoid"),
        layers.Dense(3, activation = "sigmoid"),
        layers.Dense(1, activation = "sigmoid", name = "output")])
        
        model.compile(
        optimizer=keras.optimizers.Adam(),
        loss=keras.losses.BinaryCrossentropy(),
        metrics=[keras.metrics.TruePositives(), keras.metrics.FalseNegatives(), keras.metrics.FalsePositives(), keras.metrics.TrueNegatives(), keras.metrics.Recall(), keras.metrics.BinaryAccuracy(), keras.metrics.AUC()])
        
        history = model.fit(X_train, Y_train, epochs = 50  , class_weight = class_weights)
        
        return model
    
def predictionsOf(data):
    
    X_input = DP.currentDataSet(data)
    X_input = tf.convert_to_tensor(X_input, dtype=tf.float64)
    model = getModel()
    Y_pred = model.predict(X_input)
    credit = 850 - 550*Y_pred
    np.savetxt('creditScores.csv',credit, delimiter=",")
    return

    
