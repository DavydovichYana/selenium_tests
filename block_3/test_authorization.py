import time
import math
import pytest
from selenium.webdriver.common.by import By


class TestAliens:
    __params = ["https://stepik.org/lesson/236895/step/1",
                "https://stepik.org/lesson/236896/step/1",
                # "https://stepik.org/lesson/236897/step/1",
                # "https://stepik.org/lesson/236898/step/1",
                # "https://stepik.org/lesson/236899/step/1",
                # "https://stepik.org/lesson/236903/step/1",
                # "https://stepik.org/lesson/236904/step/1",
                # "https://stepik.org/lesson/236905/step/1"
                ]
    __hint = []
    __pass_w = 'Correct!'

    @pytest.mark.parametrize('url', __params)
    def test_get_some_alien_hints(self, browser, url):
        link = url
        browser.implicitly_wait(20)  # настройка неявного ожидания (до 20 с на каждый find)
        browser.get(link)

        browser.find_element(by="id", value="ember33").click()
        browser.find_element(by="id", value="id_login_email").send_keys("luckyabsolut@gmail.com")
        browser.find_element(by="id", value="id_login_password").send_keys("00025032")
        browser.find_element(by="css selector", value="button.sign-form__btn").click()

        answ_input = browser.find_element(By.TAG_NAME, "textarea")
        answ_input.send_keys(str(math.log(int(time.time()))))

        time.sleep(10)
        button_send = browser.find_element(By.CLASS_NAME, 'submit-submission')
        button_send.click()

        feedback = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
        try:
            assert self.__pass_w == feedback
        except AssertionError:
            self.__hint.append(feedback)

    def test_print_hints(self):
        print()
        print("------- " + ''.join(self.__hint) + " ---------")
        print()