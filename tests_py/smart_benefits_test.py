import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))

def test_smart_benefits_portal():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()

        try:
            # Step 1: Login
            from login_secrets import EMAIL, PASSWORD, DEMO_URL, PROD_URL
            from fixtures.employee_data import employees
            from pages_py.login_page import LoginPage
            from pages_py.employees_page import EmployeesPage
            from utils_py.custom_commands import fill_text_field

            login_page = LoginPage(page)
            # Choose DEMO_URL or PROD_URL as needed
            login_page.navigate_to_login_page(DEMO_URL)
            login_page.login(EMAIL, PASSWORD)
            login_page.validate_dashboard_url()
            login_page.validate_user_email()

            # Debugging step to capture login state immediately after login
            login_page.debug_login_state()

            # Step 2: Employees navigation
            employees_page = EmployeesPage(page)
            employees_page.navigate_to_employees()
            employees_page.click_add_new_employee()
            
            # Debugging step before validating Add Employee URL
            employees_page.debug_login_state()
            
            employees_page.validate_add_employee_url()

            # Step 3: Fill employee form for each employee
            for emp in employees:
                # Full Name
                if emp.get('fullName', {}).get('is_required') and emp['fullName'].get('name'):
                    fill_text_field(page, 'Full Name', emp['fullName']['name'])
                # Employee ID
                if emp.get('employeeId', {}).get('is_required') and emp['employeeId'].get('employeeId'):
                    fill_text_field(page, 'Employee ID', emp['employeeId']['employeeId'])
                # CNIC
                if emp.get('cnic', {}).get('is_required') and emp['cnic'].get('cnic'):
                    cnic_numeric = ''.join(filter(str.isdigit, emp['cnic']['cnic']))
                    fill_text_field(page, 'CNIC', cnic_numeric)
                # Branch
                if emp.get('branch', {}).get('is_required') and emp['branch'].get('branch'):
                    fill_text_field(page, 'Branch', emp['branch']['branch'])
                # Optionally, add code for other fields following the same pattern
        finally:
            browser.close()

if __name__ == "__main__":
    test_smart_benefits_portal()
