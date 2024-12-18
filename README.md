# Water Potability Analysis

This project analyzes a dataset on water potability to assess the quality of water using various statistical and visualization techniques. The project is implemented in Python, leveraging popular libraries like pandas, NumPy, and Matplotlib.

---

## Dataset

The dataset used for this project is `water_potability.csv`. It contains information on water quality parameters that can help determine whether water is potable or not.

### Features:

- **pH**: Measure of the acidity or alkalinity of water.
- **Turbidity**: Measure of water clarity in NTU.
- **Dissolved Oxygen**: Amount of oxygen dissolved in water (mg/L).
- **Organic Carbon**: Organic material present in water (mg/L).
- **Conductivity**: Water's ability to conduct electricity (µS/cm).

---

## Project Workflow

### Step 1: Load the Dataset

The dataset is loaded from the specified file path using pandas.

```python
file_path = "/path/to/your/dataset.csv"
data = pd.read_csv(file_path)
```

### Step 2: Dataset Information

Initial inspection of the dataset is done to understand its structure and identify missing values using:

- `data.head()`
- `data.info()`

### Step 3: Handle Missing Data

Missing data is filled using the mean of the respective columns:

```python
data = data.fillna(data.mean())
```

### Step 4: Descriptive Statistics

Basic statistical measures such as mean, standard deviation, and percentiles are computed:

```python
print(data.describe())
```

### Step 5: Correlation Analysis

A correlation matrix is generated to analyze the relationships between different features:

```python
correlation_matrix = data.corr()
print(correlation_matrix)
```

## Step 6: Data Visualization

1. **Scatter Plot**: Relationship between pH and Turbidity.
2. **Histogram**: Distribution of Organic Carbon.
3. **Line Plot** (Optional): Conductivity over time (if time data is available).

Examples:

```python
# Scatter Plot for pH vs Turbidity
plt.scatter(data['pH'], data['Turbidity'], c='blue', alpha=0.5)
```

### Step 7: Save Processed Data

The processed dataset is saved to a new CSV file for further analysis:

```python
processed_file_path = 'processed_water_quality_data.csv'
data.to_csv(processed_file_path, index=False)
```

---

## Installation and Requirements

### Libraries:

- `pandas`: Data manipulation and analysis.
- `numpy`: Numerical computations.
- `matplotlib`: Data visualization.

### Installation:

To install the required libraries, run:

```bash
pip install pandas numpy matplotlib
```

---

---

## Results

The project provides insights into:

- Statistical relationships between water quality parameters.
- Visualizations to understand data distributions and trends.

---

---

## Acknowledgements

Thanks to the creators of the `water_potability.csv` dataset for providing the data for this analysis.

