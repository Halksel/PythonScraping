from sklearn import cross_validation, svm, metrics
import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv("bmi.csv")

label = tbl["label"]
w = tbl["weight"] / 120
h = tbl["height"] / 200

wh = pd.concat([w, h], axis=1)

data_train, data_test, label_train, label_test = cross_validation.train_test_split(
    wh, label)

clf = svm.SVC()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)

print("rate:", ac_score)
print("report\n", cl_report)
