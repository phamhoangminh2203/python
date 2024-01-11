import pandas as pd
import requests

# Đọc danh sách ID từ tệp Excel, bắt đầu từ dòng thứ 2 của cột A
df = pd.read_excel(r'D:\PycharmProject\pythonProject\.venv\lutru\typemap.xlsx', engine='openpyxl', header=None, names=['ID'])

# Đường dẫn API cơ bản
base_url = "https://api-data.map4d.vn/map/manage/place/delete/"

# Token của bạn
token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJNMUtocHl1OGg1cjlxVkNfN29hbDJaUERseU9CRjJMazkwdlVBS2hTNko0In0.eyJqdGkiOiIyMjE1ODYwZS1iNTgyLTRiOWQtYWNkNi1lODdhY2NiYzgyMjYiLCJleHAiOjE3MDU2NDAxMjgsIm5iZiI6MCwiaWF0IjoxNzA0Nzc2MTI4LCJpc3MiOiJodHRwczovL2FjY291bnRzLm1hcDRkLnZuL2F1dGgvcmVhbG1zL3ZpbWFwIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjhlOTNmNWJiLTI5NGMtNGFiZi1hMmVkLTBlNDM3YjI5NDk0OSIsInR5cCI6IkJlYXJlciIsImF6cCI6Im1hcDRkIiwiYXV0aF90aW1lIjoxNzA0Nzc2MTI4LCJzZXNzaW9uX3N0YXRlIjoiZmJhMTEzOTQtMjhkOC00NzNkLThjNTUtNWQyZmQxNGY5NjRlIiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJNaeG7gW4gTmFtIFRlYW1EYXRhIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiZGF0YS1taWVubmFtQG1hcDRkLnZuIiwiZ2l2ZW5fbmFtZSI6Ik1p4buBbiBOYW0iLCJmYW1pbHlfbmFtZSI6IlRlYW1EYXRhIiwiZW1haWwiOiJkYXRhLW1pZW5uYW1AbWFwNGQudm4ifQ.Z3FAruPVtQWyn0bP8TX8Oy_vURiMnUOnGLP8v_VCFJRc92vkKJkdWDHmCpFFfKdWWfvf1GI3AVhuPnzUvlgtu1xELZvYsiAwlDxiv79RlI1s8cMxZt_O4mnClAArVL4KS5d4iYbWlE7v_3xK0EIMp8JFTcXdwsCx02jRzEJbrFfIxBa_6yVmvc8klS1yG7QSjkcSlNdVOtsdMfytKKhMYe-8AymDTqNl9ofGJm-zEYE-bCl05Pt-ip0tap4g9w5qlsimUNouWgPXkCMKsKfJjO89JiI3UdqsFXOPSIpsSE-ROegJ4pmniV-KOgIk81QMiVLBw-lES3tDySYRKNJmxg"  # Hãy cập nhật token của bạn ở đây

# Loop qua từng ID trong DataFrame và thực hiện yêu cầu DELETE
for idx, row in df.iterrows():
    place_id = row['ID']  # Lấy ID từ cột 'ID'
    full_url = base_url + place_id
    headers = {"accept": "text/plain", "Authorization": f"Bearer {token}"}

    response = requests.delete(full_url, headers=headers)

    print(f"Processed ID: {place_id}, Status Code: {response.status_code}, Response: {response.text}")
