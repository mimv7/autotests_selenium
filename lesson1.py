from  selenium import webdriver


driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element('xpath', '//*[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('input login')
password = driver.find_element('css selector', '#password')
password.send_keys(password_all)
print('input password')

button_login = driver.find_element('xpath', "//input[@value='Login']")
button_login.click()
print('click to the button')

url_inventory = 'https://www.saucedemo.com/inventory.html'
get_url_inventory = driver.current_url
print(get_url_inventory)
assert url_inventory == get_url_inventory, f"Ожидался URL {url_inventory}, но открылся {get_url_inventory}"



# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()