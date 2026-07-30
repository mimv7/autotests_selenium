import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
options= Options()
#options.add_argument('__headless=new')

base_url = 'https://www.testmuai.com/selenium-playground/upload-file-demo/'
driver.get(base_url)
driver.maximize_window()
time.sleep(2)

path_to_file = 'C:/Python/autotest_selenium/file_upload/image.jpg'
button_file = driver.find_element('xpath','//input[@id="file"]')
button_file.send_keys(path_to_file)
print('file domnload')

test_text = 'File Successfully Uploaded'
text_successfully = driver.find_element('xpath', '//div[@id="error"]')
value_text_successfully = text_successfully.text
print(f'value {value_text_successfully}')

assert  test_text == value_text_successfully
print('file dowload ok')

input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()