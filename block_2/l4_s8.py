from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math
import pyperclip as pc


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    book_wait = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()
    time.sleep(1)

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
    time.sleep(5)
    browser.quit()
