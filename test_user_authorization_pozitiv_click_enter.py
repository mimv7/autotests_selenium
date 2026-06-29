import time

from  selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element('id', 'user-name')
user_name.send_keys(login_standard_user)
time.sleep(5)
user_name.send_keys(Keys.BACKSPACE) # удаляем последний символ
time.sleep(5)
user_name.send_keys('r') #добавляем к концу
password = driver.find_element('id', 'password')
password.send_keys(password_all)
password.send_keys(Keys.RETURN) # после ввода пароль нажимаем enter

url_inventory = 'https://www.saucedemo.com/inventory.html'
get_url_inventory = driver.current_url
print(get_url_inventory)
assert url_inventory == get_url_inventory, \
    f"Ожидался URL {url_inventory}, но открылся {get_url_inventory}"
print('ok')

#Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()