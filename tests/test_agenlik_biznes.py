import time

import pytest
import allure


class TestAgenlikBiznes:

    @pytest.mark.parametrize("expected_text", ["* Viloyat", "* Tuman", "* Mahalla", "Muassasalar uchun",
                                               "Yonda ilovasida muassasa akkauntini olish uchun quyidagi formani to‘ldiring:",
                                               "Davom etish"])
    def test_text_labels_visible_region(self, biznes, expected_text):
        is_visible, is_text = biznes.labels_visible_region(expected_text)

        assert is_visible is True, f"{expected_text} ko‘rinmayapti"
        assert is_text == expected_text, f"{expected_text} noto‘g‘ri matn: {expected_text}"

    @pytest.mark.parametrize("expected_click,search_value",
                             [("Viloyatni tanlang", "Toshkent shahri"), ("Tumanni tanlang", "Yunusobod tumani"),
                              ("Mahallani tanlang", "Bodomzor")])
    def test_select_region(self, biznes, expected_click, search_value):
        biznes.select_region_click(expected_click)
        is_visible_expected_click, is_text_expected_click = biznes.region_district(expected_click)

        assert is_visible_expected_click is True, f"{expected_click} ko‘rinmayapti"
        assert is_text_expected_click == expected_click, f"{expected_click} noto‘g‘ri matn: {expected_click}"

        biznes.region_district_fill("Qidirish...", search_value)
        biznes.region_district_click(search_value)

        is_visible_search_value, is_text_search_value = biznes.region_district(search_value)
        assert is_visible_search_value is True, f"{search_value} ko‘rinmayapti"
        assert is_text_search_value == search_value, f"{search_value} noto‘g‘ri matn: {search_value}"

        is_visible_button, is_text_button = biznes.region_district("Davom etish")
        assert is_visible_button is True, f"Davom etish Button  ko‘rinmayapti"
        assert is_text_button == "Davom etish", f" Davom etish noto‘g‘ri matn: Davom etish"
        if is_text_button:
            biznes.continue_button("Davom etish")

    @pytest.mark.parametrize("week_days_text",
                             [
                                 "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba",
                             ])
    def test_forma_2_text_week(self, biznes, week_days_text):
        is_visible_text_week = biznes.week_days_text('div', week_days_text)

        assert is_visible_text_week.is_visible(), f"{week_days_text} ko‘rinmayapti"
        actual_text = is_visible_text_week.inner_text()
        assert actual_text == week_days_text, f"Matn noto‘g‘ri: '{actual_text}' o‘rniga '{week_days_text}' bo‘lishi kerak"

    @pytest.mark.parametrize("text",
                             ["* Muassasa kategoriyasi", "* Tel raqami", "* Elektron pochta", "Muassasa ish vaqtlari",
                              "Davom etish", "Ortga"])
    def test_form_2_text(self, text, biznes):
        is_visible, actual_text = biznes.get_text_safe(text)

        assert is_visible, f"{text} ko‘rinmayapti"

        actual = actual_text.replace("\n", " ").strip()
        expected = text.strip()

        assert actual == expected, f"Matn noto‘g‘ri: '{actual}' o‘rniga '{expected}' bo‘lishi kerak"

    @pytest.mark.parametrize("text,expected_text",
                             [("Muassasa nomini kiriting", "Test"),
                              ("99 999 99 99", "91 348 95 75"),
                              ("my@email.com", "test123@gmail.com")])
    def test_form_2_input_fill(self, biznes, fake_date, text, expected_text):
        biznes.form_input_placeholder_fill(text, expected_text)
        assert expected_text == biznes.form_input_get_text('value', expected_text)

    @pytest.mark.parametrize("role,expected_text",
                             [("button", "Muassasa kategoriyasini tanlang"),
                              ("option", "Sport"),
                              ])
    def test_form_2_select(self, biznes, role, expected_text):
        biznes.form_input_role_fill_click(role, expected_text)
        selected = biznes.select_option_and_check_text(role, expected_text)
        assert selected.inner_text() == expected_text

    @pytest.mark.parametrize("weekdays, start_hour, start_minute", [
        ("Dushanba", "04", "20"),
        ("Juma", "11", "20"),
    ])
    def test_weekday_custom_time(self, biznes, weekdays, start_hour, start_minute):
        biznes.find_by_tag_and_text("div", weekdays).get_by_role("checkbox").click()

        biznes.find_by_tag_and_text("div", f"{weekdays}00:00-00:00").get_by_role("button").first.click()
        biznes.select_time_range(start_hour, start_minute)
        biznes.find_by_tag_and_text("div", f"{weekdays}{start_hour}:{start_minute}-00:00").get_by_role("button").nth(
            1).click()
        biznes.select_time_range("18", "00")
        assert biznes.get_by_role_custom("button",
                                         f"{start_hour}:{start_minute}").inner_text() == f"{start_hour}:{start_minute}"
        assert biznes.find_by_tag_and_text("div", f"{weekdays}{start_hour}:{start_minute}-18:00").get_by_role(
            "button").nth(
            1).get_by_text("18:00").inner_text() == "18:00"

    @pytest.mark.parametrize("weekday, expected_checked", [
        ("Dushanba", "true"),
        ("Seshanba", "false"),
        ("Chorshanba", "false"),
        ("Payshanba", "false"),
        ("Juma", "true"),
        ("Shanba", "false"),
        ("Yakshanba", "false"),
    ])
    def test_weekday_checkbox_checked(self, biznes, weekday, expected_checked):
        actual_checked = biznes.find_by_tag_and_text("div", weekday) \
            .get_by_role("checkbox") \
            .get_attribute("aria-checked")

        assert actual_checked == expected_checked

    @pytest.mark.parametrize("text", ["* Manzil"])
    def test_form_3_location(self, biznes, text):
        biznes.continue_button("Davom etish")
        is_visible, actual_text = biznes.get_text_safe(text)
        input_text = biznes.get_by_role_custom("textbox", "Manzilni kiriting").get_attribute("placeholder")
        assert is_visible, f"{actual_text} ko‘rinmayapti"
        assert actual_text == text, f"Matn noto‘g‘ri: '{actual_text}' o‘rniga '{text}' bo‘lishi kerak"
        assert input_text == "Manzilni kiriting", f"Matn noto‘g‘ri: '{input_text}' o‘rniga 'Manzilni kiriting' bo‘lishi kerak"
