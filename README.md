**Python 2.7.x only!**

# Page Object Pattern in Python

#### *If you want to try this code, just change FirefoxBinary path and type `python runtests.py` in prompt - it'll "test" few of W3.org functionalities.* 

#### How to run it?:


1. change FirefoxBinary path in file `environment.py` in line `binary = FirefoxBinary('...')`

2. in file `locators.py` set locators.

3. if necessary, provide correct credentials in `users.py`

4. in file `base.py` you can define your own methods for all pages of your website

5. in file 'testCases.py' you can create your own test cases, every method's name **must** begin with "test".
   For every method you should create instance of \*Page class, for example `page = base.TestPages()`. That allows every single test case to be run in separate browser window.

6. run your tests with `python runtests.py`



#### Examples:

- **Basic login**
    ### 1. In `base.py`:

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

    ### 2. In `locators.py`

    ```
    class LoginPageLocators(object):

      USERNAME = (By.ID, 'login-username')
      PASSWORD = (By.ID, 'login-password')
      BUTTON = (By.ID, 'btn-login')
    ```
    ### 3. In `testCases.py`

    ```
    def exampleLogin(self):

      page = base.ExampleLoginPage()
      base.ExampleLoginPage.open_login_page(page)

      base.ExampleLoginPage.login(page, "valid_user")
      base.ExampleLoginPage.close(page)
    ```

    ### 4. In `users.py`

    ```
    users = [

	     {"name": "invalid_user", "username": "test", "password": "testpwd123"},
       {"name": "valid_user", "username": "admin", "password": "admin"},

    ]

    ```

  - **Prtsc:**

  ### 1. in `testCases.py`:

  ```
  (...)
  import environment
  (...)
  # in class ExampleTest:

  ##
  def testscreenOnly(self):
      page = base.MainW3Page()
      base.MainW3Page.open_main_page(page)
      environment.grab_and_save_screen('screenOnly') ##'screenOnly' is name of screen file
      base.MainW3Page.close(page)
  ##

  ```


  ## PRTSC does not work?

  #### If prtsc does not work, then you should remove file prtscn.so, and then compile prtsc.c again using the following command:

  ```
  gcc -shared -O3 -lX11 -fPIC -Wl,-soname,prtscn -o prtscn.so prtscn.c
  ```
  *requires gcc*
