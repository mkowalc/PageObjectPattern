#!/usr/bin/env python
from operator import itemgetter


users = [

	{"name": "invalid_user", "username": "user", "password": "passwd"},
	{"name": "valid_user", "username": "admion", "password": "123test"},

]

def get_user(name):
    try:
        return (user for user in users if user["name"] == name).next()
    except:
        print "\n     User %s is not defined, enter a valid user.\n" %name
