from  selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element('id', 'user-name')
user_name.send_keys(login_standard_user)
password = driver.find_element('id', 'password')
password.send_keys(password_all)
button_login = driver.find_element('id', "login-button")
button_login.click()

url_inventory = 'https://www.saucedemo.com/inventory.html'
get_url_inventory = driver.current_url
print(get_url_inventory)
assert url_inventory == get_url_inventory, \
    f"Ожидался URL {url_inventory}, но открылся {get_url_inventory}"
print('ok')

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()