import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the GEO object properties
df = pd.read_csv('geo_objects_with_properties.csv')

# Quick look
print(df.head())

# --- BASIC STATISTICS ---

print("\nMass (kg) Statistics:")
print(df['mass_kg'].describe())

print("\nCross Section (m²) Statistics:")
print(df['max_cross_section_m2'].describe())

# --- HISTOGRAMS ---

# Mass histogram
plt.figure()
df['mass_kg'].dropna().hist(bins=30)
plt.title('Mass Distribution of GEO Objects')
plt.xlabel('Mass (kg)')
plt.ylabel('Number of Objects')
plt.grid(True)
plt.savefig('mass_distribution.png')
plt.show()

# Cross-section histogram
plt.figure()
df['max_cross_section_m2'].dropna().hist(bins=30)
plt.title('Max Cross-Section Area Distribution')
plt.xlabel('Cross-Section (m²)')
plt.ylabel('Number of Objects')
plt.grid(True)
plt.savefig('cross_section_distribution.png')
plt.show()

# --- MASS vs CROSS-SECTION ---

plt.figure()
plt.scatter(df['mass_kg'], df['max_cross_section_m2'], alpha=0.7)
plt.title('Mass vs Cross-Section Area')
plt.xlabel('Mass (kg)')
plt.ylabel('Max Cross-Section (m²)')
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.savefig('mass_vs_cross_section.png')
plt.show()

# --- OBJECT CLASS PIE CHART ---

plt.figure()
df['object_class'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Object Classes in GEO Sample')
plt.ylabel('')
plt.savefig('object_classes_pie.png')
plt.show()

# --- INFER MATERIAL GROUP ---

def infer_material_group(mass):
    if pd.isna(mass):
        return 'Unknown'
    elif mass > 1000:
        return 'Heavy Metal Structure'
    elif 100 < mass <= 1000:
        return 'Medium Metal/Composite'
    elif mass <= 100:
        return 'Light Composite/Fragment'
    else:
        return 'Unknown'

# Apply the material inference
df['material_group'] = df['mass_kg'].apply(infer_material_group)

# Show counts
print("\nInferred Material Groups:")
print(df['material_group'].value_counts())

# Pie chart for material groups
plt.figure()
df['material_group'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Inferred Material Types of GEO Objects')
plt.ylabel('')
plt.savefig('material_type_pie_chart.png')
plt.show()

# --- SAVE FINAL DATASET ---
df.to_csv('geo_objects_enriched.csv', index=False)
print("\n✅ Saved enriched dataset as 'geo_objects_enriched.csv'.")
