from sklearn import svm
import pandas as pd 
import numpy as np 


X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)

clf.predict([[2., 2.]])

# get support vectors
print(clf.support_vectors_)
 