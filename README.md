##Page Object Pattern in Python

####How to run it?:


1. change FirefoxBinary path in file `environment.py` in line `binary = FirefoxBinary('...')`

2. in file `locators.py` set locators.

3. if necessary, provide correct credentials in `users.py`

4. in file `base.py` you can define your own methods for all pages of your website

5. in file 'testCases.py' you can create your own test cases, every method's name should begin with "test".
   For every method you should create instance of \*Page class, for example `page = base.TestPages()`. That allows every single test case to be run in separate browser window.

6. run your tests with `python runtests.py`

Foregoing steps are necessary to run this code, as this is just an example. 

**Python 2.7.x only!*
