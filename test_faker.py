import datetime
import time

from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
from faker import Faker

# Инициализируем генератор.
# Передаем 'ru_RU', чтобы имена, адреса и телефоны генерировались на русском языке
faker = Faker('en_US')

options = Options()
#options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_user = faker.first_name()
print(login_user)

password = faker.password(length=8)
print(password)

user_name = driver.find_element('id', 'user-name')
user_name.send_keys(login_user)
password_field = driver.find_element('id', 'password')
password_field.send_keys(password)

now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()