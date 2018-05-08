from sklearn import svm

# y = 10 x + 3
b = 3
linear_data = [
    # x,a, y
    [-0.5, 10, -2],
    [-21, 10, -207],
    [-3, 10, -27],
    [0, 10, 3],
    [1, 10, 13],
    [2, 10, 23],
    [3, 10, 33],
    [4, 10, 43],
    [5, 10, 53],
    [6, 10, 63],
    [7, 10, 73],
    [7.1, 10, 74],
    [7.2, 10, 75],
    [7.3, 10, 76],
    [7.4, 10, 77],
    [7.6, 10, 79],
    [7.7, 10, 80],
    [7.8, 10, 81],
    [7.9, 10, 82],
    [8, 10, 83],
    [9, 10, 93],
    [10, 10, 103],
    [100, 10, 1003],
    [114514, 10, 1145143],
    [150, 10, 1503],
    [27, 10, 273],
    [87, 10, 873],
    [870, 10, 8703],
    [871, 10, 8713],
    [873, 10, 8733],
]

data = []
label = []
for row in linear_data:
    x = row[0]
    a = row[1]
    y = row[2]
    data.append([x, a])
    label.append(y)

clf = svm.SVC(kernel='linear')
clf.fit(data, label)

test_data = [[-1, 10], [3, 10], [10, 10], [1, 10], [872, 10], [1514, 10],
             [9, 10], [7, 10], [4, 10], [7.5, 10]]

pre = clf.predict(test_data)

ok = 0
total = 0
answer = []
for idx, l in enumerate(test_data):
    p = pre[idx]
    answer.append(l[0] * l[1] + b)
    if p == l[0] * l[1] + b:
        ok += 1
    total += 1

print("result", pre)
print("answer", answer)
print("accurate", ok / total)
