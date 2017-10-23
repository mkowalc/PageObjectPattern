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
import prtsc
import datetime

binary = environment.setBinary()

class ExampleTest(unittest.TestCase):

    # def testSearchBar(self): ##there must be "test" at the beginning of method name
    #
    #     page = base.MainW3Page()
    #     base.MainW3Page.open_main_page(page)
    #     base.MainW3Page.search_something(page, "HTML")
    #     base.MainW3Page.click_search_button(page)
    #     there should be some assertion
    #     base.MainW3Page.close(page)

    # def testclickStandards(self):
    #
    #     page = base.MainW3Page()
    #     base.MainW3Page.open_main_page(page)
    #     base.MainW3Page.click_standards(page)
    #
    #
    #     os.mkdir('screens/' + 'testClickStd')
    #     screen_name = ("testClickStd" + str(datetime.datetime.now()))
    #     im = prtsc.grab_screen(0,0, 1440, 900)
    #     prtsc.save_screen(im, "testClickStd", screen_name)
    #     environment.grab_and_save_screen('clickStandards')
    #
    #     base.MainW3Page.close(page)

    def testscreenOnly(self):
        page = base.MainW3Page()
        base.MainW3Page.open_main_page(page)
        environment.grab_and_save_screen('screenOnly')
        base.MainW3Page.close(page)
