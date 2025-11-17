# URL Shortener

A simple Flask-based URL shortener that generates short codes for long URLs.

## Features

- Shorten long URLs to 6-character codes
- Automatic URL protocol handling (adds https:// if missing)
- SQLite database storage
- Simple web interface

## Requirements

- Python 3.x
- Flask

## Installation

1. Install Flask:
```bash
pip install flask
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://127.0.0.1:5000`

## Usage

1. Enter a URL in the input field
2. Click submit to generate a shortened URL
3. Use the short URL to redirect to the original link

## Database

The app automatically creates a SQLite database (`url_shortner.db`) to store URL mappings.

## Notes

- Runs on `http://127.0.0.1:5000` by default
- Debug mode is enabled for development
- Short codes are 6 characters (letters and numbers)