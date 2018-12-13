import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler  
from sklearn.neighbors import KNeighborsClassifier 

# Read dataset to pandas dataframe
df = pd.read_csv('./input/liputan62_label.csv')  
# print(df.head())

X = df.iloc[:, :-1].values  
y = df.iloc[:, -1].values  
# print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)  

scaler = StandardScaler()  
scaler.fit(X_train)

X_train = scaler.transform(X_train)  
X_test = scaler.transform(X_test)  
 
classifier = KNeighborsClassifier(n_neighbors=3)  
classifier.fit(X_train, y_train)  

y_pred = classifier.predict(X_test)  
scores = classifier.score(X_test, y_test)
# print(y_pred)
print("Performasin KNN : ", scores)
