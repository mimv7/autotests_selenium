import datetime
import time

from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)  # не закрывать браузер

# --- БЛОКИРОВКА МЕНЕДЖЕРА ПАРОЛЕЙ И АВТОЗАПОЛНЕНИЯ ---
prefs = {
    "credentials_enable_service": False,     # Отключить службу учетных данных
    "profile.password_manager_enabled": False # Отключить сам менеджер паролей
}
options.add_experimental_option("prefs", prefs)

# Остальные фиксы для стабильности (от крашей)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.use_automation_extension = False
# ----------------------------------------------------
#options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element('id', 'user-name')
user_name.send_keys(login_standard_user)
print('input login')

password = driver.find_element('id', 'password')
password.send_keys(password_all)
print('input pass')

button_login = driver.find_element('id', "login-button")
button_login.click() #клик по кнопке
print('click on the button')


menu = driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]')
menu.click()
print('open menu')
time.sleep(3)

link_about = driver.find_element('xpath', '//a[@id="about_sidebar_link"]')
link_about.click()
time.sleep(5)
print('open about')

url_saucelabs = 'https://saucelabs.com/'
get_url_saucelabs = driver.current_url
print(get_url_saucelabs)
assert  url_saucelabs == get_url_saucelabs , \
    f"Ожидался URL {url_saucelabs}, но открылся {get_url_saucelabs}"
print('ok')
time.sleep(3)



now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()