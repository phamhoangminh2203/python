import json
import requests

# Đọc dữ liệu từ file JSON
file_path = "D:\PycharmProject\pythonProject\.venv\output_transformed.json"  # Thay 'path_to_your_file.json' bằng đường dẫn tới file JSON của bạn
with open(file_path, 'r', encoding='utf-8') as file:
    data_to_send_list = json.load(file)
# Định nghĩa URL API và header cần thiết
url = "https://api-data.map4d.vn/map/manage/place"
headers = {
    "accept": "text/plain",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI5NWY0ZDA3Ny1iNGM4LTRmZGYtOGVlNi00YTBlNDUwZGJkNTMifQ.eyJqdGkiOiIwMDYyMDhiOC1iMmQxLTQxMzgtYjIxYy04NTA0MDI2NDE5YTgiLCJleHAiOjE3MDQ5NDg5MjgsIm5iZiI6MCwiaWF0IjoxNzA0Nzc2MTI4LCJpc3MiOiJodHRwczovL2FjY291bnRzLm1hcDRkLnZuL2F1dGgvcmVhbG1zL3ZpbWFwIiwiYXVkIjoiaHR0cHM6Ly9hY2NvdW50cy5tYXA0ZC52bi9hdXRoL3JlYWxtcy92aW1hcCIsInN1YiI6IjhlOTNmNWJiLTI5NGMtNGFiZi1hMmVkLTBlNDM3YjI5NDk0OSIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJtYXA0ZCIsImF1dGhfdGltZSI6MCwic2Vzc2lvbl9zdGF0ZSI6ImZiYTExMzk0LTI4ZDgtNDczZC04YzU1LTVkMmZkMTRmOTY0ZSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIn0.-lncBjRY9r3691DIv8phJAqC0K9sFDFKCdvjA_TLxrw",  # Thay YOUR_ACCESS_TOKEN_HERE bằng token của bạn
    "Content-Type": "application/json"
}
# Gửi từng POI một
for data_to_send in data_to_send_list:
    response = requests.post(url, headers=headers, json=data_to_send)
    if response.status_code == 200:
        print(f"POI '{data_to_send['name']}' đã được gửi thành công!")
    else:
        print(f"Lỗi khi gửi POI '{data_to_send['name']}': {response.status_code}")
        print(response.text)

    # Nếu bạn muốn có một khoảng thời gian chờ trước khi gửi POI tiếp theo, bạn có thể sử dụng sleep
    # import time
    # time.sleep(5)  # Chờ 5 giây trước khi gửi POI tiếp theo
