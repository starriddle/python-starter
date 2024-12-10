#!/usr/bin/python3

import numpy
import pandas

numpy.set_printoptions(suppress=True, precision=2, floatmode='fixed') # 设置numpy的打印格式
pandas.options.display.float_format = '{:,.2f}'.format # 设置pandas的打印格式

df = pandas.read_excel('data.xls') # 读取数据
area = df['地区'] #取出第一列的区域数据
data = df.drop('地区', axis=1) #舍弃第一列
print('原始数据:\n', data.values) # 打印原始数据

data = (data - data.mean()) / data.std() # 数据标准化
matrix = data.cov() # 计算协方差矩阵
print('协方差矩阵:\n', matrix.values) # 打印协方差矩阵

k = 3 # 指定主成分个数
eigVal, eigVec = numpy.linalg.eig(matrix) # 计算协方差矩阵的特征值和特征向量
print('特征值:\n', eigVal) # 打印特征值
print('特征向量:\n', eigVec) # 打印特征向量

eigValInd = numpy.argsort(eigVal) # 对特征值进行排序
print('特征值排序(下标):\n', eigValInd) # 打印特征值排序(下标)
selectVec = eigVec[:, eigValInd[-1:-(k+1):-1]] # 取出特征值最大的k个特征向量
print('最大的k个特征向量:\n', selectVec) # 打印特征值最大的k个特征向量

finalData = data.dot(selectVec) # 计算主成分
finalData.columns = ['PC1', 'PC2', 'PC3'] # 设置主成分的列名
result = pandas.DataFrame(area).join(finalData) # 将主成分与区域数据合并
print('各省份经济数据的主成分:\n', result) # 打印结果
