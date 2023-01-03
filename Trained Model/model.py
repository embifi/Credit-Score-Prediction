from dataExtraction import extract
import numpy as np
from pickle import load
from random import choice, random
import tensorflow as tf

def predict(customer_id):
    
    X = extract(customer_id)
    X1 = X[0]
    Xrest = X[1:]
    lstX2 = [1,2]
    lstX4 = [1,2]
    X2 = choice(lstX2)
    X4 = choice(lstX4)
    X5 = 20+(60-20)*random()
    a = np.array([X1,X2,X4,X5])
    X = np.concatenate((a,Xrest), axis=0)
    X = X.reshape(-1,X.shape[0])
    print(X)
    
    scaler = load(open('scaler.pkl', 'rb'))
    
    X_t = scaler.transform(X)
    
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = tf.keras.models.model_from_json(loaded_model_json)
    model.load_weights("model.h5")
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics='recall')
    PD = model.predict(X_t)
    
    credit = 850 - 550*PD

    return [credit[0][0], PD[0][0]]
    
    
    
