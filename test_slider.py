import datetime

from  selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
base_url = 'https://www.schoolsw3.com/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)
slider = driver.find_element('xpath', '//input[@id="id2"]')
action.click_and_hold(slider).move_by_offset(70,0).release().perform()



'''now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)
'''
# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()