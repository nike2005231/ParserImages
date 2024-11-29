import requests
from bs4 import BeautifulSoup
import os

headers = {
    "user-agent" : "aosdbh23b87dno2q7d8wgo123ewdaih3lky3whdbo8bx",
    "Accept" : "application/json"
}

list_link = []
def parse_link_image(num_page: int):
    global list_link
    link = rf"https://wallpapershq.ru/categories/all/3840x2160?page={num_page}"
    main_request = requests.get(link, headers=headers)
    flag = 1
    print("...Ожидайте, идет генерация ссылок...")
    for num in range(1, 31):

        soup = BeautifulSoup(main_request.content, "lxml")

        image_link_page_download_0 = soup.find("div", class_ = f"list-wallpapers__item order-{num}0 row-3")
        image_link_page_download_1 = image_link_page_download_0.find('a')['href']

        request_page_download = requests.get(image_link_page_download_1, headers=headers)
        soup_download = BeautifulSoup(request_page_download.content, "lxml")
        image_download_link = soup_download.find('a', class_ = 'download-btn')['href']
        list_link.append(image_download_link)

    folder_name = "downloaded_images"
    os.makedirs(folder_name, exist_ok=True)
    for index, img_link in enumerate(list_link, start=1):
        img_data = requests.get(img_link).content
        with open(f"{folder_name}/image_{index}.jpg", "wb") as img_file:
            img_file.write(img_data)
        print(f"Загружено {index} изображение")


parse_link_image(2)