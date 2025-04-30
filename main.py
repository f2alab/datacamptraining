import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_dict = {
    'age': [25, 30, 35, 40, 45],
    'salary': [50000, 60000, 70000, 80000, 90000],
    'department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
}
df = pd.DataFrame(data_dict)

# Display the first few rows of the dataframe
print(df.head())