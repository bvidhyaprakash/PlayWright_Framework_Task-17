from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_element(self, selector: str):
        self.page.wait_for_selector(selector)