# Custom Playwright commands for form interactions (Python)
from playwright.sync_api import Page

def fill_text_field(page: Page, label_or_placeholder: str, value: str):
    selectors = [
        f"input[placeholder='{label_or_placeholder}']",
        f"input[aria-label='{label_or_placeholder}']",
        f"label:has-text('{label_or_placeholder}') ~ input"
    ]
    for selector in selectors:
        try:
            page.wait_for_selector(selector, timeout=20000)
            page.fill(selector, value)
            return
        except Exception:
            continue
    raise Exception(f"Text field '{label_or_placeholder}' not found")

def select_dropdown(page: Page, label_or_placeholder: str, option_text: str):
    selectors = [
        f"select[aria-label='{label_or_placeholder}']",
        f"select[placeholder='{label_or_placeholder}']",
        f"label:has-text('{label_or_placeholder}') ~ select"
    ]
    for selector in selectors:
        try:
            page.wait_for_selector(selector, timeout=20000)
            page.select_option(selector, label=option_text)
            return
        except Exception:
            continue
    raise Exception(f"Dropdown '{label_or_placeholder}' not found")

def pick_calendar_date(page: Page, label_or_placeholder: str, date_string: str):
    selectors = [
        f"input[type='date'][placeholder='{label_or_placeholder}']",
        f"input[type='date'][aria-label='{label_or_placeholder}']",
        f"label:has-text('{label_or_placeholder}') ~ input[type='date']"
    ]
    for selector in selectors:
        try:
            page.wait_for_selector(selector, timeout=20000)
            page.fill(selector, date_string)
            return
        except Exception:
            continue
    raise Exception(f"Calendar field '{label_or_placeholder}' not found")

def select_radio_button(page: Page, label_or_value: str):
    selectors = [
        f"input[type='radio'][value='{label_or_value}']",
        f"label:has-text('{label_or_value}') input[type='radio']"
    ]
    for selector in selectors:
        try:
            page.wait_for_selector(selector, timeout=20000)
            page.check(selector)
            return
        except Exception:
            continue
    raise Exception(f"Radio button '{label_or_value}' not found")
