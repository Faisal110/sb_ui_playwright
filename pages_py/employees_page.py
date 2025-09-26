from playwright.sync_api import Page

class EmployeesPage:
    def __init__(self, page: Page):
        self.page = page
        self.employees_selectors = [
            'a:has-text("Employees")',
            '[href*="employees"]',
            'a:has-text("Employee")',
            'a[href*="/hr/"]',
            '.sidebar a:has-text("Employee")',
            'nav a:has-text("Employee")'
        ]
        self.add_new_employee_button = 'button:has-text("Add New Employee"), a:has-text("Add New Employee")'

    def navigate_to_employees(self):
        found = False
        for selector in self.employees_selectors:
            try:
                self.page.wait_for_selector(selector, state='visible', timeout=20000)
                self.page.click(selector)
                found = True
                break
            except Exception:
                continue
        if not found:
            raise Exception('Could not find Employees link')
        self.page.wait_for_load_state('networkidle', timeout=60000)

    def click_add_new_employee(self):
        self.page.wait_for_selector(self.add_new_employee_button, state='visible', timeout=60000)
        self.page.click(self.add_new_employee_button)
        self.page.wait_for_load_state('networkidle', timeout=60000)

    def validate_add_employee_url(self):
        print("Debug: Current URL during validation:", self.page.url)
        # Validate by checking for specific elements on the Add Employee page
        self.page.wait_for_selector('form, .add-employee-form, .employee-form', timeout=90000)