import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PageObjects.login_page import LoginPage
from PageObjects.dashboard_page import DashboardPage
from TestDatas.data import Data

def test_successful_login(page):

    login_page = LoginPage(page)
    dashboard = DashboardPage(page)
    data = Data()

    login_page.navigate(data.url)
    login_page.login(data.username, data.password)
    page.wait_for_selector("p.header-name")
    assert page.locator("//p[@class='header-name']").is_visible(), "Login failed: Dashboard not found"

    dashboard.click_logout()
    assert dashboard.is_logged_out(), "Logout failed: Login page not displayed"
