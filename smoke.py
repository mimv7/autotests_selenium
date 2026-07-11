import datetime
import time

from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Инициализируем настройки один раз
options = webdriver.ChromeOptions()

# Включаем отсоединение: браузер останется открытым после завершения скрипта
options.add_experimental_option("detach", True)

# Режим гостя (все сессии чистые, история не сохраняется)
options.add_argument("--guest")
# АЛЬТЕРНАТИВА: если гостевой режим работает некорректно, раскомментируйте строку ниже:
# options.add_argument("--incognito")

# Для фонового режима (без графического окна) раскомментируйте это:
# options.add_argument("--headless=new")

# Запуск браузера (в Selenium 4+ Service() автоматически найдет chromedriver)
driver = webdriver.Chrome(service=Service(), options=options)


driver.get('https://www.saucedemo.com/')
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'
#autorization
user_name = driver.find_element('id', 'user-name')
user_name.send_keys(login_standard_user)
password = driver.find_element('id', 'password')
password.send_keys(password_all)
button_login = driver.find_element('id', "login-button")
button_login.click() #клик по кнопке

#info product 1
product_1 = driver.find_element('xpath', '//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(f'value_product_1 - {value_product_1}')
price_1 = driver.find_element('xpath', '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_1 = price_1.text
print(f'value_price_1 - {value_price_1}')

#select product 1
select_product_1 = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print('select_product_1')

#info product 2
product_2 = driver.find_element('xpath', '//a[@id="item_0_title_link"]')
value_product_2 = product_2.text
print(f'value_product_1 - {value_product_2}')
price_2 = driver.find_element('xpath', '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
value_price_2 = price_2.text
print(f'value_price_2 - {value_price_2}')

#select product 2
select_product_2 = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bike-light"]')
select_product_2.click()
print('select_product_2')

#open shopping cart
cart = driver.find_element('xpath','//*[@id="shopping_cart_container"]')
cart.click()
print('open cart')

#info cart
cart_product_1 = driver.find_element('xpath', '//a[@id="item_4_title_link"]')
value_cart_product_1 = cart_product_1.text
print(f'value_cart_product_1 - {value_cart_product_1}')
cart_price_1 = driver.find_element('xpath', '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_1 = cart_price_1.text
print(f'value_cart_price_1 - {value_cart_price_1}')

cart_product_2 = driver.find_element('xpath','//a[@id="item_0_title_link"]')
value_cart_product_2 = cart_product_2.text
print(f'value_cart_product_2 - {value_cart_product_2}')
cart_price_2 = driver.find_element('xpath','//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_cart_price_2 = cart_price_2.text
print(f'value_cart_price_2 - {value_cart_price_2}')

#assert
assert value_product_1 == value_cart_product_1
print('\n assert value card - ok')
assert value_price_1 == value_cart_price_1
print('\n assert price - ok\n')

assert value_product_2 == value_cart_product_2
print('\n assert value card - ok')
assert value_price_2 == value_cart_price_2
print('\n assert price - ok\n')

button_checkout = driver.find_element('xpath', '//button[@id="checkout"]')
button_checkout.click()
print('button checkout click')

#select user info
first_name = driver.find_element('xpath','//input[@id="first-name"]')
first_name.send_keys('Roman')
print('input Roman')
last_name = driver.find_element('xpath', '//input[@id="last-name"]')
last_name.send_keys('Meleshin')
print('input Meleshin')
zip_code = driver.find_element('xpath','//input[@id="postal-code"]')
zip_code.send_keys('1234')
print('input zip code')
button_continue = driver.find_element('xpath', '//input[@id="continue"]')
button_continue.click()
print('btn continue click')

#finish product 1
finish_product_1 = driver.find_element('xpath','//a[@id="item_4_title_link"]')
value_finish_product_1 = finish_product_1.text
print(f'value_finish_product_1 {value_finish_product_1}')
finish_price_1 = driver.find_element('xpath','//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_finish_price_1 = finish_price_1.text
print(f'value_finish_price_1 {value_finish_price_1}')

#finish product 2
finish_product_2 = driver.find_element('xpath', '//a[@id="item_0_title_link"]')
value_finish_product_2 = finish_product_2.text
print(f'value_finish_product_2 - {value_finish_product_2}')
finish_price_2 = driver.find_element('xpath','//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_finish_price_2 = finish_price_2.text
print(f'value_finish_price_2 - {value_finish_price_2}')

#assert
assert value_product_1 == value_finish_product_1
print('\n assert finish droduct 1 - ok')
assert value_price_1 == value_finish_price_1
print('\n assert finish price 1 - ok \n')

assert value_product_2 == value_finish_product_2
print('\n assert finish droduct 2 - ok')
assert value_price_2 == value_finish_price_2
print('\n assert finish price 2 - ok \n')

total_price =driver.find_element('xpath','//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_total_price = total_price.text
print(f'value_total_price - {value_total_price}')


#summ price 2 product
price_1 = float(value_price_1.replace('$',''))
price_2 = float(value_price_2.replace('$',''))
control_summ_price = price_1 + price_2
print(control_summ_price)
content_summ_price = f'Item total: ${control_summ_price:.2f}'

assert  content_summ_price == value_total_price
print('assert total price - ok')


now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)

# Скрипт остановится и будет ждать нажатия Enter в терминале
input("Нажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()