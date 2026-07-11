import datetime
import time

from  selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

base_url = 'https://demoqa.com/'
driver.get(base_url)
driver.maximize_window()

category_elements = driver.find_element('xpath', '//*[@id="root"]/div/div/div[2]/div/a[1]')
category_elements.click()
print('click category_elements')
time.sleep(2)
elements_checkbox = driver.find_element('xpath', '//*[@id="item-1"]')
elements_checkbox.click()
time.sleep(2)
print('click elements_checkbox')

checkbox_home = driver.find_element('xpath','//span[@class = "rc-tree-checkbox"]')
checkbox_home.click()

value_checkbox_home_result ='You have selected :'
checkbox_home_result = driver.find_element('xpath','//*[@id="result"]/span[1]')
get_checkbox_home_result = checkbox_home_result.text
assert  value_checkbox_home_result == get_checkbox_home_result
print('value_checkbox_home_result - ok')

reveal_checkbox_home = driver.find_element('xpath','//span[@class="rc-tree-switcher rc-tree-switcher_close"]')
reveal_checkbox_home.click()
print('click reveal_checkbox_home')

'''now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)'''

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()