import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        length = int(input("Enter the length of the password you want to generate: "))
        if length < 1:
            print("Password length must be at least 1.")
        else:
            password = generate_password(length)
            print("Generated password:", password)
            generate_again = input("Do you want to generate another password? (yes/no): ").lower()
            if generate_again != 'yes':
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()
