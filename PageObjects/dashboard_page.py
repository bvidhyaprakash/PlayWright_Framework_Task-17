from PageObjects.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.close_popup = page.locator("//button[contains(text(),'✕')]")
        self.profile = page.locator("//div[@class='profile-click-icon-div']")
        self.logout_button = page.locator("//div[normalize-space()='Log out']")

    def click_logout(self):
        if self.close_popup.is_visible():
            self.close_popup.click()
            self.profile.click()
            self.logout_button.click()
        else:
            self.profile.click()
            self.logout_button.click()

    def is_logged_out(self):
        self.page.wait_for_selector("//button[normalize-space()='Sign in']")
        return self.page.locator("//button[normalize-space()='Sign in']").is_visible()
