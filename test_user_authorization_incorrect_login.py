from  selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
'''options.add_argument("--headless=new")'''
driver = webdriver.Chrome(options=options)

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

login_incorrect_user = 'standard_use'
password_all = 'secret_sauce'

user_name = driver.find_element('id', 'user-name')
user_name.send_keys(login_incorrect_user)
password = driver.find_element('id', 'password')
password.send_keys(password_all)
button_login = driver.find_element('id', "login-button")
button_login.click()

warning_text_received = driver.find_element('xpath', "//h3[@data-test='error']")
value_warning_text_received = warning_text_received.text


warning_text_expected = 'Epic sadface: Username and password do not match any user in this service'
assert warning_text_expected == value_warning_text_received, \
    f"Ожидался URL {warning_text_expected}, но открылся {warning_text_received}"
print('ok')
#driver.refresh()

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()