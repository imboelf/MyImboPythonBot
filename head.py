import csv
import random
from time import sleep
from body import headers, json, requests, BeautifulSoup

with open("all_categories_dict.json", encoding="UTF-8-sig") as file:
    all_categories = json.load(file)

iteration_count = int(len(all_categories)) - 1
count = 0
print(f'Всего итераций: {iteration_count}')
for category_name, category_href in all_categories.items():

    rep = [",", " ", "-", "_"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")
    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{category_name}.html", "w", encoding="UTF-8") as file:
        file.write(src)

    with open(f"data/{count}_{category_name}.html", encoding="UTF-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    product_info = []

    for item in products_data:
        product_tds = item.find_all("td")

        title = product_tds[0].find("a").text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbonhydrates = product_tds[4].text


        product_info.append(
            {
                "Title" : title,
                "Calories" : calories,
                "Proteins" : proteins,
                "Fats" : fats,
                "Carbonhydrates" : carbonhydrates

            }
        )
        with open(f"data/{count}_{category_name}.csv", "a", encoding="UTF-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title, calories, proteins, fats, carbonhydrates
                )
            )
        with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
            json.dump(product_info, file, indent=4, ensure_ascii=False)
    count += 1
    print(f'#Итерация {count}, {category_name} записан...')
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print(f'Работа завершена')
        break

    print(f'Осталось итераций {iteration_count}')
    sleep(random.randrange(2, 4))