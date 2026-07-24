import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
options = Options()
#options.add_argument('__headless=new')

base_url = 'https://demoqa.com/alerts'
driver.get(base_url)
driver.maximize_window()

btn_alert = driver.find_element('xpath','//button[@id="alertButton"]')
btn_alert.click()
print('click alert button')
driver.switch_to.alert.accept()
time.sleep(2)

btn_confirm = driver.find_element('xpath','//button[@id="confirmButton"]')
btn_confirm.click()
print('click confirm button')
driver.switch_to.alert.dismiss()
control_tex_dismiss = 'You selected Cancel'
text_cancel = driver.find_element('xpath','//span[@id="confirmResult"]')
value_text_cancel = text_cancel.text
print(value_text_cancel)

assert  control_tex_dismiss == value_text_cancel
print('asssert dismiss text ok')
time.sleep(2)
btn_confirm.click()
driver.switch_to.alert.accept()
control_text_confirm ='You selected Ok'
text_confirm = driver.find_element('xpath','//span[@id="confirmResult"]')
value_text_confirm =text_confirm.text
print(value_text_confirm)

assert control_text_confirm == value_text_confirm
print('assert confirm text ok')

'''now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)'''

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()