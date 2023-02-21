import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_digit = int(browser.find_element(By.CSS_SELECTOR, 'h2 > span:nth-child(2)').text)
    second_digit = int(browser.find_element(By.CSS_SELECTOR, 'h2 > span:nth-child(4)').text)
    sum_digits = first_digit + second_digit

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_digits))

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
