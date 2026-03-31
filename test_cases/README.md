# Student Registration System - Test Cases

| TC ID | Description | Expected Result |
|-------|-------------|-----------------|
| TC_01 | Verify registration page loads successfully | Page displays "Student Registration" and all form fields. |
| TC_02 | Submit form with all fields empty | Error message "All fields are mandatory!" is displayed. |
| TC_03 | Submit form with only name filled (partial submission) | Error message "All fields are mandatory!" is displayed. |
| TC_04 | Enter register number with incorrect overall format | Error message "Register Number must be in format: 23MIS0146" is displayed. |
| TC_05 | Enter register number in lowercase instead of uppercase | Error message "Register Number must be in format: 23MIS0146" is displayed. |
| TC_06 | Enter register number with extra digits beyond required length | Error message "Register Number must be in format: 23MIS0146" is displayed. |
| TC_07 | Enter register number containing special characters | Error message "Register Number must be in format: 23MIS0146" is displayed. |
| TC_08 | Enter password with less than 6 characters | Error message about password rules is displayed. |
| TC_09 | Enter password with exactly 6 characters (boundary case) | Success if it meets complexity requirements. |
| TC_10 | Enter valid email address format | Form accepts the email without validation error. |
| TC_11 | Enter email missing “@” symbol | Browser validation or error message "Please enter a valid email address!" |
| TC_12 | Submit form without selecting department | Error message "All fields are mandatory!" is displayed. |
| TC_13 | Submit form without selecting gender | Error message "All fields are mandatory!" is displayed. |
| TC_14 | Submit form with all valid inputs | Success message "Student Registered Successfully!" is displayed. |
| TC_15 | Enter numeric values in name field | Error message "Name must contain only alphabets!" is displayed. |
| TC_16 | Enter special characters in name field | Error message "Name must contain only alphabets!" is displayed. |
| TC_17 | Enter only spaces in input fields | Error message "All fields are mandatory!" is displayed. |
| TC_18 | Submit form multiple times consecutively | Registration remains successful; no duplication or crashes. |
| TC_19 | Verify error message is displayed for invalid input | Error element becomes visible with appropriate text. |
| TC_20 | Verify success message is displayed for valid input | Success element becomes visible after submission. |
| TC_21 | Verify error message styling (red color) | Error text has the appropriate CSS class/color applied. |
| TC_22 | Verify form does not reload on submission | Page state is preserved after clicking register. |
| TC_23 | Store credentials into local array/storage | User data is persisted in `localStorage` for future login. |
