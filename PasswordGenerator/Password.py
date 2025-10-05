import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_characters = lower + upper + digits + symbols

    if not all_characters:
        raise ValueError("You must have something in password, at least one character")

    password = ''  # Initialize password

    for i in range(length):
        random_character = random.choice(all_characters)
        password += random_character

    return password

if __name__ == "__main__":
    print("\nWelcome to password generator")

    length = int(input("Enter the password length: "))

    use_upper = input("You want uppercase letters in password? (y/n): ").lower() == 'y'
    use_digits = input("You want digits in your password? (y/n): ").lower() == 'y'
    use_symbols = input("You want to use symbols in password? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_upper, use_digits, use_symbols)
        print("\nPassword generated:", password)
    except ValueError as e:
        print("Error:", e)
