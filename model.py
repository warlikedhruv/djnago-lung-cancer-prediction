#import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('survey_lung_cancer.csv')

cleanup_nums = {"LUNG_CANCER":     {"YES": 1, "NO": 2}}
df.replace(cleanup_nums, inplace=True)

cleanup_numss = {"GENDER":     {"M": 1, "F": 2}}
df.replace(cleanup_numss, inplace=True)

df.isnull().sum()

X = df.iloc[:,0:13]
y = df['LUNG_CANCER']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

lr = LogisticRegression()

lr.fit(X_train, y_train)
predicted = lr.predict(X_test)

clf = LogisticRegression(solver='lbfgs', max_iter=1000)
clf.fit(X_train, y_train)
y_predicted = clf.predict(X_test)


pickle.dump(clf, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1, 69, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2]]))