import os
import glob
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 1. Настройка путей
path_download_directory = r'C:\Python\autotest_selenium\file_download'

if not os.path.exists(path_download_directory):
    os.makedirs(path_download_directory)

# Предварительно чистим папку от прошлых неудачных тестов
for f in glob.glob(os.path.join(path_download_directory, "*")):
    try: os.remove(f)
    except: pass

# 2. Обычная инициализация настроек
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Базовая маскировка от блокировок сайта (ошибка 429)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(service=Service(), options=options)

# --- ЖЕСТКАЯ КОМАНДА CDP ДЛЯ ОБХОДА ВСЕХ БЛОКИРОВОК ХРОМА ---
# Переопределяем поведение загрузки на уровне самого движка Chromium
driver.execute_cdp_cmd("Page.setDownloadBehavior", {
    "behavior": "allow", # Разрешить абсолютно всё
    "downloadPath": path_download_directory
})

driver.get('https://practice-automation.com/file-download/')
driver.maximize_window()
time.sleep(3)

# 3. Клик по кнопке скачивания
download_element = driver.find_element(By.XPATH, '//*[@id="post-1042"]/div/div/div/div/div/div/a')
download_element.click()
print("Клик выполнен через Selenium. Ожидаем завершения скачивания...")

# 4. Ожидание появления файла (20 секунд)
file_path = os.path.join(path_download_directory, "sample.pdf")
downloaded = False

for _ in range(20):
    files = os.listdir(path_download_directory)
    # Если Chrome всё еще качает временный файл .crdownload, ждем дальше
    if any(f.endswith('.crdownload') for f in files):
        time.sleep(1)
        continue
    # Если файл успешно лег на диск
    if os.path.exists(file_path):
        downloaded = True
        break
    time.sleep(1)

# 5. Проверка результатов тестом
file_name = "test.pdf"    #имя ожидаемого файла

file_path = path_download_directory + file_name    #путь до ожидаемого файла + имя файла
assert os.access(file_path, os.F_OK) == True    #проведение проверки на наличие файла
print("Файл в директории")