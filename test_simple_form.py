import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Инициализируем настройки один раз
options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

options.add_argument("--guest")

driver = webdriver.Chrome(service=Service(), options=options)

# Логика автоматизации
base_url = 'https://www.testmuai.com/selenium-playground/simple-form-demo/'
driver.get(base_url)
driver.maximize_window()

time.sleep(2)

input_pole = driver.find_element('xpath', '//input[@id="user-message"]')
input_pole.click()
print('click input pole')
message_for_input_pole = '123'
input_pole.send_keys(message_for_input_pole)

button_get_value = driver.find_element('xpath','//button[contains(text(),"Get Checked Value")]')
button_get_value.click()
print('click button "Get Checked Value"')

pole_message = driver.find_element('xpath','//p[@id="message"]')
value_pole_message = pole_message.text

assert message_for_input_pole == value_pole_message
print('ok')

'''now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)'''

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()