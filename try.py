from selenium import webdriver


driver = webdriver.Chrome()
options= Options()
#options.add_argument('__headless=new')

url = 'https://demoqa.com/dynamic-properties'
driver.get(url)
driver.minimize_window()