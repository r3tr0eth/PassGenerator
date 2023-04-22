import random
import string

def generate_password(length=16):
    """Generate a strong password with the specified length"""
    # Define the characters to use in the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = '!@#$%^&*()_+-={}[]|\\:;<>,.?/~`'

    # Create a list of all possible characters
    all_chars = lowercase_letters + uppercase_letters + digits + symbols

    # Shuffle the characters to create a random order
    shuffled_chars = random.sample(all_chars, len(all_chars))

    # Choose the first `length` characters from the shuffled list
    password_chars = shuffled_chars[:length]

    # Join the password characters into a string
    password = ''.join(password_chars)

    return password

password = generate_password()
print(password)