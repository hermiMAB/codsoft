import random
import string

def generate_password(length):
  """Generates a random password of the specified length."""

  # Define character sets for password complexity
  characters = string.ascii_letters + string.digits + string.punctuation

  # Generate a random password using the chosen characters
  password = ''.join(random.choice(characters) for i in range(length))

  return password

if __name__ == "__main__":
  # Prompt the user for password length
  length = int(input("Enter the desired password length: "))

  # Generate and display the password
  password = generate_password(length)
  print("Generated Password:", password)