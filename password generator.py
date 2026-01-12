import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    all_characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

print("=== Password Generator ===")
length = int(input("Enter password length: "))

password = generate_password(length)
print("Generated Password:", password)
