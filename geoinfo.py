import pandas as pd

# Load your saved CSV
df = pd.read_csv('initial_orbits_discosweb.csv')

# Quick look
print(df.head())

# Column list
print(df.columns)

# Statistics
print(df.describe())

