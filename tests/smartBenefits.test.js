const { test, expect } = require('@playwright/test');
const fs = require('fs');
const path = require('path');
const LoginPage = require('../pages/LoginPage');
const EmployeesPage = require('../pages/EmployeesPage');
const customCommands = require('../customCommands');

const employeeData = JSON.parse(fs.readFileSync(path.join(__dirname, '../fixtures/employee.json'), 'utf-8')).employees;

test.describe('Smart Benefits Portal End-to-End', () => {
    test.setTimeout(120000);
    test('should login, navigate, and fill employee form', async ({ page }) => {
        // Step 1: Login
        const loginPage = new LoginPage(page);
        await loginPage.navigateToLoginPage();
        await loginPage.login('aghasherazi355+17@gmail.com', 'secret17');
        await loginPage.validateDashboardURL();
        await loginPage.validateUserEmail('aghasherazi355@gmail.com');

        // Step 2: Employees navigation
        const employeesPage = new EmployeesPage(page);
        await employeesPage.navigateToEmployees();
        await employeesPage.clickAddNewEmployee();
        await employeesPage.validateAddEmployeeURL();

        // Step 3: Fill employee form for each employee
        for (const emp of employeeData) {
            // Full Name
            if (emp.fullName?.is_required && emp.fullName.name) {
                await customCommands.fillTextField(page, 'Full Name', emp.fullName.name);
            }
            // Employee ID
            if (emp.employeeId?.is_required && emp.employeeId.employeeId) {
                await customCommands.fillTextField(page, 'Employee ID', emp.employeeId.employeeId);
            }
            // CNIC
            if (emp.cnic?.is_required && emp.cnic.cnic) {
                // Remove non-numeric characters for input[type=number]
                const cnicNumeric = emp.cnic.cnic.replace(/\D/g, '');
                await customCommands.fillTextField(page, 'CNIC', cnicNumeric);
            }
            // Branch
            if (emp.branch?.is_required && emp.branch.branch) {
                await customCommands.fillTextField(page, 'Branch', emp.branch.branch);
            }
            // Optionally, add code for other fields following the same pattern
        }
    });
});
