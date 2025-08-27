/**
 * Custom Playwright commands for form interactions
 */

module.exports = {
  /**
   * Fill a text field by label or placeholder
   */
  async fillTextField(page, labelOrPlaceholder, value) {
    const selector = `input[placeholder='${labelOrPlaceholder}'], input[aria-label='${labelOrPlaceholder}'], label:has-text('${labelOrPlaceholder}') ~ input`;
    await page.waitForSelector(selector, { timeout: 20000 });
    await page.fill(selector, value);
  },

  /**
   * Select a dropdown option by label or placeholder
   */
  async selectDropdown(page, labelOrPlaceholder, optionText) {
    const selector = `select[aria-label='${labelOrPlaceholder}'], select[placeholder='${labelOrPlaceholder}'], label:has-text('${labelOrPlaceholder}') ~ select`;
    await page.waitForSelector(selector, { timeout: 20000 });
    await page.selectOption(selector, { label: optionText });
  },

  /**
   * Pick a date from a calendar field by label or placeholder
   */
  async pickCalendarDate(page, labelOrPlaceholder, dateString) {
    const selector = `input[type='date'][placeholder='${labelOrPlaceholder}'], input[type='date'][aria-label='${labelOrPlaceholder}'], label:has-text('${labelOrPlaceholder}') ~ input[type='date']`;
    await page.waitForSelector(selector, { timeout: 20000 });
    await page.fill(selector, dateString);
  },

  /**
   * Select a radio button by label or value
   */
  async selectRadioButton(page, labelOrValue) {
    const selector = `input[type='radio'][value='${labelOrValue}'], label:has-text('${labelOrValue}') input[type='radio']`;
    await page.waitForSelector(selector, { timeout: 20000 });
    await page.check(selector);
  }
};
