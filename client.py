import requests

def check_serial_key(ip, port, key):
    """
    Checks if the provided serial key is valid by making a request to the server.

    Args:
    ip (str): The IP address of the server.
    port (int): The port number of the server.
    key (str): The serial key to be checked.

    Returns:
    bool: True if the serial key is valid, False otherwise.
    """
    url = f'http://{ip}:{port}/check_serial_key'  # Construct the URL for the request
    response = requests.get(url, params={'key': key})  # Make a GET request with the serial key as a parameter
    if response.status_code == 200:
        return response.json().get('valid', False)  # Return the 'valid' status from the response JSON
    return False  # Return False if the request was not successful

# Example usage
ip_address = '127.0.0.1'  # Server's IP address
port = 5000  # Server's port number
key = input("Please enter the serial key to check: ")  # Get the serial key from user input
is_valid = check_serial_key(ip_address, port, key)  # Check if the serial key is valid
print(f'Serial key valid: {is_valid}')  # Print the result
