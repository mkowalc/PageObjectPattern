#!/usr/bin/env python
import selenium
from selenium import webdriver
import environment
import locators
from locators import *
import users
import os
binary = environment.setBinary()


class BasePage(object):

    url = None
    def __init__(self):
        self.driver = webdriver.Firefox(firefox_binary=binary)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def fill_form_by_id(self, value, *locator):
        elem = self.find_element(*locator)
        elem.send_keys(value)

    def click_button(self, *locator):
        self.find_element(*locator).click()

    def navigate(self, url):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()


class LoginPage(BasePage):

    url = "___" #ENTER_URL

    def open_login_page(self):
        self.navigate(self.url)

    def enter_username(self, user):
        self.find_element(*LoginPageLocators.USERNAME).send_keys(users.get_user(user)["username"])

    def enter_password(self, user):
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(users.get_user(user)["password"])

    def click_login_button(self):
        self.find_element(*LoginPageLocators.BUTTON).click()

    def login(self, user):
        self.enter_username(user)
        self.enter_password(user)
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return self.find_element(*OtherPageLocators.TEST_PAGE)

    def login_with_invalid_user(self, user):
        self.login(user)
        return self.find_element(*LoginPageLocators.ERROR_MESSAGE)

    def logout(self):
        self.click_button(*OtherPageLocators.LOGOUT_BUTTON)
        return self.find_element(*LoginPageLocators.LOGOUT_INFO)

class TestPages(LoginPage):

    def click_something(self):
        self.click_button(*OtherPageLocators.TEST_LOCATOR)
        return self.find_element(*OtherPageLocators.TEST2_LOCATOR)

    def check_sth_with_assertion(self, name):

        text_1 = self.find_element(*OtherPageLocators.TEXT_TO_ASSERT)
        assert(text_1.text == "sth")
