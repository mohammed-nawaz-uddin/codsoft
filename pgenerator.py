import random
import string

def generate_password(length):
    # Define the character set to use: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # User input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 8 characters): "))
            if length < 8:
                print("Password length should be at least 8 characters. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Generate and display the password
    generated_password = generate_password(length)
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()