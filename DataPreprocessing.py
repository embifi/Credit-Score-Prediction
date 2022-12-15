import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_excel(r'C:\Users\DELL\OneDrive - IIT Kanpur\Documents\Internships\Embifi Intern\Code\Data\Default of credit card Clients.xls')
df.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
df.drop(["a"], axis=1, inplace=True)
df = df.drop([0], axis=0, inplace=False)

df.duplicated().sum()
df = df.drop_duplicates()

arr = df.to_numpy()

X = arr[:, 0:23]
Y = arr[:,23]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)

scaler = StandardScaler()
scaler.fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

np.savetxt("X_train.csv", X_train, delimiter=",")
np.savetxt("X_test.csv", X_test, delimiter=",")
np.savetxt("Y_train.csv", Y_train, delimiter=",")
np.savetxt("Y_test.csv", Y_test, delimiter=",")

def 