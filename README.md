# QR Code Generator for URLs

## Overview

This project is a web application that allows users to generate QR codes from URLs. Simply input a URL into the form, and the application will generate a QR code that encodes the URL. This tool is designed to be simple and user-friendly, suitable for both desktop and mobile devices.

## Features

- **URL Input**: Enter any valid URL.
- **QR Code Generation**: Generates a QR code based on the provided URL.
- **Responsive Design**: Ensures compatibility with both desktop and mobile devices.
- **User-Friendly Interface**: Easy to navigate and use.

## Technology Stack

- **Frontend**: HTML, CSS
- **Backend**: Django
- **QR Code Library**: `qrcode` (Python library)

## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/qr-code-generator.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd qr-code-generator
    ```

3. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the Application**: Open your browser and go to `http://127.0.0.1:8000` to start using the QR code generator.

## Usage

1. Open the application in your web browser.
2. Enter a URL in the input field.
3. Click the "Generate QR Code" button.
4. The QR code will be displayed on the page, ready for scanning or downloading.

## Contribution

Contributions are welcome! If you have suggestions for improvements or would like to contribute, please fork the repository and submit a pull request. For bug reports or feature requests, open an issue on GitHub.

## Contact

For questions or feedback, you can reach me at (mailto:gaurabneupane8969@gmail.com).

