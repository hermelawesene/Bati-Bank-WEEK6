import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def understanding_data(df):
    # Overview of the dataset
    print("Number of rows and columns: ", df.shape)  # Prints (rows, columns)

    # Display the first few rows of the dataset
    print("First 5 rows of the dataset:")
    print(df.head())

    # Data types of each column
    print("Data types of each column:")
    print(df.dtypes)

    # Summary of the dataset
    print("Dataset Summary:")
    print(df.info())

def summary_statistics(df):
    # Summary statistics for numeric columns
    summary_stats = df.describe()
    print("Summary Statistics:")
    print(summary_stats)

    # If you want to include non-numeric columns in the summary:
    summary_stats_incl_non_numeric = df.describe(include='all')
    print("Summary Statistics (including non-numeric columns):")
    print(summary_stats_incl_non_numeric)

    # Calculate specific central tendency and dispersion metrics
    mean = df.mean()  # Mean for each numeric column
    median = df.median()  # Median for each numeric column
    std_dev = df.std()  # Standard deviation for each numeric column
    variance = df.var()  # Variance for each numeric column

    print("\nMean:\n", mean)
    print("\nMedian:\n", median)
    print("\nStandard Deviation:\n", std_dev)
    print("\nVariance:\n", variance)

    # Check skewness and kurtosis for shape of the distribution
    skewness = df.skew()  # Skewness for each numeric column
    kurtosis = df.kurt()  # Kurtosis for each numeric column

    print("\nSkewness:\n", skewness)
    print("\nKurtosis:\n", kurtosis)

def numerical_feature_distribution(df):
    # Set up the visual style
    sns.set(style="whitegrid")

    # Visualize distribution using histograms
    df.hist(bins=30, figsize=(15, 10), color='skyblue', edgecolor='black')
    plt.suptitle('Histogram of Numerical Features', fontsize=16)
    plt.show()

    # Visualize distribution using box plots to detect outliers
    plt.figure(figsize=(15, 10))
    sns.boxplot(data=df, orient="h", palette="Set2")
    plt.title('Box Plot of Numerical Features', fontsize=16)
    plt.show()

