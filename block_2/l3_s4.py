from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
import pyperclip as pc


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(1)

    print(browser.switch_to.alert.text)
    pc.copy(browser.switch_to.alert.text.split(': ')[-1])  # сохранить в буфер

finally:
    time.sleep(10)
    browser.quit()
