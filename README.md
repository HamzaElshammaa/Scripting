<div align="center">

# Automated Academic Portal Evaluation Suite 🤖🌐

### **Headless Browser Automation Scripts Built with Python & Selenium WebDriver**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)

*A collection of Python + Selenium WebDriver automation scripts designed to eliminate repetitive manual form entry across university course and staff evaluation portals.*

</div>

---

## ✨ Features

- 🔄 **Automated Course Evaluation (`Evaluation Script GUC (courses).py`):** Iterates through all enrolled courses in the student portal dropdown, populates standardized Likert-scale radio matrices, and submits evaluations automatically.
- 👨‍🏫 **Automated Staff & Instructor Evaluation (`Evaluation Script GUC.py`, `Evaluation Script-Staff.py`):** Cycles through academic staff listings, handles missing/already-completed forms gracefully via `NoSuchElementException` recovery, and submits responses.
- 🧪 **Selenium Sandbox (`Learning Selenium.py`):** Minimal WebDriver setup reference for Chromium Edge.

---

## 🚀 Usage

### 1. Install Dependencies
```bash
pip install selenium
```

### 2. Set Portal Credentials via Environment Variables
```bash
export GUC_USERNAME="your.username"
export GUC_PASSWORD="your_password"
```

### 3. Run the Evaluation Scripts
```bash
# Automate course evaluations
python "Evaluation Script GUC (courses).py"

# Automate staff evaluations
python "Evaluation Script GUC.py"
```
