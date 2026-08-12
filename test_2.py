import datetime
import time

from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')



login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element('id', 'user-name')
user_name.send_keys(login_standard_user)
password = driver.find_element('id', 'password')
password.send_keys(password_all)
button_login = driver.find_element('id', "login-button")
button_login.click() #клик по кнопке'''


print('\tПриветствую тебя в нашем интернет - магазине')
print('Выбери один из следующих товаров и укажи его номер:'
      '\n Sauce Labs Backpack - 1' 
      '\n Sauce Labs Bike Light - 2'
      '\n Sauce Labs Bolt T-Shirt - 3'
      '\n Sauce Labs Fleece Jacket - 4'
      '\n Sauce Labs Onesie - 5'
      '\n Test.allTheThings() T-Shirt (Red) - 6')
num_product = input()
if num_product == '1':
    print('Sauce Labs Backpack')
    product_1 = driver.find_element('xpath', '//a[@id="item_4_title_link"]')
    value_product = product_1.text
    print(f'value_product - {value_product}')
    price = driver.find_element('xpath', '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    value_price = price.text
    print(f'value_price - {value_price}')
    # select product 1
    select_product_1 = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]')
    select_product_1.click()
    print('select_product_1')
    # open shopping cart
    cart = driver.find_element('xpath', '//*[@id="shopping_cart_container"]')
    cart.click()
    print('open cart')
    # info cart
    cart_product = driver.find_element('xpath', '//a[@id="item_4_title_link"]')
    value_cart_product = cart_product.text
    print(f'value_cart_product_1 - {value_cart_product}')
    cart_price = driver.find_element('xpath','//div[@class="inventory_item_price"]')
    value_cart_price = cart_price.text
    print(f'value_cart_price_1 - {value_cart_price}')
    # assert
    assert value_product == value_cart_product
    print('\n assert value card - ok')
    assert value_price == value_cart_price
    print('\n assert price - ok\n')

elif  num_product == '2':
    print('Sauce Labs Bike Light')
    product_2 = driver.find_element('xpath', '//a[@id="item_4_title_link"]')
    value_product_2 = product_2.text
    print(f'value_product_2 - {value_product_2}')
    price_2 = driver.find_element('xpath', '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    value_price_2 = price_2.text
    print(f'value_price_1 - {value_price_2}')
    # select product 2
    select_product_2 = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]')
    select_product_2.click()
    print('select_product_2')
    # open shopping cart
    cart = driver.find_element('xpath', '//*[@id="shopping_cart_container"]')
    cart.click()
    print('open cart')
    # info cart
    cart_product_2 = driver.find_element('xpath', '//a[@id="item_4_title_link"]')
    value_cart_product_2 = cart_product_2.text
    print(f'value_cart_product_2 - {value_cart_product_2}')
    cart_price_2 = driver.find_element('xpath', '//div[@class="inventory_item_price"]')
    value_cart_price_2 = cart_price_2.text
    print(f'value_cart_price_2 - {value_cart_price_2}')
    # assert
    assert value_product_2 == value_cart_product_2
    print('\n assert value card - ok')
    assert value_price_2 == value_cart_price_2
    print('\n assert price - ok\n')

elif num_product == '3':
    print('Sauce Labs Bolt T-Shirt')
elif num_product == '4':
    print('Sauce Labs Fleece Jacket')
elif num_product == '5':
    print('Sauce Labs Onesie')
elif num_product == '6':
    print('Test.allTheThings() T-Shirt (Red)')
else:
    print('Вы выбрали что то не то')
#------------------------------------

driver.implicitly_wait(10)

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
finish_product = driver.find_element('xpath','//a[@id="item_4_title_link"]')
value_finish_product = finish_product.text
print(f'value_finish_product {value_finish_product}')
finish_price = driver.find_element('xpath','//div[@class="inventory_item_price"]')
value_finish_price = finish_price.text
print(f'value_finish_price {value_finish_price}')

#assert
assert value_product == value_finish_product
print('\n assert finish product - ok')
assert value_price == value_finish_price
print('\n assert finish price - ok \n')


total_price =driver.find_element('xpath','//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_total_price = total_price.text
print(f'value_total_price - {value_total_price}')


price = float(value_price.replace('$',''))
control_summ_price = price
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