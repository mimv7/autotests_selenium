import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Настройки браузера
options = webdriver.ChromeOptions()

# Убираем "detach", так как в конце кода у вас и так стоит input() для удержания процесса.
# Добавляем аргументы для стабильности сетевых соединений в Chrome 115+:
options.add_argument("--guest")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-allow-origins=*")

# Запуск браузера
driver = webdriver.Chrome(service=Service(), options=options)
wait = WebDriverWait(driver, 15)  # Увеличили таймаут для тяжелого сайта SauceLabs

# Логика автоматизации
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

# Используем явные ожидания вместо жестких локаторов, чтобы избежать падений
user_name = wait.until(EC.element_to_be_clickable((By.ID, 'user-name')))
user_name.send_keys(login_standard_user)
print('input login')

password = driver.find_element(By.ID, 'password')
password.send_keys(password_all)
print('input pass')

button_login = driver.find_element(By.ID, "login-button")
button_login.click()
print('click on the button')

# Открываем бургер-меню
menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
menu.click()
print('open menu')

# Ожидаем, пока ссылка в меню станет видимой и кликабельной
link_about = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id="about_sidebar_link"]')))

# Кликаем через JavaScript, чтобы предотвратить "ConnectionResetError" и "Target frame detached"
driver.execute_script("arguments[0].click();", link_about)
print('open about')

# Ждем, пока URL изменится на сайт Sauce Labs и страница полностью загрузится
wait.until(EC.url_contains("saucelabs.com"))
time.sleep(3)  # Даем секунды на стабилизацию рендеринга

print('go back')
driver.back()
# Ждем возврата на saucedemo
wait.until(EC.url_to_be(base_url + "inventory.html"))
time.sleep(2)

print('go forward')
driver.forward()
# Ждем перехода обратно на saucelabs
wait.until(EC.url_contains("saucelabs.com"))
time.sleep(2)

# Проверка URL (используем endswith или вхождение, так как сайт может редиректить на локализованные поддомены)
get_url_saucelabs = driver.current_url
print(f"Текущий URL: {get_url_saucelabs}")
assert "saucelabs.com" in get_url_saucelabs, \
    f"Ожидался URL, содержащий saucelabs.com, но открылся {get_url_saucelabs}"
print('ok')

# Скриншот
now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = f'screenshot_{now_date}.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' + name_screenshot)

# Остановка для ручной проверки
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()
