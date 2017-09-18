#!/usr/bin/env python
from selenium.webdriver.common.by import By

class LoginPageLocators(object):

    USERNAME = (By.ID, 'login-username')
    PASSWORD = (By.ID, 'login-password')
    BUTTON = (By.ID, 'btn-login')
    ERROR_MESSAGE = (By.ID, 'login-alert')
    LOGOUT_INFO = (By.ID, 'logout-info')

class OtherPageLocators(object):

    TEST_PAGE = (By.ID, 'test-page-id')
    LOGOUT_BUTTON = (By.XPATH, "//xpath_to_logout_button
    TEST_LOCATOR = (By.CLASS_NAME, 'class-name')
    TEST2_LOCATOR = (By.CSS_SELECTOR, 'div.css_selector.selector_x')
    TEXT_TO_ASSERT = (By.ID, 'text_1')
