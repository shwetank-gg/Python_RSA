# Project Statement

## Problem Statement
Modern cryptographic libraries abstract away the complex mathematics required for secure communication. While efficient, this abstraction creates a "black box" where developers may use encryption without understanding the underlying mechanics of prime number generation, modular inverse, and key derivation. Furthermore, many environments require lightweight encryption tools without the overhead of installing heavy C-compiled dependencies (like `cryptography` or `OpenSSL`).

## Scope of the Project
This project aims to build a functional RSA cryptosystem using only raw mathematics and standard Python libraries. 
* **In Scope:** * Implementation of the Miller-Rabin primality test.
    * Multi-threaded generation of 1024-bit primes (to form 2048-bit keys).
    * Basic text-to-integer padding and conversion.
    * Command-line interface for user interaction.
* **Out of Scope:** * Industrial-grade padding schemes (OAEP) for protection against advanced side-channel attacks.
    * Persistent key storage (saving to PEM/DER files).
    * Graphical User Interface (GUI).

## Target Users
* **Computer Science Students:** To visualize and understand the mathematical flow of Public Key Cryptography.
* **Security Researchers:** For testing mathematical properties of RSA without library constraints.
* **Legacy Systems Engineers:** Who need basic encryption capabilities in restricted environments where external package managers (`pip`) are unavailable.

## High-Level Features
1.  **Parallel Prime Search:** Utilizes concurrency to overcome the performance bottlenecks of finding large prime numbers in an interpreted language.
2.  **Key Pair Derivation:** Automatically calculates the Modulus ($n$), Public Exponent ($e$), and Private Exponent ($d$).
3.  **Secure Message Transfer Simulation:** Demonstrates the full lifecycle of a message: `Plaintext -> Ciphertext -> Plaintext` in a single session.
4.  **Input Flexibility:** Handles variable-length string inputs (up to the bit-limit of the generated key).