from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_cart_button(browser):
    browser.get(link)
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(buttons)!=0, "No such element!"