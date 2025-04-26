import json

# Load the original JSON data
with open('coop.json', 'r') as f:
    data = json.load(f)

# Create a GeoJSON feature collection
geojson = {
    "type": "FeatureCollection",
    "features": []
}

for store in data:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                store["geoKoordinaten"]["longitude"],
                store["geoKoordinaten"]["latitude"]
            ]
        },
        "properties": {
            "name": store["namePublic"],
            "address": f"{store['strasse']} {store['hausnummer']}, {store['plz']} {store['ort']}",
            "opening_hours": store["openingHours"][0]["time"] if store["openingHours"] else "Unknown",
            "opening_day": store["openingHours"][0]["day"] if store["openingHours"] else "Unknown",
            "distance": store["distance"],
            "format": store["formatId"],
            "logo": store["logo"],
            "logo_small": store["logoSmall"],
            "internal_name": store["nameInternal"],
            "betriebsnummer": store["betriebsNummerId"]["id"]
        }
    }
    geojson["features"].append(feature)

# Save the GeoJSON to a file
with open('coop.geojson', 'w') as f:
    json.dump(geojson, f, indent=2)

print("GeoJSON file created successfully!")