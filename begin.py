from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options



options = Options()
options.add_argument("--headless")


driver = webdriver.Firefox(options=options)
driver.get('https://quotes.toscrape.com/login')

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'username')))

login = driver.find_element('xpath', "//input[@id='username']")
password = driver.find_element('xpath', "//input[@id='password']")

login.send_keys('admin')
password.send_keys('admin')

login_btn = driver.find_element('xpath', "//input[@value='Login']")


login_btn.click()
html = driver.page_source
print(html)
driver.quit()


# driver = webdriver.Firefox()
# driver.get('https://www.google.com/')