import datetime
import time

from  selenium import webdriver
from selenium.webdriver import ActionChains
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
elements_buttons = driver.find_element('xpath', '//*[@id="item-4"]/a')
elements_buttons.click()
time.sleep(2)
print('click elements_buttons')

action =ActionChains(driver)
double_click_me = driver.find_element('xpath','//button[@id="doubleClickBtn"]')
action.double_click(double_click_me).perform()
expected_double_click = 'You have done a double click'
received_double_click = driver.find_element('xpath','//p[@id="doubleClickMessage"]')
value_received_double_click =received_double_click.text
assert expected_double_click == value_received_double_click,\
f'expect {expected_double_click} received {value_received_double_click}'
print('aseert double_click_me -ok')


right_click_me =driver.find_element('xpath','//button[@id="rightClickBtn"]')
action.context_click(right_click_me).perform()
expected_right_click_me = 'You have done a right click'
received_right_click_me = driver.find_element('xpath','//p[@id="rightClickMessage"]')
value_received_right_click_me =received_right_click_me.text
assert expected_right_click_me == value_received_right_click_me,\
f'expect {expected_right_click_me} received {value_received_right_click_me}'
print('aseert double_click_me -ok')







'''now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)'''

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()