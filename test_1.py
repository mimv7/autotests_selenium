from  selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

user_name = driver.find_element('id', 'user-name')
user_name.send_keys('standard_user')
password = driver.find_element('id', 'password')
password.send_keys('secret_sauce')
button_login = driver.find_element('id', "login-button")
button_login.click()


# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()