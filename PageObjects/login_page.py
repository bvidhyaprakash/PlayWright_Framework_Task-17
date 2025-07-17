from PageObjects.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("input[placeholder='Enter your mail']")
        self.password_input = page.locator("input[placeholder='Enter your password ']")
        self.login_button = page.locator("//button[normalize-space()='Sign in']")

    def navigate(self, url):
        self.page.goto(url)

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()