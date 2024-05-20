# RSA Encryption and Decryption Example

This project demonstrates RSA encryption and decryption using the `pycryptodome` library in Python. The script generates an RSA key pair, encrypts a message with the public key, and decrypts it with the private key. Additionally, it simulates the decryption process with logging and a loading bar.

## Prerequisites

- Python 3.x
- `pycryptodome` library
- `tqdm` library

## Installation

1. Clone this repository or download the script files.
2. Install the required Python packages:

    ```sh
    pip install pycryptodome tqdm
    ```

## Files

- `rsa_encryption.py`: Main script to perform RSA encryption and decryption.
- `rsa_decryption_simulation.py`: Module that simulates the decryption process with logging and a loading bar.

## Usage

1. Ensure both `rsa_encryption.py` and `rsa_decryption_simulation.py` are in the same directory.
2. Run the `rsa_encryption.py` script:

    ```sh
    python rsa_encryption.py
    ```

3. The script will output the encrypted message in hexadecimal format, simulate the decryption process, and display the decrypted message along with the decryption time.

## Example Output

```sh
Encrypted: b'...'
Decrypting: [..................................................] 100% 
[2024-05-20 12:34:56] - INFO - Decryption took 1.234567 seconds
Decrypted: Hello, this is a message to be encrypted.
