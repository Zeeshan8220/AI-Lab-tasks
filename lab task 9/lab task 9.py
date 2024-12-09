import pandas as pd

# Use the full path to the file, since both are in the same directory
file_path = r'D:\AI lab tasks\gender_submission.csv'

# Load the dataset
data = pd.read_csv(file_path)

# Data Exploration
first_rows = data.head()
dataset_info = data.info()
summary_stats = data.describe()
missing_values = data.isnull().sum()
columns = data.columns
dataset_shape = data.shape

# Display results
print("First 5 rows:\n", first_rows)
print("\nDataset Information:")
print(dataset_info)
print("\nSummary Statistics:\n", summary_stats)
print("\nMissing Values:\n", missing_values)
print("\nColumns:", columns)
print("\nShape:", dataset_shape)
