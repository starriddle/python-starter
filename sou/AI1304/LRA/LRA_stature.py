#!/usr/bin/env python3

import pandas
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文字体

#读取数据
dataFrame = pandas.read_excel("stature.xlsx") # 读取数据
print(dataFrame.head()) # 打印前n列数据，快速检查
xy_dataFrame = dataFrame.drop(columns='身高') # 删除身高列数据
x_series = dataFrame['足长'] # 提取足长列数据
y_series = dataFrame['步幅'] # 提取步幅列数据
z_series = dataFrame['身高'] # 提取身高列数据

# 线性回归模型
model = LinearRegression() # 创建线性回归模型
model.fit(xy_dataFrame, z_series) # 模型训练
z_pred = model.predict(xy_dataFrame) # 预测数据
print("回归系数：", model.coef_) # 打印回归系数
print("截距：", model.intercept_) # 打印截距
print("R²：", model.score(xy_dataFrame, z_series)) # 模型评估

# 绘制图形
axes3d = pyplot.subplot(111, projection='3d') # 创建一个三维坐标图形
axes3d.scatter(x_series, y_series, z_series, color='b', marker='.', label='原始数据')  # 绘制原始数据
axes3d.scatter(x_series, y_series, z_pred, color='r', marker='.', label='预测数据') # 绘制预测数据
axes3d.set_xlabel('足长')  # 设置x轴标签
axes3d.set_ylabel('步幅')  # 设置y轴标签
axes3d.set_zlabel('身高')  # 设置z轴标签
axes3d.set_title("身高与足长步频关系模型")  # 设置标题
pyplot.legend(loc='best') # 设置图例
pyplot.show() # 显示图形
