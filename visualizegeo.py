import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv('initial_orbits_discosweb.csv')

# Check values
print(df['attributes.sma'].describe())
print("Missing semi-major axis values:", df['attributes.sma'].isnull().sum())

# Drop missing semi-major axis if any (not needed here)
# df = df.dropna(subset=['attributes.sma'])

# CORRECT: Filter in meters
geo_df = df[(df['attributes.sma'] >= 42064000) & (df['attributes.sma'] <= 42264000)]

print(f"Found {len(geo_df)} GEO objects.")

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(geo_df['attributes.sma'] / 1000, geo_df['attributes.inc'], s=5)
plt.xlabel('Semi-Major Axis (km)')
plt.ylabel('Inclination (degrees)')
plt.title('Objects near GEO Region (Initial Orbits)')
plt.grid(True)
plt.show()
