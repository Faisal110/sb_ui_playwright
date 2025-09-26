from playwright.sync_api import Page
from login_secrets import ACCOUNT_MANAGER_EMAIL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_phone_input = 'input[type="text"], input[type="email"], input[type="tel"]'
        self.password_input = 'input[type="password"]'
        self.login_button = 'button[type="submit"]'
        self.user_email = ACCOUNT_MANAGER_EMAIL

    def navigate_to_login_page(self, url):
        self.page.goto(url, wait_until='networkidle', timeout=60000)

    def login(self, email, password):
        self.page.wait_for_selector(self.email_phone_input, state='visible', timeout=60000)
        self.page.fill(self.email_phone_input, email)
        self.page.wait_for_selector(self.password_input, state='visible', timeout=60000)
        self.page.fill(self.password_input, password)
        with self.page.expect_navigation(wait_until='networkidle', timeout=60000):
            self.page.click(self.login_button)
        self.page.wait_for_load_state('domcontentloaded', timeout=60000)

    def validate_dashboard_url(self):
        self.page.wait_for_selector('.dashboard, .main-content, nav', timeout=60000)

    def validate_user_email(self):
        email_selectors = [
            f'text={self.user_email}',
            f'[title*="{self.user_email}"]',
            f'[aria-label*="{self.user_email}"]',
            '.user-info, .profile-info'
        ]
        for selector in email_selectors:
            try:
                self.page.wait_for_selector(selector, timeout=20000)
                return
            except Exception:
                continue
        raise Exception('Could not find user email on dashboard')
