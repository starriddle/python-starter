#!/usr/bin/python3

import numpy

numpy.set_printoptions(suppress=True, precision=2) #设置输出格式

x = [[-1, 2, 1, -2], [-2, 0, 0, 2], [-2, 0, 0, 2]] #数据集
data = numpy.array(x, dtype='float64') #将数据集转换为numpy数组
print('原始数据:\n', data) #打印数据集
data = numpy.cov(data.T) #计算协方差矩阵
print('协方差矩阵:\n', data) #打印协方差矩阵

k = 3 #选择前K个特征向量
eigVal, eigVec = numpy.linalg.eig(data) #求协方差矩阵的特征值和特征向量
print('特征向量:\n', eigVec) #打印特征向量
print('特征值:\n', eigVal) #打印特征值
eigValInd = numpy.argsort(-eigVal) #返回特征值由大到小排序的下标p
print('特征值排序(下标):\n', eigValInd) #打印特征值由大到小排序的下标p
selectVec = eigVec[:, eigValInd[:k]] #提取前K个特征向量
print('选择特征向量:\n', selectVec) #打印选择特征向量
print('选择特征值:\n', eigVal[eigValInd[:k]]) #打印选择特征值
