import re

from pages.base_page import BasePage


class RegisterBusinessesAccountForm(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def open_page(self):
        self.open("https://agentlik.yonda.uz/")

    def labels_visible_region(self, text):
        return self.get_text_safe(text)

    def select_region_click(self, text):
        return self.click_by_role("button", text)

    def region_district(self, text):
        return self.get_text_safe(text)

    def region_district_fill(self, text, value):
        return self.fill_by_role('textbox', text, value)

    def region_district_click(self, value):
        return self.click_by_role("option", value)

    def continue_button(self, text):
        return self.click_by_role("button", text)

    def week_days_text(self, tagName, text):
        return self.find_by_tag_and_text(tagName, text)

    def form_input_placeholder_fill(self, placeholder, text):
        self.fill_by_placeholder(placeholder, text)

    def form_input_role_fill_click(self, role, text):
        self.click_by_role(role, text)

    def form_input_get_text(self, role, text):
        locator = f"input[{role}='{text}']"
        return self.page.locator(locator).input_value()

    def select_option_and_check_text(self, role, option_text):
        return self.get_by_role_custom(role, option_text)

    def select_time_range(self, start_hour, start_minute):
        self.get_by_text(start_hour, True).click()
        self.get_by_text(start_minute, True).nth(1).click()
        self.find_by_tag_and_text("div","Saqlash").click()


