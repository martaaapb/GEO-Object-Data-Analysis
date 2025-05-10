# 🌍 GEO Object Data Analysis

A complete pipeline for collecting, enriching, analyzing, and visualizing data on objects in geostationary orbit (GEO), using ESA's DISCOS API.

---

## 📌 Overview

This repository provides a Python-based workflow to:

- Fetch initial orbital data from the DISCOS API
- Filter objects within the GEO region
- Retrieve detailed physical properties (mass, dimensions, etc.)
- Perform statistical analysis and generate insightful visualizations

---

## 📂 Repository Structure
├── discosweb.py # Collects initial orbit data from DISCOS
├── geoinfo.py # Inspects structure and stats of orbit data
├── info.py # Filters for GEO objects and fetches physical properties
├── analysis.py # Main analysis: stats, plots, material grouping
├── visualizegeo.py # Visualizes GEO region orbits
├── initial_orbits_discosweb.csv # Raw orbit data (output)
├── geo_objects_with_properties.csv # Enriched GEO object data (output)
├── geo_objects_enriched.csv # Final dataset with inferred materials
└── *.png # Output plots (mass, cross-section, pie charts)


---

## 🛰️ Features

- **API Integration**: Pulls real-time orbital and object data from ESA’s DISCOS API
- **Data Filtering**: Identifies GEO objects by semi-major axis
- **Metadata Enrichment**: Adds mass, shape, size, and classification
- **Visualization**: Generates histograms, scatter plots, and pie charts
- **Material Inference**: Categorizes objects by mass into material groups

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/GEO-Object-Data-Analysis.git
cd GEO-Object-Data-Analysis

### 2. Install Requirements
Make sure you have Python 3.8+ and install dependencies:

pip install pandas matplotlib numpy requests

### 3. Set Up API Access
You need a DISCOS API token. Insert your token into discosweb.py and info.py:

TOKEN = "your_discos_api_token"

### 4. Run the Pipeline

python discosweb.py          # Step 1: Get initial orbit data
python geoinfo.py            # Step 2: Inspect data
python info.py               # Step 3: Enrich GEO objects
python analysis.py           # Step 4: Analyze and plot

Optional: visualize GEO orbit distribution

python visualizegeo.py

---

## 📊 Example Outputs
mass_distribution.png: Histogram of object masses

cross_section_distribution.png: Histogram of cross-section areas

mass_vs_cross_section.png: Scatter plot (mass vs area)

object_classes_pie.png: Object classification chart

material_type_pie_chart.png: Inferred material types

---

## 📄 License
This project is licensed under the MIT License.

---

## 🙋‍♀️ Author
Developed by Marta Pareja Boto.
For questions, feel free to open an issue or contact me at [m.pareja@student.maastrichtuniversity.nl].
