"""
Data Preprocessing Module

Research Title:
Detecting Phishing Websites in Web Browsing Environments
Using Ensemble Machine Learning Algorithms

Purpose:
This script demonstrates the preliminary process of preparing
phishing website datasets before machine learning classification.
"""


import pandas as pd


def load_dataset(file_path):
    """
    Load phishing website dataset.

    Parameters:
        file_path (str):
            Location of dataset file

    Returns:
        pandas DataFrame
    """

    dataset = pd.read_csv(file_path)

    return dataset



def clean_dataset(dataset):
    """
    Perform basic dataset cleaning.

    Processing:
    - Remove duplicated records
    - Remove missing values

    Returns:
        Cleaned dataset
    """

    dataset = dataset.drop_duplicates()

    dataset = dataset.dropna()

    return dataset



def preprocess_dataset(file_path):

    dataset = load_dataset(file_path)

    cleaned_dataset = clean_dataset(dataset)

    return cleaned_dataset



# Example usage:
#
# dataset = preprocess_dataset(
#     "phishing_website_dataset.csv"
# )
#
# print(dataset.head())
