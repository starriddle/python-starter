#!/usr/bin/python3

import numpy
import pandas
import seaborn
from matplotlib import pyplot
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

pyplot.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文字体
pyplot.rcParams['axes.unicode_minus'] = False  # 正常显示负号

dataFrame = pandas.read_csv("StressLevelDataset.csv") # 读取数据集
print(dataFrame.head()) # 显示数据集的前几行
print(dataFrame.isnull().sum()) # 检查数据集中是否存在缺失值，输出每列的缺失值数量
# 数据完整，校验通过
data = dataFrame.drop('stress_level', axis=1) # 提取所有特征数据
level = dataFrame['stress_level'] # 将 'stress_level' 列保存到变量 level 中
data_scaled = StandardScaler().fit_transform(data) # 对特征数据进行标准化处理

# PCA 分析，以确定主成分数量
pca = PCA() # 创建 PCA 模型
pca.fit(data_scaled) # 拟合 PCA 模型
pyplot.figure(figsize=(10, 6))
pyplot.plot(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, marker='.') # 绘制解释方差曲线
pyplot.title('解释方差曲线')
pyplot.xlabel('主成分数量')
pyplot.ylabel('解释方差')
pyplot.show() # 显示解释方差曲线

# 确定主成分数量为 2，进行降维
pca = PCA(n_components=2) # 创建含 2 个主成分的 PCA模型
data_pca = pca.fit_transform(data_scaled) # 拟合模型并对数据降维
pyplot.figure(figsize=(10, 6))
seaborn.scatterplot(x=data_pca[:, 0], y=data_pca[:, 1], hue=1, palette='crest') # 绘制 PCA 降维后的散点图
pyplot.title('PCA 散点图')
pyplot.xlabel('PC1')
pyplot.ylabel('PC2')
pyplot.show() # 显示 PCA 降维后的散点图

print("主成分解释方差比例:", pca.explained_variance_ratio_) # 输出每个主成分的解释方差比例
print("总解释方差比例:", numpy.sum(pca.explained_variance_ratio_)) # 输出总解释方差比例
loadings_df = pandas.DataFrame(pca.components_.T, columns=['PC1', 'PC2'], index=data.columns) # 将主成分加载系数转换为 DataFrame
print("主成分加载系数:")
print(loadings_df) # 输出主成分加载系数

correlation_loadings = pca.components_.T * numpy.sqrt(pca.explained_variance_) # 计算相关加载系数
correlation_loadings_df = pandas.DataFrame(correlation_loadings, columns=['PC1', 'PC2'], index=data.columns) # 将相关加载系数转换为 DataFrame
cutoff = 0.5 # 设置相关加载系数的阈值
significant_correlation_loadings_df = correlation_loadings_df.where(lambda x: abs(x) > cutoff).dropna(how='all').fillna('') # 过滤相关加载系数 DataFrame，只保留大于阈值的值，并删除所有列都为 NaN 的行
print("显著相关加载系数:")
print(significant_correlation_loadings_df) # 输出显著相关加载系数

# 使用主成分数据进行聚类分析
max_clusters = 10 # 设置最大聚类数量

# 使用肘方法确定最佳聚类数量
wcss = []
for i in range(1, max_clusters + 1):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42) # 创建 KMeans 模型
    kmeans.fit(data_pca) # 对数据进行聚类
    wcss.append(kmeans.inertia_)
pyplot.figure(figsize=(10, 6))
pyplot.plot(range(1, max_clusters + 1), wcss, marker='.')
pyplot.title('肘方法')
pyplot.xlabel('K值')
pyplot.ylabel('WCSS')
pyplot.show() # 显示肘方法曲线

# 使用轮廓系数法确定最佳聚类数量
silhouette_scores = []
for n_clusters in range(2, max_clusters + 1):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42) # 创建 KMeans 模型
    cluster_labels = kmeans.fit_predict(data_pca) # 对数据进行聚类
    silhouette_avg = silhouette_score(data_pca, cluster_labels) # 计算平均轮廓系数
    silhouette_scores.append(silhouette_avg)
pyplot.plot(range(2, max_clusters + 1), silhouette_scores, marker='.', linestyle='-')
pyplot.title('轮廓系数法')
pyplot.xlabel('K值')
pyplot.ylabel('轮廓系数')
pyplot.show() # 显示轮廓系数曲线

# 确定最佳聚类数量
optimal_num_clusters = numpy.argmax(silhouette_scores) + 2 # 获取轮廓系数最大的聚类数量
print("最佳聚类数量:", optimal_num_clusters)

# K-均值++聚类
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42) # 创建 KMeans 模型
kmeans.fit(data_pca) # 对数据进行聚类
cluster_labels = kmeans.labels_ # 获取聚类标签
clustered_data = dataFrame.copy()
clustered_data['cluster'] = cluster_labels # 将聚类标签添加到数据集中

pyplot.figure(figsize=(10, 6))
pyplot.scatter(data_pca[:, 0], data_pca[:, 1], c=cluster_labels, marker='.', cmap='crest', s=50, alpha=0.5)
pyplot.title('K-均值++聚类')
pyplot.xlabel('PC1')
pyplot.ylabel('PC2')
pyplot.show() # 显示 K-均值++聚类结果

# 分析聚类结果
clustered_data.groupby('cluster').mean() # 查看每个聚类的均值
cluster_sizes = clustered_data['cluster'].value_counts() # 计算每个聚类的样本数量
print("每个聚类的样本数量:\n", cluster_sizes)
crosstab = pandas.crosstab(clustered_data['cluster'], clustered_data['stress_level'], normalize='index') # 计算每个聚类中不同 stress_level 的比例
print("每个聚类中不同 stress_level 的比例:\n", crosstab)
