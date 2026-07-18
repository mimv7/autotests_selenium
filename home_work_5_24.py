import datetime
import time

from  selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options


options = Options()
#options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

base_url = 'https://demoqa.com/'
driver.get(base_url)
driver.maximize_window()

category_widgets = driver.find_element('xpath', '//*[@id="root"]/div/div/div[2]/div/a[4]')
category_widgets.click()
print('click category widgets')

time.sleep(2)
elements_data_picker = driver.find_element('xpath', '/html/body/div/div/div/div/div[1]/div/div/div[4]/div/ul/li[3]')
elements_data_picker.click()
time.sleep(2)
print('click elements data picker')

select_date = driver.find_element('xpath', '//input[@id="datePickerMonthYearInput"]')
select_date.send_keys(Keys.CONTROL + 'a')
select_date.send_keys(Keys.BACKSPACE)
time.sleep(2)
select_date.send_keys('06/18/2026')
time.sleep(2)
select_date.send_keys(Keys.RETURN)
time.sleep(2)
print('select date 06/18/2026')

select_date.click()
time.sleep(2)
date_19_06_2026 = driver.find_element( 'xpath', '//div[contains(@aria-label, "June 18th, 2026")]')
date_19_06_2026.click()
print('select date 06/19/2026')

select_date.send_keys(Keys.CONTROL + 'a')
select_date.send_keys(Keys.BACKSPACE)
time.sleep(2)
select_date.click()
now_date_picker = driver.find_element('xpath', '//div[contains(@class,react-datepicker__day--today )]')
now_date_picker.click()
print('select now date')

select_date.click()
now_date = datetime.datetime.now().strftime("%d")
next_day_int = int(now_date) + 1
locator_next_day = f'//div[contains(@aria-label, "July {str(next_day_int)}th, 2026")]'
next_day = driver.find_element('xpath',locator_next_day)
next_day.click()
print('select next day')








'''now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)'''

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()