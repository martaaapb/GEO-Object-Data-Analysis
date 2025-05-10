import pandas as pd
import requests
import time

# Your DISCOS API token
TOKEN = 'ImVmMzFmYTRkLTQ5NDEtNDFmMy1hOWJiLWFkNzY5ZjgyZDE2MyI.2I2BB7x_tLuaV4MsVlXhRdPZfXk'  # <<--- Replace with your token!

# Load the GEO DataFrame
df = pd.read_csv('initial_orbits_discosweb.csv')

# Filter the GEO region
geo_df = df[
    (df['attributes.sma'] >= 42064000) &
    (df['attributes.sma'] <= 42264000)
]

print(f"Found {len(geo_df)} GEO objects.")

# Get object IDs
object_ids = geo_df['id'].tolist()

# API settings
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/vnd.api+json'
}
base_url = 'https://discosweb.esoc.esa.int/api/objects/'

# Storage for the properties
records = []

for obj_id in object_ids:
    url = base_url + str(obj_id)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        attributes = data['data']['attributes']
        
        record = {
            'object_id': obj_id,
            'name': attributes.get('name', ''),
            'cospar_id': attributes.get('cosparId', ''),
            'object_class': attributes.get('objectClass', ''),
            'mass_kg': attributes.get('mass'),
            'shape': attributes.get('shape', ''),
            'max_cross_section_m2': attributes.get('maximumCrossSection'),
            'min_cross_section_m2': attributes.get('minimumCrossSection'),
            'avg_cross_section_m2': attributes.get('averageCrossSection'),
            'diameter_m': attributes.get('diameter'),
            'height_m': attributes.get('height'),
            'width_m': attributes.get('width')
        }
        
        records.append(record)
        
        print(f"Fetched object {obj_id}: {record['name']}")
        
    else:
        print(f"Failed to fetch object {obj_id}: Status {response.status_code}")
    
    time.sleep(0.5)  # Be nice to the server, avoid hitting rate limits

# Save collected data
properties_df = pd.DataFrame(records)
properties_df.to_csv('geo_objects_with_properties.csv', index=False)

print(f"✅ Done! Collected {len(properties_df)} object properties.")
print(f"Saved to geo_objects_with_properties.csv")
