# Custom RSA Encryption Implementation

## Overview
This project is a standalone, "from-scratch" implementation of the RSA (Rivest–Shamir–Adleman) algorithm. Unlike standard production environments that rely on pre-compiled libraries like `OpenSSL` or `PyCryptodome`, this project implements the core mathematical foundations of asymmetric cryptography purely using Python's standard library. 

It handles large number generation, primality testing (Miller-Rabin), modular arithmetic, and the logic for encryption and decryption without any external dependencies.

## Features
* **Custom Key Generation:** Generates 2048-bit Public and Private key pairs using a multi-threaded prime search.
* **No Dependencies:** Runs entirely on the Python standard library (`random`, `sys`, `threading`, `math`).
* **Mathematical Core:** Implements the Miller-Rabin primality test and Extended Euclidean Algorithm manually.
* **Text Encryption:** Converts standard string inputs into integer format for mathematical encryption.
* **Decryption:** Restores original text from encrypted cipher integers.
* **Cross-Version Compatibility:** Designed to function on both Python 2.x and Python 3.x environments.

## Technologies Used
* **Language:** Python 3 (Compatible with Python 2.7)
* **Libraries:** * `random` (for bit generation)
    * `threading` (for parallel processing during prime search)
    * `sys` (for I/O and version detection)
    * `math` (standard mathematical operations)

## Steps to Install & Run
Since this project uses no external libraries, "installation" is simply cloning the repository.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/rsa-custom-implementation.git](https://github.com/your-username/rsa-custom-implementation.git)
    cd rsa-custom-implementation
    ```

2.  **Run the Application:**
    You can run the script directly with the Python interpreter:
    ```bash
    python rsa_main.py
    ```
    *(Note: Replace `rsa_main.py` with whatever you named your python file)*

## Instructions for Testing
1.  Run the script using the command above.
2.  When prompted `please input the text to be encrypted:`, type a test phrase (e.g., "Hello World").
3.  **Observe Key Generation:** The system will spin up 4 threads to find prime numbers. Wait for the "Public Key" to be displayed.
4.  **Verify Encryption:** The terminal will output a large integer representing the **Encrypted** ciphertext.
5.  **Verify Decryption:** The system will immediately use the private key to decrypt the message.
6.  **Success Condition:** The final "Decrypted" output must exactly match your initial input.

## Screenshots
*(Place a screenshot of your terminal output here showing the full flow from input -> encryption -> decryption)*