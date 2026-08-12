import datetime
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 1. Настройка браузера
options = Options()
options.add_argument("--guest")
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get('https://saucedemo.com')

# 2. Авторизация
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

# 3. Интерактивное меню в консоли
print('\tПриветствую тебя в нашем интернет-магазине')
print('Выбери один из следующих товаров и укажи его номер:'
      '\n Sauce Labs Backpack - 1' 
      '\n Sauce Labs Bike Light - 2'
      '\n Sauce Labs Bolt T-Shirt - 3'
      '\n Sauce Labs Fleece Jacket - 4'
      '\n Sauce Labs Onesie - 5'
      '\n Test.allTheThings() T-Shirt (Red) - 6'
      '\n')
num_product = input()

# Проверка ввода: если пользователь ввел не число или вышел за рамки 1-6
if not num_product.isdigit() or not (1 <= int(num_product) <= 6):
    print('\n[!] Ошибка: Введен неверный номер товара. Завершение работы.')
    driver.quit()
    sys.exit()

# Конвертируем в синтаксис XPATH (где индексация элементов начинается с 1)
index = int(num_product)

# === ТРИ УНИВЕРСАЛЬНЫХ ЛОКАТОРА (на основе f-строк и индексов) ===
# Находим нужную карточку товара по счету, а внутри нее берем название, цену или кнопку
product_title_xpath = f'(//div[@class="inventory_item"])[{index}]//div[@class="inventory_item_name "]'
product_price_xpath = f'(//div[@class="inventory_item"])[{index}]//div[@class="inventory_item_price"]'
add_to_cart_xpath = f'(//div[@class="inventory_item"])[{index}]//button'

# 4. Сбор данных на главной странице (динамически)
product_element = driver.find_element(By.XPATH, product_title_xpath)
value_product = product_element.text

price_element = driver.find_element(By.XPATH, product_price_xpath)
value_price = price_element.text

print(f'\n[Главная] Выбран товар №{index}: "{value_product}" с ценой {value_price}')

# Добавление в корзину и переход
driver.find_element(By.XPATH, add_to_cart_xpath).click()
driver.find_element(By.ID, 'shopping_cart_container').click()
print('Товар добавлен. Перешли в корзину.')

# 5. Проверка данных в корзине
# В корзине всего один товар, поэтому локаторы статичны и берутся прямо со страницы
cart_product_element = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
value_cart_product = cart_product_element.text

cart_price_element = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
value_cart_price = cart_price_element.text

print(f'[Корзина] Товар: "{value_cart_product}", Цена: {value_cart_price}')

assert value_product == value_cart_product, "Ошибка: Названия не совпадают!"
assert value_price == value_cart_price, "Ошибка: Цены не совпадают!"
print('Asserts в корзине — OK')

# 6. Оформление заказа (Checkout)
driver.find_element(By.ID, 'checkout').click()

driver.find_element(By.ID, 'first-name').send_keys('Roman')
driver.find_element(By.ID, 'last-name').send_keys('Meleshin')
driver.find_element(By.ID, 'postal-code').send_keys('1234')
driver.find_element(By.ID, 'continue').click()
print('Форма покупателя заполнена.')

# 7. Проверка на финальном экране (Summary)
finish_product = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
value_finish_product = finish_product.text

finish_price = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
value_finish_price = finish_price.text

print(f'[Финал] Товар: "{value_finish_product}", Цена: {value_finish_price}')

assert value_product == value_finish_product, "Ошибка на финальной странице!"
assert value_price == value_finish_price, "Ошибка цены на финальной странице!"
print('Asserts на финальной странице — OK')

# Проверка итоговой суммы (Item total)
total_price_element = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
value_total_price = total_price_element.text

# Формируем ожидаемую строку на основе динамически полученной цены
expected_total_string = f'Item total: {value_price}'
assert expected_total_string == value_total_price, f"Ошибка стоимости: {expected_total_string} != {value_total_price}"
print('Assert итоговой суммы — OK. Тест успешно завершен!')

# 8. Скриншот и закрытие
now_date = datetime.datetime.now().strftime("%H.%M.%S-%d.%m.%Y")
print(now_date)
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('C:\\Python\\autotest_selenium\\screen\\' +name_screenshot)

input("\nНажмите Enter в консоли, чтобы закрыть браузер...")
driver.quit()
