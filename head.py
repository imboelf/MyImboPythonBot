import requests
import json
from bs4 import BeautifulSoup
#
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
#
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
#
# req = requests.get(url, headers=headers)
#
# src = req.text
# ------------------------------create html-file------------------------------
# with open("index.html", "w", encoding='utf-8') as file:
#      file.write(src)

#------------------------------open html-file and create json------------------------------
# with open("index.html", encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
#
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
#
# all_categories_dict = {}
#
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru/" + item.get("href")
#     all_categories_dict[item_text] = item_href
#
# with open("all_categories_dict.json", "w", encoding="utf-8") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
#------------------------------open json------------------------------

with open("all_categories_dict.json", encoding="utf-8") as file:
    all_categories = json.load(file)
for category_name, category_href in all_categories.items():

    rep = [",", " ", "-", "_"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")
    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"{category_name}.html", "w", encoding="utf-8") as file:
        file.write(src)