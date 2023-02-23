import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUniqueSelectors():

    def fill_form(self, link):
        self.driver = webdriver.Chrome()
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Kesa')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Lisa')
        browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('KL@google.com')

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
        return welcome_text

    def test_registration(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)

        assert "Congratulations! You have successfully registered!"== registration_result
        self.driver.close()
    def test_registration_bug(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)

        assert "Congratulations! You have successfully registered!" == registration_result
        self.driver.close()


if __name__ == "__main__":
    pytest.main()