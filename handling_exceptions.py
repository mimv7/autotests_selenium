import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
options = Options()
#options.add_argument('__headless=new')
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()

try:
    visible_after = driver.find_element('xpath', '//button[@id="visibleAfter"]')
    visible_after.click()

except NoSuchElementException:
    print('error NoSuchElementException')
    time.sleep(7)
    visible_after = driver.find_element('xpath', '//button[@id="visibleAfter"]')
    visible_after.click()


print('click visible after ')

input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()