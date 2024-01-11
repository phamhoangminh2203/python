import json

# Read the JSON source file
with open('test binh thuan.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
# Create a GeoJSON feature
features = []
for item in data:
    feature = {
        "type": "Feature",
        "geometry": item["geometry"],
        "properties": {
            "isDeleted": item["properties"]["isDeleted"],
            "createdBy": item["properties"]["createdBy"],
            "address": item["properties"]["address"],
            "name": item["properties"]["name"],
            "description": item["properties"]["description"],
            "types": item["properties"]["types"],
            "phoneNumber": item["properties"]["phoneNumber"],
            "website": item["properties"]["website"]
        }
    }
    features.append(feature)
# Create GeoJSON feature collection
geojson = {
    "type": "FeatureCollection",
    "features": features
}

# Write the GeoJSON object to a new file
with open('test.geojson', 'w') as geojson_file:
    json.dump(geojson, geojson_file)