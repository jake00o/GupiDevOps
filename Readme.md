
# Guppi Di Dhui - Back Pain Relief

A modern, single-page web application designed to help individuals find relief from back pain through posture correction, therapeutic exercises, and specialized consultations. This repository demonstrates core HTML, CSS, and JavaScript functionality, along with automated testing (using Python + Selenium) and a basic CI/CD pipeline configuration.
Live Preview: https://jake00o.github.io/Gupi.github.io/

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation & Setup](#installation--setup)
3. [Project Architecture](#project-architecture)
4. [Usage Instructions](#usage-instructions)
5. [Testing & Validation](#testing--validation)
   - [Automated Testing with Python and Selenium](#automated-testing-with-python-and-selenium)
   - [Manual Testing](#manual-testing)
6. [CI/CD Pipeline Overview](#cicd-pipeline-overview)
7. [Future Enhancements](#future-enhancements)
8. [License](#license)

---

## Project Overview

**Purpose:**
The “Guppi Di Dhui” website focuses on holistic back pain relief methods. It includes:
- An **About Us** section highlighting the approach to back pain relief.
- A **Services** section offering posture correction, therapeutic exercises, and one-on-one consultations.
- A **FAQ** that answers common queries about session duration, causes of back pain, and what to bring.
- **Testimonials** for credibility.
- A **Contact Form** for direct inquiries.

**Key Objectives:**
1. Provide easy access to service bookings.
2. Offer clear, concise information for individuals dealing with back pain.
3. Demonstrate a robust and maintainable code structure.

---

## Installation & Setup

### Prerequisites
- **Modern web browser** (e.g., Chrome, Firefox, Edge).
- **Python 3.9+** (if running automated tests).
- **Git** (to clone the repository) and an optional HTTP server to serve the site locally.

### Steps

1. **Clone Repository:**
   ```bash
   git clone https://github.com/username/GuppiDiDhui.git
   cd GuppiDiDhui
   ```

2. **Install Python Dependencies (Optional for Testing):**
   ```bash
   pip install selenium webdriver-manager
   ```

3. **Open index.html:**
   - **Option A:** Double-click `index.html` to open it in your browser.
   - **Option B:** Use a local server, for example:
     ```bash
     python -m http.server 5500
     ```
     Then go to `http://localhost:5500/index.html` in your web browser.

---

## Project Architecture

```
GuppiDiDhui/
│
├── index.html        # Main HTML structure
├── style.css         # CSS styling for the entire site
├── script.js         # Core site interactivity and form handling
│
├── test_booking.py   # Example Python + Selenium automated test script
├── requirements.txt  # Python dependencies (if using automated tests)
│
├── .github/workflows/ci.yml   # Example GitHub Actions config
└── README.md          # This documentation
```

1. **index.html**  
   Holds the primary HTML layout for the site, referencing `style.css` and `script.js`.
2. **style.css**  
   Responsible for responsive design, gradients, and layout styling.
3. **script.js**  
   Contains JavaScript for booking alerts, custom cursor, and contact form submission.

---

## Usage Instructions

1. **Navbar:**  
   - The top nav bar is fixed. Sections: About, Services, FAQ, Testimonials, Contact.
2. **Services:**  
   - Each service card includes a “Book Now” button that triggers a JavaScript alert.
3. **FAQ:**  
   - Lists common questions about back pain and session details.
4. **Testimonials:**  
   - Showcases feedback from satisfied clients, providing credibility.
5. **Contact Form:**  
   - Basic form that upon submission displays an alert to confirm successful outreach.

---

## Testing & Validation

### Automated Testing with Python and Selenium

**Goal:** Validate main features (like booking) to ensure the site behaves correctly.

1. **Install Python Dependencies:**
   ```bash
   pip install selenium webdriver-manager
   ```

2. **Example Script (test_booking.py):**
   ```python
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   from selenium.webdriver.chrome.service import Service
   from webdriver_manager.chrome import ChromeDriverManager
   import time

   def test_booking():
       driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       driver.get("http://localhost:5500/index.html")  # or your hosted URL

       # Scroll to services
       services_section = driver.find_element(By.ID, "services")
       driver.execute_script("arguments[0].scrollIntoView();", services_section)
       time.sleep(1)

       # Click "Book Now" for Therapeutic Exercises
       book_button = driver.find_element(By.XPATH, "//button[contains(text(),'Therapeutic Exercises')]")
       book_button.click()
       time.sleep(1)

       alert = driver.switch_to.alert
       alert_text = alert.text
       print("Alert Text:", alert_text)
       alert.accept()

       driver.quit()

   if __name__ == "__main__":
       test_booking()
   ```

3. **Run the Test:**
   ```bash
   python test_booking.py
   ```
4. **Expected Outcome:**  
   - Script loads the site, scrolls to Services, clicks “Book Now,” and prints alert message.

**Additional Tests:**
- **Contact Form Submission:** Ensure it triggers the correct alert.
- **Cross-Browser Checking:** Manual checks in Chrome, Firefox, etc.

### Manual Testing

- **Navigation Verification:** Each nav link correctly scrolls to the respective section.
- **Responsive Layout:** Confirm site is mobile-friendly by resizing browser or using DevTools.
- **Booking & Form Submission:** Manually click “Book Now” or submit contact form to confirm alert messages appear.

---

## CI/CD Pipeline Overview

An example GitHub Actions pipeline (`.github/workflows/ci.yml`) might:

- **Install Python** and **Selenium** dependencies.
- **Run your test scripts** automatically on every push or pull request.
- (Optional) **Deploy** the site if tests pass.

```yaml
name: CI Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install selenium
          pip install webdriver-manager

      - name: Run tests
        run: |
          python test_booking.py
```

**Key Benefits:**
1. Ensures code changes don’t break existing functionality.
2. Provides immediate feedback for every commit or pull request.

---

## Future Enhancements

1. **Database Integration** to store bookings or user data.
2. **Advanced Analytics** for user behavior tracking and feedback loops.
3. **Deployment Automation** with Docker and environment-specific configurations.
4. **More Comprehensive Test Coverage**, including accessibility tests.

---

## License

This project is distributed under the [MIT License](https://opensource.org/licenses/MIT). You’re free to use, modify, and distribute this project in accordance with the license’s terms.

