# Test Automation Exam - Behave + Selenium

This is my automation exam output using Behave + Selenium.

## What I covered

- Drag and Drop
- Infinite Scroll
- Dynamic Content
- Horizontal Slider

I separated each exercise into its own feature so it is easier to check one by one.

## Setup (what I used)

Prerequisites:

- Python 3.10+
- Chrome browser

Install steps:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run tests

Run all exercises:

```powershell
python -m behave
```

Run one exercise only:

```powershell
python -m behave features/drag_and_drop.feature
python -m behave features/infinite_scroll.feature
python -m behave features/dynamic_content.feature
python -m behave features/slider.feature
```

Run in headless mode:

```powershell
$env:HEADLESS = '1'
python -m behave
```