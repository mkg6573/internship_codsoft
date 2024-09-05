import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to include all character types.")

    # Define the characters to use for generating the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password includes at least one of each character type
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure at least one of each type of character is included
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Add random characters to reach the desired length
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list of characters to a string
    return ''.join(password)

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            raise ValueError("Length must be at least 1.")
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
