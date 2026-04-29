# OTP Challenge-Response System

A Python-based implementation of a two-factor authentication (2FA) mechanism using the **Challenge-Response** method powered by the HMAC-SHA256 algorithm.

## Project Structure
* `main.py` – The Server simulation (handles user registration and the login flow).
* `algorithm.py` – The core logic library for calculating HMAC hashes.
* `authenticator.py` – The Client tool (your virtual token) used to generate OTP responses.

## How to Run

To test the full authentication flow, it is recommended to use two separate terminal windows to simulate the Server and the Client. Start with main.py file and register.
