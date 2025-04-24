import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

# Set seaborn style for better visualization
sns.set_style("whitegrid")

# Task 1: Load and Explore the Dataset
def load_and_explore_data():
    try:
        # Load Iris dataset
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        print("First few rows of the dataset:")
        print(df.head())
        print("\nDataset Info:")
        print(df.info())
        
        # Check for missing values
        print("\nMissing Values:")
        print(df.isnull().sum())
        
        # Since Iris dataset is clean, no need for cleaning
        return df
    
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Task 2: Basic Data Analysis
def analyze_data(df):
    try:
        print("\nBasic Statistics:")
        print(df.describe())
        
        # Group by species and compute mean for each feature
        print("\nMean values by species:")
        grouped_means = df.groupby('species').mean()
        print(grouped_means)
        
        # Observations
        print("\nObservations:")
        print("1. Setosa species tends to have smaller measurements across all features.")
        print("2. Virginica species generally has the largest measurements.")
        print("3. Versicolor falls between Setosa and Virginica in terms of measurements.")
        
        return grouped_means
    
    except Exception as e:
        print(f"Error in analysis: {e}")
        return None

# Task 3: Data Visualization
def create_visualizations(df, grouped_means):
    try:
        # Create a figure with subplots
        plt.figure(figsize=(15, 10))
        
        # 1. Line chart: Mean measurements across species
        plt.subplot(2, 2, 1)
        for column in df.columns[:-1]:
            plt.plot(grouped_means.index, grouped_means[column], marker='o', label=column)
        plt.title('Mean Measurements by Species')
        plt.xlabel('Species')
        plt.ylabel('Measurement (cm)')
        plt.legend()
        plt.xticks(rotation=45)
        
        # 2. Bar chart: Average sepal length by species
        plt.subplot(2, 2, 2)
        sns.barplot(x=grouped_means.index, y=grouped_means['sepal length (cm)'])
        plt.title('Average Sepal Length by Species')
        plt.xlabel('Species')
        plt.ylabel('Sepal Length (cm)')
        
        # 3. Histogram: Distribution of petal length
        plt.subplot(2, 2, 3)
        sns.histplot(data=df, x='petal length (cm)', bins=20)
        plt.title('Distribution of Petal Length')
        plt.xlabel('Petal Length (cm)')
        plt.ylabel('Count')
        
        # 4. Scatter plot: Sepal length vs Petal length
        plt.subplot(2, 2, 4)
        sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
        plt.title('Sepal Length vs Petal Length')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        
        plt.tight_layout()
        plt.savefig('iris_visualizations.png')
        plt.close()
        
        print("\nVisualizations created and saved as 'iris_visualizations.png'")
        print("Insights from visualizations:")
        print("1. The line chart shows clear differences in measurements across species.")
        print("2. The bar chart confirms Virginica has the longest average sepal length.")
        print("3. The histogram shows petal length has a multimodal distribution.")
        print("4. The scatter plot reveals distinct clusters for each species.")
        
    except Exception as e:
        print(f"Error creating visualizations: {e}")

def main():
    # Execute all tasks
    df = load_and_explore_data()
    if df is not None:
        grouped_means = analyze_data(df)
        if grouped_means is not None:
            create_visualizations(df, grouped_means)

if __name__ == "__main__":
    main()