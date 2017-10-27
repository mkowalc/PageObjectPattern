#!/usr/bin/env python
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import config as cfg
import string
import os
import random
import datetime
import prtsc

def setBinary():
    binary = FirefoxBinary(cfg.tests['driver']) #Path to your binary

def id_generator(size, chars = string.digits):
    a = ''.join(random.choice(chars) for _ in range(size))
    return a

def str_generator(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    a = ''.join(random.choice(chars) for _ in range(size))
    return a

def load_bar(filename):
    path = "foo/" + filename
    with open(path, "r") as bar_file: #path to bar file in foo directory
        bar_file_string = bar_file.read()
        return bar_file_string

def grab_and_save_screen(casename):
    path = os.getcwd() + '/screens/' + casename
    if(os.path.isdir(path) != True):
        os.mkdir('screens/' + casename)

    screen_name = (casename + str(datetime.datetime.now()))
    im = prtsc.grab_screen(0,0, 1440, 900)
    prtsc.save_screen(im, casename, screen_name)
