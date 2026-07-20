import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Инициализируем настройки один раз
options = webdriver.ChromeOptions()

# Включаем отсоединение: браузер останется открытым после завершения скрипта
options.add_experimental_option("detach", True)

# Режим гостя (все сессии чистые, история не сохраняется)
options.add_argument("--guest")
# АЛЬТЕРНАТИВА: если гостевой режим работает некорректно, раскомментируйте строку ниже:
# options.add_argument("--incognito")

# Для фонового режима (без графического окна) раскомментируйте это:
# options.add_argument("--headless=new")

# Запуск браузера (в Selenium 4+ Service() автоматически найдет chromedriver)
driver = webdriver.Chrome(service=Service(), options=options)

# Логика автоматизации
base_url = 'https://www.testmuai.com/selenium-playground/simple-form-demo/'
driver.get(base_url)
driver.maximize_window()

time.sleep(5)

'''now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)'''

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()