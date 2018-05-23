from sklearn import cross_validation, svm, metrics


def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2:
                continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 255, cols))
            images.append(vals)
    return {"labels": labels, "images": images}


data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")

clf = svm.SVC(C=10, gamma=0.015)
clf.fit(data["images"], data["labels"])

predict = clf.predict(test["images"])

ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("rate:", ac_score)
print("report", cl_report)
