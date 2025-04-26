import json

# Load the original JSON data
with open('migros_data.json', 'r') as f:
    data = json.load(f)

# Create GeoJSON structure
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Process each facility
for facility in data['data']['facilities']['results']:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [facility['location']['geo']['lon'], facility['location']['geo']['lat']]
        },
        "properties": {
            "id": facility['id'],
            "name": facility['name'],
            "type": facility['type'],
            "slug": facility['slug'],
            "address": facility['location']['address'],
            "address2": facility['location']['address2'],
            "zip": facility['location']['zip'],
            "city": facility['location']['city'],
            "country": facility['location']['country'],
            "logo": facility['logo']['medium'],
            "logo_alt_text": facility['logo']['alt_text']
        }
    }
    geojson['features'].append(feature)

# Save as GeoJSON file
with open('migros_facilities.geojson', 'w') as f:
    json.dump(geojson, f, indent=2)

print("GeoJSON file created successfully!")