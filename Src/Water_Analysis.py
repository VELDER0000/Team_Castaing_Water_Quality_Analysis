import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_path = "/Users/vivansarupariya/Desktop/water_potability.csv" # Replace with your file path
data = pd.read_csv(file_path)

# Step 2: Display dataset info
print(data.head())
print(data.info())

# Step 3: Handle missing data
data = data.fillna(data.mean())  # Fill missing values with mean

# Step 4: Descriptive Statistics
print("\nDescriptive Statistics:")
print(data.describe())

# Step 5: Correlation Analysis
correlation_matrix = data.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Step 6: Visualizations

# Scatter Plot for pH vs Turbidity
plt.figure(figsize=(8, 6))
plt.scatter(data['pH'], data['Turbidity'], c='blue', alpha=0.5)
plt.title("pH vs Turbidity")
plt.xlabel("pH")
plt.ylabel("Turbidity (NTU)")
plt.grid(True)
plt.show()

# Histogram of Dissolved Oxygen
plt.figure(figsize=(8, 6))
plt.hist(data['Organic_carbon'], bins=20, color='green', alpha=0.7)
plt.title("Organic Carbon Distribution")
plt.xlabel("Organic carbon (mg/L)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Line Plot for Conductivity over Time (if a time column exists)
if 'Time' in data.columns:
    plt.figure(figsize=(10, 6))
    plt.plot(data['Time'], data['Conductivity'], marker='o', linestyle='-', color='red')
    plt.title("Conductivity Over Time")
    plt.xlabel("Time")
    plt.ylabel("Conductivity (µS/cm)")
    plt.grid(True)
    plt.show()

# Step 7: Save processed data
processed_file_path = 'processed_water_quality_data.csv'
data.to_csv(processed_file_path, index=False)
print(f"\nProcessed data saved to {processed_file_path}")
