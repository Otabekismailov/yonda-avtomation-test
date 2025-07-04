import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://agentlik.yonda.uz/")
    page.get_by_role("button", name="Viloyatni tanlang").click()
    page.get_by_role("textbox", name="Qidirish...").fill("Toshkent shahri")
    page.get_by_role("option", name="Toshkent shahri").click()
    expect(page.locator("form")).to_match_aria_snapshot("- button \"Toshkent shahri\":\n  - img")
    page.get_by_role("button", name="Toshkent shahri").click()
    page.get_by_role("option", name="Toshkent shahri").click()
    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)