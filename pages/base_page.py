import re

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def wait_for(self, locator, timeout=5000):
        self.page.wait_for_selector(locator, timeout=timeout)

    def get_text(self, locator):
        locator_obj = self.page.locator(locator) if isinstance(locator, str) else locator
        return locator_obj.inner_text()

    def assert_text(self, locator, expected):
        actual = self.get_text(locator)
        assert actual is True, f"{actual} ko‘rinmayapti"
        assert actual == expected, f"{actual} noto‘g‘ri matn: {expected}"

    def screenshot(self, path="screenshot.png"):
        self.page.screenshot(path=path)

    def is_visible(self, locator):
        try:
            return self.page.locator(locator).is_visible()
        except:
            return False

    def get_by_role_custom(self, role, name, timeout=6000):
        element = self.page.get_by_role(role, name=name)
        element.wait_for(timeout=timeout)
        return element

    def click_by_role(self, role, name):
        self.get_by_role_custom(role, name).click()

    def fill_by_role(self, role, name, value):
        return self.get_by_role_custom(role, name).fill(value)

    def get_text_safe(self, text):
        """Return (is_visible, text) tuple if element is visible."""
        locator = f"text={text}"
        if self.is_visible(locator):
            return True, self.get_text(locator)
        return False, None

    def click_text_if_visible(self, text):
        locator = f"text={text}"
        if self.is_visible(locator):
            return self.click(locator)
        return False
    def fill_by_placeholder(self, placeholder_text, value):
        locator = f"input[placeholder='{placeholder_text}']"
        self.fill(locator, value)

    def find_by_tag_and_text(self, tag, text):
        """Return locator that matches exact text inside a tag."""
        pattern = re.escape(text)
        return self.page.locator(tag).filter(has_text=re.compile(fr"^{pattern}$"))

    def get_by_text(self, text, exact=False):
        return self.page.get_by_text(text, exact=exact)

