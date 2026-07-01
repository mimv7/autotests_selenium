import datetime
import time
from argparse import Action

from  selenium import webdriver
from selenium.webdriver import ActionChains
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
password = driver.find_element('id', 'password')
password.send_keys(password_all)
button_login = driver.find_element('id', "login-button")
button_login.click() #клик по кнопке

url_inventory = 'https://www.saucedemo.com/inventory.html'
get_url_inventory = driver.current_url
print(get_url_inventory)
assert url_inventory == get_url_inventory, \
    f"Ожидался URL {url_inventory}, но открылся {get_url_inventory}"
print('ok')

#driver.execute_script('window.scrollTo( 0 , 200 )')# скролл на 200 пикселей
actions = ActionChains(driver)# каким драйвером мы будем двигаться
red_t_shirt = driver.find_element('xpath', '//button[contains(@id, "red")]')# локатор
actions.move_to_element(red_t_shirt).perform()# драйвер двигается к элементу и выполни

time.sleep(5)
now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()