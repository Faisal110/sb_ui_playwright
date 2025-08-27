class EmployeesPage {
    constructor(page) {
        this.page = page;
        this.employeesSelectors = [
            'a:has-text("Employees")',
            '[href*="employees"]',
            'a:has-text("Employee")',
            'a[href*="/hr/"]',
            '.sidebar a:has-text("Employee")',
            'nav a:has-text("Employee")'
        ];
        this.addNewEmployeeButton = 'button:has-text("Add New Employee"), a:has-text("Add New Employee")';
    }

    async navigateToEmployees() {
        // Try each selector until we find one that works
        let found = false;
        for (const selector of this.employeesSelectors) {
            try {
                await this.page.waitForSelector(selector, { state: 'visible', timeout: 20000 });
                await this.page.click(selector);
                found = true;
                break;
            } catch (e) {
                continue;
            }
        }
        
        if (!found) {
            throw new Error('Could not find Employees link');
        }
        
        await this.page.waitForLoadState('networkidle', { timeout: 60000 });
    }

    async clickAddNewEmployee() {
        await this.page.waitForSelector(this.addNewEmployeeButton, { state: 'visible', timeout: 60000 });
        await this.page.click(this.addNewEmployeeButton);
        await this.page.waitForLoadState('networkidle', { timeout: 60000 });
    }

    async validateAddEmployeeURL() {
        // Wait for both URL and form elements
        await Promise.all([
            this.page.waitForURL(/.*add.*/, { timeout: 60000 }),
            this.page.waitForSelector('form, .add-employee-form, .employee-form', { timeout: 60000 })
        ]);
    }
}

module.exports = EmployeesPage;
