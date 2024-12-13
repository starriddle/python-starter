#!/usr/bin/python3

import time
import numpy
import pandas
from matplotlib import pyplot
from sklearn.utils import shuffle
from sklearn.model_selection import KFold
from sklearn.svm import SVC

pyplot.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
pandas.options.display.float_format = '{:,.2f}'.format  # 显示小数点后两位
numpy.set_printoptions(suppress=True, precision=2, floatmode='fixed')  # 不使用科学计数法，显示小数点后两位

df_train = pandas.read_csv("train-data.csv")
df_test = pandas.read_csv("test-data.csv")

# 构建向量
print('构建向量……', end='')
start=time.time()
train_target = df_train["Exited"]
train_data = df_train.drop(["Unnamed: 0", "Exited"], axis=1)
test_target = df_test["Exited"]
test_data = df_test.drop(["Unnamed: 0", "Exited"], axis=1)
cols = train_data.columns.tolist()
test_data = test_data[cols]  # 保持列顺序一致
end=time.time()
print(f'耗时 {(end-start)*1000:.3f} ms')

train_data, train_target = shuffle(train_data.values, train_target.values) # 打乱样本数据
scores = []
k = 10
kernels = ['linear', 'poly', 'rbf', 'sigmoid']

print('K折交叉验证(k=10)……', end='')
start=time.time()
for train_index, test_index in KFold(n_splits=k).split(train_data):  # K折交叉验证
    trainx = train_data[train_index]
    trainy = train_target[train_index]
    testx = train_data[test_index]
    testy = train_target[test_index]
    for kernel in kernels:  # 使用不同核函数进行训练和测试
        svc = SVC(kernel=kernel)
        clf = svc.fit(trainx, trainy)
        sc = svc.score(testx, testy)
        scores.append(sc)
end=time.time()
print(f'耗时 {(end-start):.2f} s')

result = pandas.DataFrame(numpy.array(scores).reshape(k, len(kernels)), columns=kernels)
pyplot.title(f'K折交叉验证(k={k})')
pyplot.xlabel('次数')
pyplot.ylabel('正确率acc')
pyplot.ylim([0.5, 1])
pyplot.xlim([1, k])
for kernel in kernels:
    pyplot.plot(result.index, result[kernel], marker='.', label=kernel)
pyplot.legend(loc='best')
pyplot.show()

# 结果分析
print(result * 100)
print('min: ', result.min(axis=0).values * 100)  # 最小值
print('max: ', result.max(axis=0).values * 100)  # 最大值
print('mean: ', result.mean(axis=0).values * 100)  # 平均值
scores = []
for kernel in kernels:
    svc = SVC(kernel=kernel)
    clf = svc.fit(train_data, train_target)
    sc = svc.score(test_data.values, test_target.values)
    scores.append(sc)
print(f'新样本正确率: {numpy.array(scores) * 100}')
