#!/usr/bin/env python
from selenium.webdriver.common.by import By

class MainPageLocators(object):

    LOGO = (By.XPATH, "//div[@id='w3c_mast']/h1/a")
    WEB_AND_INDUSTRY = (By.XPATH, "//div[@id='w3c_main']/div[2]/h3[2]/span/a")
    STANDARDS = (By.XPATH, "//div[@id='w3c_nav']/form/ul/li/a")
    SEARCHBAR = (By.XPATH, "//div[@id='search-form']/input")
    SEARCH_SUBMIT = (By.ID, 'search-submit')

class StandardsPageLocators(object):

    STANDARDS_HEADER = (By.CLASS_NAME, 'title')
