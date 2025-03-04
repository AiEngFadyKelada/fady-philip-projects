# -*- coding: utf-8 -*-
"""ML session 6 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W09F0gAD5suVv3eVXigw4F6CTyooDzge
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("Position_Salaries.csv")

df.head()

X=df.iloc[:,1:-1].values
y=df.iloc[:,-1].values

X

from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor(n_estimators=8,random_state=0)
model.fit(X,y)

model.predict([[4]])

X_grid =np.arange(min(X ) ,max(X),.01)
X_grid=X_grid.reshape(len(X_grid),1)
print(X_grid)

plt.scatter(X,y,color="red")
plt.plot(X_grid,model.predict(X_grid),color="blue")
plt.title('Truth or Bluff(RandomForest regression)')
plt.xlabel('position_level')
plt.ylabel('Salary')
plt.show()

df2=pd.read_csv("AER_credit_card_data.csv")

df2.head()

df2.info()

df2.columns
X=df2[['card', 'reports', 'age', 'income', 'share', 'expenditure', 'owner',
       'selfemp', 'dependents', 'months', 'majorcards', 'active']].values
y=df2["expenditure"].values

df2["card"]=df2["card"].map({"yes":0,"no":1})
df2["owner"]=df2["owner"].map({"yes":0,"no":1})
df2["selfemp"]=df2["selfemp"].map({"yes":0,"no":1})
df2.head()

X=df2.drop("expenditure",axis=1)
y=df2["expenditure"]



y

from sklearn.model_selection import train_test_split
X_train,X_val,y_train,y_val=train_test_split(X,y,test_size=.2)
X_train,X_val,y_train,y_val=train_test_split(X_train,y_train,test_size=.2)

model=RandomForestRegressor()
model.fit(X_train,y_train)

from sklearn.model_selection import KFold
kf=KFold(n_splits=5)

for train_index,test_index in kf.split(X):
  X_train,X_test=X.iloc[train_index] ,X.iloc[test_index]
  y_train,y_test=y.iloc[train_index],y.iloc[test_index]
  model.fit(X_train,y_train)
  score=model.score(X_test,y_test)
  print(score)

ave_score=score.mean()
ave_score

from sklearn.metrics import r2_score

pred=model.predict(X_test)
r2=r2_score(y_test,pred)
print(r2)





