#!/usr/bin/env python
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import string
import os
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def setBinary():
    binary = FirefoxBinary('etc/firefox-54.0.1/firefox/firefox-bin') #Path to your binary

def id_generator(size, chars = string.digits):
    a = ''.join(random.choice(chars) for _ in range(size))
    return a

def str_generator(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    a = ''.join(random.choice(chars) for _ in range(size))
    return a

def load_bar():
    with open("foo/bar", "r") as bar_file: #path to bar file in foo directory
        bar_file_string = bar_file.read()
        return bar_file_string
