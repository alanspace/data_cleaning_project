# -*- coding: utf-8 -*-
"""
Advanced Data Cleaning and Visualization Pipeline

This script encapsulates a full data processing workflow into a reusable class.
It performs cleaning, generates advanced static visualizations, creates an
interactive HTML dashboard with Plotly, and produces an automated PDF report.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from fpdf import FPDF
import os

class DataProcessor:
    """A class to handle the data cleaning, visualization, and reporting pipeline."""
    
    def __init__(self, input_file: str):
        """Initializes the DataProcessor with file paths and loads the data."""
        self.input_file = input_file
        self.raw_df = None
        self.cleaned_df = None
        self.output_dir = "output"
        self.viz_dir = os.path.join(self.output_dir, "visualizations")
        self.dashboard_file = os.path.join(self.output_dir, "interactive_dashboard.html")
        self.report_file = os.path.join(self.output_dir, "summary_report.pdf")
        
        # Create output directories if they don't exist
        os.makedirs(self.viz_dir, exist_ok=True)
        
        self.load_data()

    def load_data(self):
        """Loads data from the input CSV file."""
        try:
            self.raw_df = pd.read_csv(self.input_file)
            print(f"Successfully loaded data from {self.input_file}")
        except FileNotFoundError:
            print(f"Error: The file {self.input_file} was not found.")
            self.raw_df = None

    def clean_data(self):
        """Cleans the DataFrame by removing duplicates and handling missing values."""
        if self.raw_df is None:
            print("No data to clean.")
            return

        df = self.raw_df.copy()
        df.drop_duplicates(inplace=True)

        fill_values = {
            'Name': 'Unknown',
            'Email': 'missing@email.com',
            'PhoneNumber': 'Unavailable',
            'Age': df['Age'].mean(),
            'Country': 'Unknown',
            'Salary': df['Salary'].mean(),
            'JoiningDate': pd.to_datetime('2025-01-04')
        }
        df.fillna(value=fill_values, inplace=True)
        
        df['Age'] = df['Age'].round().astype(int)
        df['Salary'] = df['Salary'].round().astype(int)
        df['JoiningDate'] = pd.to_datetime(df['JoiningDate'], errors='coerce')
        
        self.cleaned_df = df
        print("Data cleaning complete.")

    def create_static_visualizations(self):
        """Generates and saves static visualizations (histograms, bar, pie, heatmap)."""
        if self.cleaned_df is None:
            print("No cleaned data available for visualization.")
            return
        
        sns.set_theme(style="whitegrid")
        
        # Age Distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(self.cleaned_df['Age'], bins=15, kde=True, color='skyblue')
        plt.title('Age Distribution of Employees', fontsize=16)
        plt.savefig(os.path.join(self.viz_dir, 'age_distribution.png'), dpi=300)
        plt.close()

        # Salary Distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(self.cleaned_df['Salary'], bins=15, kde=True, color='lightgreen')
        plt.title('Salary Distribution of Employees', fontsize=16)
        plt.savefig(os.path.join(self.viz_dir, 'salary_distribution.png'), dpi=300)
        plt.close()

        # Country Pie Chart
        country_counts = self.cleaned_df['Country'].value_counts()
        plt.figure(figsize=(10, 8))
        plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("viridis", len(country_counts)))
        plt.title('Employee Distribution by Country', fontsize=16)
        plt.ylabel('')
        plt.savefig(os.path.join(self.viz_dir, 'country_pie_chart.png'), dpi=300)
        plt.close()

        # Correlation Heatmap
        plt.figure(figsize=(8, 6))
        numerical_df = self.cleaned_df.select_dtypes(include=['number'])
        corr = numerical_df.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap of Numerical Features', fontsize=16)
        plt.savefig(os.path.join(self.viz_dir, 'correlation_heatmap.png'), dpi=300)
        plt.close()
        
        print(f"Static visualizations saved to {self.viz_dir}")

    def create_interactive_dashboard(self):
        """Generates an interactive HTML dashboard using Plotly."""
        if self.cleaned_df is None:
            return

        with open(self.dashboard_file, 'w') as f:
            f.write("<html><head><title>Interactive Data Dashboard</title></head><body>\n")
            f.write("<h1>Employee Data Interactive Dashboard</h1>\n")
            
            # Interactive Histogram of Age
            fig_age = px.histogram(self.cleaned_df, x="Age", nbins=20, title="Interactive Age Distribution")
            f.write(fig_age.to_html(full_html=False, include_plotlyjs='cdn'))
            
            # Interactive Histogram of Salary
            fig_salary = px.histogram(self.cleaned_df, x="Salary", nbins=20, title="Interactive Salary Distribution")
            f.write(fig_salary.to_html(full_html=False, include_plotlyjs='cdn'))

            # Interactive Bar Chart for Country
            country_counts = self.cleaned_df['Country'].value_counts().reset_index()
            country_counts.columns = ['Country', 'Count']
            fig_country = px.bar(country_counts, x='Country', y='Count', title="Interactive Employee Count by Country")
            f.write(fig_country.to_html(full_html=False, include_plotlyjs='cdn'))

            f.write("</body></html>\n")
        
        print(f"Interactive dashboard saved to {self.dashboard_file}")
        
    def generate_pdf_report(self):
        """Generates a PDF report summarizing the cleaning and visualization process."""
        if self.cleaned_df is None:
            return
            
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        
        # Title
        pdf.cell(0, 10, 'Data Cleaning and Visualization Report', 0, 1, 'C')
        pdf.ln(10)
        
        # Summary
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, '1. Data Cleaning Summary', 0, 1)
        pdf.set_font("Arial", '', 10)
        pdf.multi_cell(0, 5, 
            f"Input file: {self.input_file}\n"
            f"Initial records: {len(self.raw_df)}\n"
            f"Records after dropping duplicates: {len(self.raw_df.drop_duplicates())}\n"
            f"Final cleaned records: {len(self.cleaned_df)}\n"
        )
        pdf.ln(5)
        
        # Data Description
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, '2. Cleaned Data Statistics', 0, 1)
        pdf.set_font("Arial", '', 8)
        desc_text = self.cleaned_df.describe().to_string()
        pdf.multi_cell(0, 5, desc_text)
        pdf.ln(5)

        # Visualizations
        pdf.add_page()
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, '3. Visualizations', 0, 1)
        
        viz_files = [
            'age_distribution.png', 'salary_distribution.png',
            'country_pie_chart.png', 'correlation_heatmap.png'
        ]
        
        for i, viz_file in enumerate(viz_files):
            if i % 2 == 0 and i != 0:
                pdf.add_page() # Add new page for every two images
            
            pdf.image(os.path.join(self.viz_dir, viz_file), w=180)
            pdf.ln(5)

        pdf.output(self.report_file)
        print(f"PDF report saved to {self.report_file}")

    def save_cleaned_data(self, output_file="cleaned_data.csv"):
        """Saves the cleaned DataFrame to a CSV file."""
        if self.cleaned_df is not None:
            path = os.path.join(self.output_dir, output_file)
            self.cleaned_df.to_csv(path, index=False)
            print(f"Cleaned data saved to {path}")

    def run_pipeline(self):
        """Executes the full data processing pipeline."""
        if self.raw_df is not None:
            self.clean_data()
            self.create_static_visualizations()
            self.create_interactive_dashboard()
            self.generate_pdf_report()
            self.save_cleaned_data()
            print("\nPipeline executed successfully!")

if __name__ == '__main__':
    # Define the input file and run the pipeline
    processor = DataProcessor(input_file='dirty_data_for_cleaning.csv')
    processor.run_pipeline()