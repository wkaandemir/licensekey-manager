# License Key Generator and Verification System

## Overview

This project includes a Flask web app and a PyQt desktop app for generating and verifying license keys.
Users can generate keys linked to their email addresses and a specified duration, then verify
these keys to access a calculator application.

## Components

1. **Flask Web Application**: A web interface for generating license keys.
2. **PyQt Desktop Application**: A desktop calculator application that requires a valid license key to access.

## Files

- `app.py`: The main application file for the PyQt desktop application.
- `client.py`: A helper script for checking the serial key by communicating with the Flask server.
- `server.py`: The Flask server script to handle license key generation and verification.
- `templates/index.html`: The HTML template for the main page of the Flask application.
- `templates/key_generated.html`: The HTML template for displaying the generated key.
- `serial_keys.db`: SQLite database file to store the keys and associated information.

## Usage

### Flask Web Application

1. **Setup**: Ensure you have Python and Flask installed. If not, install them using:

   ```bash
   pip install Flask
   ```

2. **Run the Server**: Execute the server script to start the Flask application:

   ```bash
   python server.py
   ```

3. **Access the Application**: Open a web browser and go to `http://127.0.0.1:5000` to access the License Key Generator web interface.

4. **Generate a License Key**:
    - Enter your email address.
    - Specify the license duration in days.
    - Submit the form to receive a license key.

### PyQt Desktop Application

1. **Setup**: Ensure you have Python and PyQt6 installed. If not, install them using:

   ```bash
   pip install PyQt6
   ```

2. **Run the Application**: Execute the main application file to start the calculator application:

   ```bash
   python app.py
   ```

3. **Enter the License Key**: A dialog will prompt you to enter the license key. The key will be verified against the Flask server.

4. **Access the Calculator**: If the key is valid, the calculator application will open. If the key is invalid or expired, an error message will be displayed.

## Purpose

The License Key Generator and Verification System serves as a simple example of how to integrate a web-based license generation system with a desktop application. This can be useful for:

- Software developers looking to implement basic license key verification for their applications.
- Learning purposes, to understand how web and desktop applications can communicate and validate data.
- Ensuring that only authorized users can access certain features of an application.

## Notes

- The database (`serial_keys.db`) stores the email addresses, generated keys, and their expiry dates.
- Ensure that the Flask server is running when trying to verify a license key from the PyQt application.
- Modify the `server.py`, `client.py`, and `app.py` files as needed to fit your specific requirements.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
