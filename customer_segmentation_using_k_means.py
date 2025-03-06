# -*- coding: utf-8 -*-
"""Customer Segmentation Using K_means.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PBKqZ3KkmGsif6QbHTydbejUvc_g9xMK
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

data=pd.read_csv('data.csv')

data.head()

data.shape

data.info()

data.isnull().sum()

X=data.iloc[:,[3,4]].values

print(X)

wcss=[]
for i in range(1,11):
  kmean=KMeans(n_clusters=i,init='k-means++',random_state=42)
  kmean.fit(X)
  wcss.append(kmean.inertia_)

sns.set()
plt.plot(range(1,11),wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

kmean = KMeans(n_clusters=5, init='k-means++', random_state=0)
Y=kmean.fit_predict(X)
print(Y)

plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0], X[Y==0,1], s=50, c='green', label='Cluster 1')
plt.scatter(X[Y==1,0], X[Y==1,1], s=50, c='red', label='Cluster 2')
plt.scatter(X[Y==2,0], X[Y==2,1], s=50, c='yellow', label='Cluster 3')
plt.scatter(X[Y==3,0], X[Y==3,1], s=50, c='violet', label='Cluster 4')
plt.scatter(X[Y==4,0], X[Y==4,1], s=50, c='blue', label='Cluster 5')

# plot the centroids
plt.scatter(kmean.cluster_centers_[:,0], kmean.cluster_centers_[:,1], s=100, c='cyan', label='Centroids')

plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

