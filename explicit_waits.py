from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

driver =webdriver.Chrome()
options = Options()
#options.add_argument('__headless=new')
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)


#driver.implicitly_wait(10)
button_after_5 =   WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//button[@id="visibleAfter"]')))
button_after_5.click()
print('click btn after 5 seconds')

input('enter click')
driver.quit()