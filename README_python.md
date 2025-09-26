# Playwright Python Project

## How to run the test

1. Make sure you have Python 3.8+ and Playwright installed.
2. Activate your virtual environment if not already active.
3. Install Playwright browsers (already done):
   ```powershell
   .venv\Scripts\python.exe -m playwright install
   ```
4. Run the test:
   ```powershell
   .venv\Scripts\python.exe tests_py\smart_benefits_test.py
   ```

## Project Structure
- `tests_py/` : Python test files
- `pages_py/` : Python page objects
- `utils_py/` : Python custom commands
- `fixtures/` : Test data (JSON)

## Notes
- All logic from the JavaScript project has been ported to Python using Playwright's sync API.
- You can extend the Python files to cover more fields and scenarios as needed.
