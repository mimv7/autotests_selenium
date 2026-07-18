import datetime
import time

from  selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options


options = Options()
#options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()


# получение даты на 10 дней вперед
# Использование timedelta страхует код от ошибок при переходе на следующий месяц/год
current_date = datetime.datetime.now()
future_date = current_date + datetime.timedelta(days=10)

# Форматируем дату под стандартный формат полей ввода (мм/дд/ГГГГ)
date_to_input = future_date.strftime("%m/%d/%Y")

print(f'Текущая дата на компьютере: {current_date.strftime("%m/%d/%Y")}')
print(f'Вычисленная дата (+10 дней): {date_to_input}')

# Используем устойчивый относительный локатор по ID элемента
select_date = driver.find_element('xpath', '//input[@id="datePickerMonthYearInput"]')

# Сначала кликаем по полю, чтобы сфокусировать драйвер

select_date.click()

# Используем Ctrl+A и Backspace для надежной очистки дефолтного значения поля
select_date.send_keys(Keys.CONTROL + 'a')
select_date.send_keys(Keys.BACKSPACE)
time.sleep(3)

# Отправляем готовую строковую дату в поле и подтверждаем операцию
select_date.send_keys(date_to_input)
select_date.send_keys(Keys.ENTER)
print(f'Результат: Дата "{date_to_input}" успешно отправлена текстом в поле ввода!')



# Принудительная остановка скрипта перед закрытием, чтобы успеть проверить результат глазами
input("Нажмите Enter в консоли, чтобы завершить работу теста и закрыть браузер...")
driver.quit()