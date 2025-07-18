import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

    yield page # To split up the function into setup and teardown

    #teardown method
    context.close()
    browser.close()