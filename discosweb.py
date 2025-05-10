import requests
import pandas as pd
import time

# ===== CONFIGURATION =====
TOKEN = "ImVmMzFmYTRkLTQ5NDEtNDFmMy1hOWJiLWFkNzY5ZjgyZDE2MyI.2I2BB7x_tLuaV4MsVlXhRdPZfXk"

# Endpoint for initial orbits
BASE_URL = "https://discosweb.esoc.esa.int/api/initial-orbits"

# Headers
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.api+json"
}

# Set page size
PAGE_SIZE = 100

# Empty list to collect all results
all_orbits = []

# Start with first page
page_number = 1

while True:
    print(f"Fetching page {page_number}...")
    
    # Setup parameters
    params = {
        "page[size]": PAGE_SIZE,
        "page[number]": page_number
    }
    
    # Send GET request
    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    
    # Check if successful
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        break
    
    # Extract data
    page_data = response.json()
    
    # If no more data, stop
    if not page_data.get('data'):
        print("No more data!")
        break
    
    # Add to full list
    all_orbits.extend(page_data['data'])
    
    # Go to next page
    page_number += 1
    
    # Pause a bit to avoid hitting rate limits (important if many pages)
    time.sleep(0.2)

# ==== Save to CSV ====
print(f"Total records collected: {len(all_orbits)}")

# Convert to pandas DataFrame
df = pd.json_normalize(all_orbits)

# Save to CSV
output_file = "initial_orbits_discosweb.csv"
df.to_csv(output_file, index=False)

print(f"✅ CSV saved as {output_file}")
