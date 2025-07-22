# -*- coding: utf-8 -*-
"""
Professional Data Cleaning and Visualization

This script cleans a dataset by handling duplicates, missing values,
and standardizing data types. It also provides enhanced data visualizations
to better understand the data distribution and saves them as image files.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame, or None if the file is not found.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the DataFrame by removing duplicates and handling missing values.

    Args:
        df (pd.DataFrame): The input DataFrame to clean.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    df_cleaned = df.copy()
    df_cleaned.drop_duplicates(inplace=True)

    fill_values = {
        'Name': 'Unknown',
        'Email': 'missing@email.com',
        'PhoneNumber': 'Unavailable',
        'Age': df_cleaned['Age'].mean(),
        'Country': 'Unknown',
        'Salary': df_cleaned['Salary'].mean(),
        'JoiningDate': '2025-01-04'
    }
    df_cleaned.fillna(value=fill_values, inplace=True)

    df_cleaned['Age'] = df_cleaned['Age'].round(0).astype(int)
    df_cleaned['Salary'] = df_cleaned['Salary'].round(0).astype(int)
    df_cleaned['JoiningDate'] = pd.to_datetime(df_cleaned['JoiningDate'], errors='coerce')

    return df_cleaned

def visualize_and_save_data(df: pd.DataFrame, output_dir: str):
    """
    Generates, displays, and saves visualizations for the cleaned data.

    Args:
        df (pd.DataFrame): The cleaned DataFrame to visualize.
        output_dir (str): The directory to save the visualization images.
    """
    sns.set_theme(style="whitegrid")

    # --- Count of Employees by Country ---
    plt.figure(figsize=(12, 7))
    sns.countplot(x='Country', data=df, order=df['Country'].value_counts().index, palette='viridis')
    plt.title('Count of Employees by Country', fontsize=16)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()  # Adjust layout to make room for labels
    
    # Save the figure before showing it
    plt.savefig(os.path.join(output_dir, 'country_distribution.png'), dpi=300)
    print(f"Saved country distribution plot to {os.path.join(output_dir, 'country_distribution.png')}")
    plt.show()

    # --- Age Distribution of Employees ---
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=15, kde=True, color='skyblue')
    plt.title('Age Distribution of Employees', fontsize=16)
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.tight_layout()
    
    # Save the figure
    plt.savefig(os.path.join(output_dir, 'age_distribution.png'), dpi=300)
    print(f"Saved age distribution plot to {os.path.join(output_dir, 'age_distribution.png')}")
    plt.show()

    # --- Salary Distribution of Employees ---
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Salary'], bins=15, kde=True, color='lightgreen')
    plt.title('Salary Distribution of Employees', fontsize=16)
    plt.xlabel('Salary', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.tight_layout()

    # Save the figure
    plt.savefig(os.path.join(output_dir, 'salary_distribution.png'), dpi=300)
    print(f"Saved salary distribution plot to {os.path.join(output_dir, 'salary_distribution.png')}")
    plt.show()


def save_cleaned_data(df: pd.DataFrame, file_path: str):
    """
    Saves the cleaned DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The cleaned DataFrame.
        file_path (str): The path to save the cleaned CSV file.
    """
    try:
        df.to_csv(file_path, index=False)
        print(f"Cleaned data saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")

if __name__ == '__main__':
    # Define file paths
    input_file_path = 'dirty_data_for_cleaning.csv'
    output_csv_path = 'clean_data.csv'
    output_viz_dir = 'visualizations'

    # Create the output directory for visualizations if it doesn't exist
    os.makedirs(output_viz_dir, exist_ok=True)

    # Main execution block
    raw_df = load_data(input_file_path)

    if raw_df is not None:
        cleaned_df = clean_data(raw_df)
        print("\nData cleaning successful.")
        print(cleaned_df.info())

        # Generate, display, and save visualizations
        visualize_and_save_data(cleaned_df, output_viz_dir)

        # Save the cleaned data to a new CSV
        save_cleaned_data(cleaned_df, output_csv_path)