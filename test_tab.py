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

category_windows = driver.find_element('xpath', '//*[@id="root"]/div/div/div[2]/div/a[3]')
category_windows.click()
print('click category windows')
time.sleep(2)
elements_browser = driver.find_element('xpath', '//span[contains(text(),"Browser Windows")]')
elements_browser.click()
time.sleep(2)
print('click elements_browser')

btn_new_tab = driver.find_element('xpath','//button[@id="tabButton"]')
btn_new_tab.click()
print('click new tab')
time.sleep(2)
print(driver.current_url)
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)

btn_new_window = driver.find_element('xpath','//button[@id="windowButton"]')
btn_new_window.click()
print('click new window')
driver.switch_to.window(driver.window_handles[2])
print(driver.current_url)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)






'''now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)'''

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()