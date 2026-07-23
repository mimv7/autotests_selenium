import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from test_back_forward import wait

# Инициализируем настройки один раз
options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

options.add_argument("--guest")

driver = webdriver.Chrome(service=Service(), options=options)

# Логика автоматизации
base_url = 'https://www.testmuai.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.maximize_window()

time.sleep(5)

# 1. Ждем загрузки iframe и переключаемся внутрь него
iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
driver.switch_to.frame(iframe)

# 2. Теперь ищем элемент внутри iframe
content_table = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="__next"]//div[@class="rsw-ce"]')))
value_content_table = content_table.text
print(value_content_table)
content_table.click()
content_table.send_keys(Keys.CONTROL + 'a')

click_edit_bold = driver.find_element('xpath','//button[@title="Bold"]')
click_edit_bold.click()
print('click editor bold')


bold_value_content_table = driver.find_element('xpath','//*[@id="__next"]/div/div/div[2]/b')
assert value_content_table == bold_value_content_table
print('ok')


# 3. Если нужно продолжить работу с основной страницей, возвращаем контекст:
driver.switch_to.default_content()

'''now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)'''

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()