import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler  
from sklearn.naive_bayes import GaussianNB 

# Read dataset to pandas dataframe
dfTrain = pd.read_csv('data_berlabel.csv')  
dfTest  = pd.read_csv('data_berlabel_test.csv')
# print(df.head())

X_train = dfTrain.iloc[:, :-1].values  
y_train = dfTrain.iloc[:, -1].values  
X_test  = dfTest.iloc[:, :-1].values  
y_test  = dfTest.iloc[:, -1].values  
# print(y)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)  

scaler = StandardScaler()  
scaler.fit(X_train)

X_train = scaler.transform(X_train)  
X_test = scaler.transform(X_test)  
 
classifier = GaussianNB()
classifier.fit(X_train, y_train)  

y_pred = classifier.predict(X_test)  
scores = classifier.score(X_test, y_test)
# print(y_pred)
print("Performasin N-B : ", scores)
