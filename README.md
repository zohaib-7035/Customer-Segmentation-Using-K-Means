# Customer Segmentation Using K-Means

## Overview
This project applies **K-Means clustering** to perform customer segmentation based on their **Annual Income** and **Spending Score**. The goal is to group customers into clusters to analyze their purchasing behavior.

## Dataset
The dataset used in this project is stored in `data.csv` and contains customer information, including:
- Customer ID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)


## Steps in the Project
1. **Load the Data**: Read the CSV file into a Pandas DataFrame.
2. **Data Exploration**:
   - Display dataset information.
   - Check for missing values.
3. **Feature Selection**:
   - Select the `Annual Income` and `Spending Score` columns for clustering.
4. **Elbow Method for Optimal Clusters**:
   - Compute Within-Cluster Sum of Squares (WCSS) for different cluster counts.
   - Use a line plot to determine the optimal number of clusters.
5. **Apply K-Means Clustering**:
   - Fit the K-Means model with the chosen number of clusters (`n_clusters=5`).
   - Predict cluster labels for the customers.
6. **Visualization**:
   - Plot clusters with different colors.
   - Mark cluster centroids.

## Results
The customers are divided into **5 clusters** based on their spending behavior, which helps in customer segmentation for targeted marketing strategies.



