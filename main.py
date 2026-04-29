import hmac
import secrets
from algorithm import generate_otp

users_db = {}

def register_user():
    while True:
        username = input("Enter username: ")
        if username in users_db:
            print("User already exists. Try again with a different username.")
        else:
            break
    user_secret = secrets.token_hex(16)
    users_db[username] = {"secret": user_secret}
    print( "User registered successfully. Your secret key is: {}".format(user_secret))


def login_user():
    for i in range(3):
        username = input("Enter username: ")
        if username not in users_db:
            print("User not found. Please register first or try again.")
        else:
            print(f"Hello {username}")
            return username

def generate_challenge_and_validate(username):
    challenge = secrets.token_hex(8)
    print(f"Your challenge: {challenge}")
    print("Use this challenge and your secret key in authenticator.py to generate your OTP.")

    #user response
    user_response = input("Enter your OTP response: ")

    # Validate OTP
    secret = users_db[username]["secret"]
    expected_response = generate_otp(secret, challenge)
    if hmac.compare_digest(user_response, expected_response):
        print("\n[SUCCESS] Login correct! Access granted.")
        return True
    else:
        print("\n[FAILED] Invalid OTP. Access denied.")
        return False


# --------------------- Start of the main program ---------------------
def main():
    print("Welcome to the OTP Generator!")
    while True:
        print("\nMenu:")
        print("1. Register User")
        print("2. Log in")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
            print("\nNow you can login with your username and the generated OTP.")
        elif choice == '2':
            username = login_user()
            if generate_challenge_and_validate(username):
                print("You have successfully logged in!")
                print("Now you know how to use OTP for secure authentication.")
                print("Bye!")
            else:
                print("Login failed. Try again.")


        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

