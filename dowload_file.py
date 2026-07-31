import os
import glob
import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 1. Настройка путей
path_download_directory = r'C:\Python\autotest_selenium\file_download'

if not os.path.exists(path_download_directory):
    os.makedirs(path_download_directory)

# 2. Инициализация браузера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)

driver.get('https://practice-automation.com/file-download/')
driver.maximize_window()
time.sleep(2)

# 3. Поиск элемента кнопки и получение прямой ссылки
# Используем ваш XPath, но добавили ожидание
download_element = driver.find_element('xpath', '//*[@id="post-1042"]/div/div[1]/div/div/div/div[3]/a')
file_url = download_element.get_attribute('href')
print(f"Прямая ссылка на файл: {file_url}")

# 4. Скачивание файла через requests (в обход блокировок браузера)
response = requests.get(file_url, stream=True)

# Автоматически вытаскиваем реальное имя файла из ссылки ("sample.pdf")
file_name = file_url.split('/')[-1]

# ИСПРАВЛЕНО: os.path.join вместо сложения строк, чтобы избежать слипшихся путей
file_path = os.path.join(path_download_directory, file_name)

# Сохраняем файл на диск
with open(file_path, 'wb') as f:
    f.write(response.content)

print(f"Файл успешно скачан под именем: {file_name}")

# 5. Проверка наличия файла через assert
assert os.path.exists(file_path), f"Файл не найден по пути: {file_path}"
print("Файл успешно обнаружен в директории!")

# 6. Ваша проверка файлов в папке на пустоту
files = glob.glob(os.path.join(path_download_directory, "*.*"))

for file in files:
    file_size = os.path.getsize(file)
    # Берем базовое имя для красивого вывода в консоль
    short_name = os.path.basename(file)

    if file_size > 10:
        print(f"Файл '{short_name}' не пуст (Размер: {file_size} байт)")
    else:
        print(f"Файл '{short_name}' пуст (Размер: {file_size} байт)")
