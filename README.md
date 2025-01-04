# **Data Cleaning and Visualization Project**

Welcome to the **Data Cleaning and Visualization** project! This repository demonstrates how to clean messy data and create insightful visualizations using **Python** with **Pandas** and **Matplotlib**.

---

## **Project Description**

This project focuses on:
1. Cleaning a dataset by handling missing values, removing duplicates, and ensuring consistent formatting.
2. Visualizing the cleaned data to uncover trends and patterns.
3. Saving the cleaned dataset for future use.

---

## **Features**

1. **Data Cleaning**:
   - **Duplicate Removal**: Eliminates duplicate rows.
   - **Handling Missing Values**:
     - Fills missing names with `"Unknown"`.
     - Replaces missing emails with `"missing@email.com"`.
     - Assigns `"Unavailable"` to missing phone numbers.
     - Fills missing ages with the average age (rounded).
     - Replaces missing countries with `"Unknown"`.
     - Assigns the mean salary (rounded) to missing salary values.
     - Sets missing joining dates to `"2025-01-04"`.
   - **Date Formatting**: Converts joining dates to a standard datetime format.

2. **Data Visualization**:
   - **Country Distribution**: Bar chart showing the number of employees by country.
   - **Age Distribution**: Histogram displaying the age distribution of employees.
   - **Salary Distribution**: Histogram showcasing the salary distribution of employees.

3. **Export Cleaned Data**:
   - Saves the cleaned dataset as a CSV file (`clean_data.csv`).

---

## **File and Folder Structure**

```bash
data_cleaning_project/
├── dirty_data_for_cleaning.csv   # Input raw data file
├── clean_data.csv                # Cleaned dataset (output)
├── data_cleaning.py              # Python script for cleaning and visualization
├── README.md                     # Documentation for the project
```

---

## **Requirements**

Install the required Python libraries using:
```bash
pip install pandas matplotlib
```

---

## **How to Run the Project**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/thekartikeyamishra/data_cleaning_project.git
   cd data_cleaning_project
   ```

2. **Add the Input Data**:
   - Place your raw dataset (`dirty_data_for_cleaning.csv`) in the project directory.

3. **Run the Script**:
   ```bash
   python data_cleaning.py
   ```

4. **View the Visualizations**:
   - The script generates:
     - A bar chart showing employee count by country.
     - Histograms for age and salary distributions.

5. **Access the Cleaned Data**:
   - The cleaned dataset is saved as `clean_data.csv` in the project directory.

---


## **Output**

1. **Cleaned Data**: Saved as `clean_data.csv`.
2. **Visualizations**:
   - **Bar Chart**: Employee count by country.
   - **Histogram**: Age distribution.
   - **Histogram**: Salary distribution.

---

## **Future Enhancements**

1. **Add More Visualizations**:
   - Correlation heatmaps.
   - Pie charts for categorical data distribution.
2. **Automate Data Cleaning**:
   - Build a reusable cleaning pipeline.
3. **Interactive Dashboards**:
   - Integrate tools like Plotly or Dash for interactive visualizations.

---

## **Contributing**

Contributions are welcome!  
- Fork the repository.  
- Add your changes.  
- Submit a pull request.


If this project helps you, consider giving it a ⭐ on GitHub!  
Happy coding and data cleaning! 🚀
