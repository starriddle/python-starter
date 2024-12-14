#!/usr/bin/python3

import numpy
import pandas
from matplotlib import pyplot
from sklearn import datasets

pyplot.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文字体
pyplot.rcParams['axes.unicode_minus'] = False  # 正常显示负号
numpy.set_printoptions(suppress=True, precision=2, floatmode='fixed')  # 显示小数点后两位

def comp_mean_vectors(data, target):  #计算类内平均向量
    labels = target.unique()
    mean_vectors = {}
    for label in labels:
        mean_vectors[label] = data[target == label].mean()
    return mean_vectors

def scatter_within(data, target):  #计算类内离散矩阵
    mean_vectors = comp_mean_vectors(data, target)
    n_features = data.shape[1]
    S_W = numpy.zeros((n_features, n_features))
    for label, mean_vec in mean_vectors.items():
        avgdevs = data[target == label] - mean_vec
        for index, avgdev in avgdevs.iterrows():
            _df = avgdev.to_frame()
            S_W += _df.dot(_df.T)
    return S_W

def scatter_between(data, target):  #计算类间离散矩阵
    mean_vectors = comp_mean_vectors(data, target)
    overall_mean = data.mean()
    n_features = data.shape[1]
    S_B = numpy.zeros((n_features, n_features))
    for label, mean_vec in mean_vectors.items():
        count = data[target == label].shape[0]
        _df = (mean_vec - overall_mean).to_frame()
        S_B += count * _df.dot(_df.T)
    return S_B

def get_components(eig_vals, eig_vecs, n=1): #计算前 n 个主成分
    n_features = data.shape[1]
    eig_pairs = [(numpy.abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]
    eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)
    W = numpy.hstack([eig_pairs[i][1].reshape(n_features, 1) for i in range(0, n)])
    return W


# dataFrame = pandas.read_csv('iris2.csv', header=None) #读取数据
# dataFrame[4] = dataFrame[4].map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})  # 如果是字符串标签，转换为数字标签。针对iris.csv文件
# dataFrame.columns = ['萼片长度', '萼片宽度', '花瓣长度', '花瓣宽度', 'classes'] #设置列名
# data=dataFrame.drop(columns='classes') #提取属性
# target=dataFrame['classes'] #提取类型

iris = datasets.load_iris()  # 加载鸢尾花数据集
data = pandas.DataFrame(iris.data, columns=iris.feature_names)  # 属性值
target = pandas.Series(iris.target, name='classes')  # 标签
classes = iris.target_names  # 标签名

print(f"\nmean：\n{data.mean(axis=0).values}")  #计算属性均值

S_W, S_B = scatter_within(data, target), scatter_between(data, target)  #计算类内离散矩阵和类间离散矩阵
print(f"\nS_W：\n{S_W.values}\n\nS_B：\n{S_B.values}")
eig_vals, eig_vecs = numpy.linalg.eig(numpy.linalg.inv(S_W).dot(S_B))  #计算特征值和特征向量
print(f'\nEigVals: \n{eig_vals}\n\nEigVecs: \n{eig_vecs}')
W = get_components(eig_vals, eig_vecs, 2)  # 计算投影矩阵
print(f'\nW: \n{W}')

X_lda = data.dot(W)  #投影
pyplot.figure()
for i in range(len(classes)):
    pyplot.scatter(X_lda[0][target == i], X_lda[1][target == i], marker='.', label = classes[i])
pyplot.title('鸢尾花线性判别分析')
pyplot.xlabel('LD1')
pyplot.ylabel('LD2')
pyplot.legend()
pyplot.show()
