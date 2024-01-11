import pandas as pd
import json

# Read Excel file into a pandas DataFrame
file_path = r'D:\PycharmProject\pythonProject\test.xlsx'
data = pd.read_excel(file_path)
json_data = data.to_json(orient='records', force_ascii=False)
with open('output_original.json', 'w', encoding='utf-8') as f:
    f.write(json_data)
original_json_data = json.loads(json_data)
transformed_data = []  # Initialize an empty list to store transformed records
for record in original_json_data:
    transformed_record = {}  # Initialize a new transformed record for each original record
    transformed_record["location"] = {
        "lng": record["Long"],
        "lat": record["Lat"]
    }
    transformed_record["name"] = record["Name"]
    transformed_record["objectId"] = None
    transformed_record["description"] = record["Name"]
    transformed_record["types"] = [record["Types"]]
    transformed_record["tags"] = None
    transformed_record["address"] = f"{record['so_nha']}, {record['ten_duong']}, {record['ten_phuong']}, {record['ten_quan']}"
    transformed_record["photos"] = []
    transformed_record["startDate"] = None
    transformed_record["endDate"] = None

    # Format the phone number only if it's not None
    # Format the phone number only if it's not None
    phone_number_float = record["Sdt"]
    if pd.notna(phone_number_float):
        phone_number_str = str(phone_number_float)

        # Remove unwanted characters from the phone number string
        cleaned_phone_number = phone_number_str.replace("-", "").replace(" ", "")

        # Format the phone number as per the desired format "19004601-0282223944-0971717123"
        formatted_phone_number = f"19004601-{cleaned_phone_number[:10]}-{cleaned_phone_number[10:]}"

        transformed_record["phoneNumber"] = formatted_phone_number
    else:
        transformed_record["phoneNumber"] = None

    business_hours_list = [
        {
            "open": {"day": day, "time": str(int(record["Giờ mở"])).zfill(4)},
            "close": {"day": day, "time": str(int(record["Giờ đóng"])).zfill(4)}
        } if pd.notna(record["Giờ mở"]) and pd.notna(record["Giờ đóng"]) else None
        for day in range(7)
    ]

    # Check if all business hours are None and set to None if true
    if all([bh is None for bh in business_hours_list]):
        transformed_record["businessHours"] = None
    else:
        transformed_record["businessHours"] = business_hours_list

    # Adding the geometry details
    transformed_record["geometry"] = {
        "type": "Point",
        "coordinates": [record["Long"], record["Lat"]]
    }

    # Adding source details
    transformed_record["layer"] = "venue"
    transformed_record["source"] = {
        "additionalProp1": None,
        "additionalProp2": None,
        "additionalProp3": None,
        "sourceId": None,
        "name": "ool"
    }

    # Adding the website
    transformed_record["website"] = record["Web"]

    transformed_record["metadata"] = None  # You can add more details if needed

    transformed_data.append(transformed_record)  # Append the transformed record to the list

# Convert the transformed data to JSON format and save it to 'output_transformed.json'
json_transformed_data = json.dumps(transformed_data, ensure_ascii=False, indent=2)

with open('output_transformed.json', 'w', encoding='utf-8') as f:
    f.write(json_transformed_data)

# Print the transformed JSON data
print("Transformed JSON Data:")
print(json_transformed_data)