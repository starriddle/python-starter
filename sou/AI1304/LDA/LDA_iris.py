#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

def comp_mean_vectors(X, y): #计算类内平均向量
    class_labels = np.unique(y)
    n_classes = class_labels.shape[0]
    mean_vectors = []
    for cl in class_labels:
        mean_vectors.append(np.mean(X[y==cl], axis=0))
    return mean_vectors

def scatter_within(X, y): #计算类内离散矩阵
    class_labels = np.unique(y)
    n_classes = class_labels.shape[0]
    n_features = X.shape[1]
    mean_vectors = comp_mean_vectors(X, y)
    S_W = np.zeros((n_features, n_features))
    for cl, mv in zip(class_labels, mean_vectors):
        class_sc_mat = np.zeros((n_features, n_features))                 
        for row in X[y == cl]:
            row, mv = row.reshape(n_features, 1), mv.reshape(n_features, 1)
            class_sc_mat += (row-mv).dot((row-mv).T)
        S_W += class_sc_mat
    return S_W

def scatter_between(X, y):  #计算类间离散矩阵
    overall_mean = np.mean(X, axis=0)
    n_features = X.shape[1]
    mean_vectors = comp_mean_vectors(X, y)
    S_B = np.zeros((n_features, n_features))
    for i, mean_vec in enumerate(mean_vectors):
        n = X[y==i,:].shape[0]
        mean_vec = mean_vec.reshape(n_features, 1)
        overall_mean = overall_mean.reshape(n_features, 1)
        S_B += n * (mean_vec - overall_mean).dot((mean_vec - overall_mean).T)
    return S_B

def get_components(eig_vals, eig_vecs, n_comp=1):
    n_features = X.shape[1]
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)
    W = np.hstack([eig_pairs[i][1].reshape(n_features, 1) for i in range(0, n_comp)])
    return W

# df = pd.read_csv('iris2.csv', header=None)  # 从本地文件加载鸢尾花数据集
# df[4] = df[4].map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})  # 如果是字符串标签，转换为数字标签。针对iris.csv文件
# y, X = df.iloc[:, 4].values, df.iloc[:, 0:4].values

iris = datasets.load_iris() # 从 scikit-learn库 加载鸢尾花数据集
X, y = iris.data, iris.target

print(X.mean(axis=0)) #计算每列的均值
S_W, S_B = scatter_within(X, y), scatter_between(X, y)
print("S_W: \n%s\nS_B: \n%s" % (S_W, S_B))
eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))
print('EigVals: \n%s\nEigVecs: \n%s' % (eig_vals, eig_vecs))
W = get_components(eig_vals, eig_vecs, n_comp=2)
print('W: \n%s' % W)

X_lda = X.dot(W)
labels = ['setosa', 'versicolor', 'virginica']
for i, label in zip( range(3), labels):
    plt.scatter(X_lda[y == i, 0], X_lda[y == i, 1], label = label)
plt.title('LDA of IRIS dataset')
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.legend()
plt.show()
