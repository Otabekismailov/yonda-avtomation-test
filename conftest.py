import pytest
from playwright.sync_api import sync_playwright

from pages.biznes_account_forma import RegisterBusinessesAccountForm
import allure

from utils.fake_data import DISTRICTS, REGIONS
from faker import Faker



fake = Faker()

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="session")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()



@pytest.fixture(scope="session")
def biznes(page):
    obj = RegisterBusinessesAccountForm(page)
    obj.open_page()
    return obj


def pytest_exception_interact(node, call, report):
    page = node.funcargs.get("page", None)
    if page:
        screenshot_path = "reports/failure.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Xatolik holati", attachment_type=allure.attachment_type.PNG)

@pytest.fixture
def districts_list_tashkent_city():
    return DISTRICTS


@pytest.fixture
def regions_list():
    return REGIONS


@pytest.fixture
def fake_date():
    return fake