**Python 2.7.x only!**

#Page Object Pattern in Python

####How to run it?:


1. change FirefoxBinary path in file `environment.py` in line `binary = FirefoxBinary('...')`

2. in file `locators.py` set locators.

3. if necessary, provide correct credentials in `users.py`

4. in file `base.py` you can define your own methods for all pages of your website

5. in file 'testCases.py' you can create your own test cases, every method's name **must** begin with "test".
   For every method you should create instance of \*Page class, for example `page = base.TestPages()`. That allows every single test case to be run in separate browser window.

6. run your tests with `python runtests.py`

Foregoing steps are necessary to run this code, as this is just an example.

####Example:

- **Basic login**
    1. In `base.py`:

    ```
    class LoginPage(BasePage):

    url = `https://example.com/login`

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
    ```

    2. In `locators.py`

    ```
    class LoginPageLocators(object):

      USERNAME = (By.ID, 'login-username')
      PASSWORD = (By.ID, 'login-password')
      BUTTON = (By.ID, 'btn-login')
    ```
    3. In `testCases.py`

    ```
    def exampleLogin(self):

      page = base.ExampleLoginPage()
      base.ExampleLoginPage.open_login_page(page)

      base.ExampleLoginPage.login(page, "valid_user")
      base.ExampleLoginPage.close(page)
    ```

    4. In `users.py`

    ```
    users = [

	     {"name": "invalid_user", "username": "test", "password": "testpwd123"},
       {"name": "valid_user", "username": "admin", "password": "admin"},

    ]

    ```


**Python 2.7.x only!**
