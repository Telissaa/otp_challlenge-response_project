from algorithm import generate_otp

print("Hello do you want to generate OTP? (yes/no)")
answer = input().lower()
if answer == "yes":
    print("Please insert your secret key:")
    secret_key = input()
    print("Please insert the challenge:")
    challenge = input()
    otp = generate_otp(secret_key, challenge)
    print(f"Your OTP is: {otp}")
else:
    print("Goodbye!")