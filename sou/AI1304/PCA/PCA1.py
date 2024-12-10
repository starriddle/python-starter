#!/usr/bin/python3

import pandas
import numpy

dataFrame = pandas.read_excel('data.xls') #读取数据
data = dataFrame.values #转化为numpy数组
area = data[:, :1] #提取第一列
data = data[:, 1:] #提取第二列到最后一列
data = numpy.array(data, dtype='float64') #转化为浮点数
numpy.set_printoptions(suppress=True, precision=2) #设置输出格式
print('原始数据:\n', data) #输出原始数据

temp = numpy.std(data, axis=0) #计算每一列的标准差
data -= numpy.mean(data, axis=0) #减去每一列的均值
data /= temp #除以每一列的标准差
normData = data #标准化后的数据
data = numpy.cov(data.T) #计算协方差矩阵
print('协方差矩阵:\n', data) #输出协方差矩阵

k = 3 #选择前k个主成分
eigVal, eigVec = numpy.linalg.eig(data) #计算协方差矩阵的特征值和特征向量
print('特征值:\n', eigVal) #输出特征值
print('特征向量:\n', eigVec) #输出特征向量

eigValInd = numpy.argsort(-eigVal) #对特征值从大到小排序
print('特征值排序(下标):\n', eigValInd) #输出特征值排序下标
selectVec = eigVec[:, eigValInd[:k]] #选择特征值最大的前k个特征向量
print('最大的k个特征向量:\n', selectVec) #输出特征值最大的前k个特征向量

finalData = numpy.dot(normData, selectVec) #计算主成分
finalData = numpy.concatenate((area, finalData), axis=1) #将区域列和主成分列拼接起来
numpy.set_printoptions(suppress=True, precision=2) #设置输出格式
print('各省份经济数据的主成分:\n', finalData) #输出各省份经济数据的主成分
