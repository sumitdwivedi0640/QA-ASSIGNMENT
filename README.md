# Playwright Google Search Automation

This repository contains a Playwright automation script that searches Google for information about the future of SDET role in IT.

## Overview

The automation script:
- Navigates to Google
- Searches for "what is the future of SDET role in IT"
- Captures screenshots of the results
- Displays the first few search results

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd QA-assignment
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install chromium
```

## Running the Script

Run the script directly:
```bash
python test_google_search.py
```

Or using pytest:
```bash
pytest test_google_search.py -v
```

## GitHub Actions

This repository includes a GitHub Actions workflow that automatically runs the Playwright tests on:
- Push to main/master branch
- Pull requests to main/master branch
- Manual trigger via workflow_dispatch

The workflow:
- Sets up Python environment
- Installs dependencies
- Installs Playwright browsers
- Runs the automation script
- Uploads screenshots as artifacts

## Project Structure

```
.
├── test_google_search.py    # Main automation script
├── requirements.txt         # Python dependencies
├── .github/
│   └── workflows/
│       └── playwright.yml   # GitHub Actions workflow
└── README.md               # This file
```

## Screenshots

The script automatically captures screenshots:
- `search_results.png` - Screenshot of search results page
- `error_screenshot.png` - Screenshot if an error occurs (only on failure)

## Notes

- The script runs in headless mode by default (suitable for CI/CD)
- To run in headed mode (see the browser), change `headless=True` to `headless=False` in the script
- The script handles cookie consent dialogs that may appear

## License

This project is for educational purposes.
