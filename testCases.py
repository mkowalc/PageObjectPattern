#!/usr/bin/env python
import base
from locators import *
import locators
import selenium
import users
import environment
import unittest
from selenium.webdriver.common.by import By
import os

binary = environment.setBinary()

class eIDTEST(unittest.TestCase):

    def test1(self): ##there must be "test" at the beginning of method name

        page = base.TestPages()
        base.TestPages.open_login_page(page)
        base.TestPages.login_with_valid_user(page, "invalid_user")
        base.TestPages.click_something(page)
        base.WBAdminPanel.close(page)
