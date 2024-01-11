from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.chrome.service import Service
from time import sleep

edge_driver_path = r"D:\PycharmProject\crawl\.venv\msedgedriver.exe"
service_obj = Service(edge_driver_path)
#options = webdriver.EdgeOptions()
#options.add_argument('--headless')
browser = webdriver.Edge(service=service_obj)
start_value = 9430703500
end_value =   9430703510
with open('test.csv', 'w', newline='', encoding='utf-8') as file_output:
    headers = ['id', 'name', 'pluscode']  # Corrected field names
    writer = csv.DictWriter(file_output, delimiter=',', lineterminator='\n', fieldnames=headers)
    writer.writeheader()
    for cell_value in range(start_value,end_value + 1):
        browser.get(f"https://diachiso.gov.vn/#/map/{cell_value}")
        browser.refresh()
        sleep(0.5)
        page_source = browser.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        # Extract the text from the specific elements within the div
        detail_code_elem = soup.find('p', class_='detail-code')
        name_elem = soup.find('p', class_='ng-star-inserted', style='font-size: 14px; line-height: 20px;')
        pluscode_elem = soup.find('p', class_='ng-star-inserted',
                                  style='font-size: 13px; line-height: 20px; color: rgb(121, 121, 121);')
        detail_code = detail_code_elem.text.strip() if detail_code_elem else 'N/a'
        name = name_elem.text.strip() if name_elem else 'N/a'
        pluscode = pluscode_elem.text.strip() if pluscode_elem else 'N/a'

        print(f"https://diachiso.gov.vn/#/map/{cell_value}")
        print(detail_code)
        writer.writerow({'id': detail_code, 'name': name, 'pluscode': pluscode})
# Close the browser when done
browser.quit()
