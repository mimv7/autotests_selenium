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
elements_radiobutton = driver.find_element('xpath', '//*[@id="item-2"]/a')
elements_radiobutton.click()
time.sleep(2)
print('click elements_Radiobutton')

radio_button_yes = driver.find_element('xpath', '//input[@id="yesRadio"]')
radio_button_yes.click()
if radio_button_yes.is_selected():
    print('on click yes')
else:
    print('not click yes')

radio_button_impressiveRadio =driver.find_element('xpath', '//input[@id="impressiveRadio"]')
radio_button_impressiveRadio.click()
print(' click radio_button_impressiveRadio')
if radio_button_yes.is_selected():
    print('on click yes')
else:
    print('not click yes')





'''now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)'''

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()