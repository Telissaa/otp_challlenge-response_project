import hmac
import hashlib

def generate_otp(secret, challenge):
    # Convert secret and challenge to bytes if they are strings
    if isinstance(secret, str): secret = secret.encode()
    if isinstance(challenge, str): challenge = challenge.encode()

    # Create HMAC object using the secret and challenge
    hmac_obj = hmac.new(secret, challenge, hashlib.sha256)

    # Generate OTP by taking the first 6 digits of the HMAC digest
    otp = hmac_obj.hexdigest()[:6]
    return otp
