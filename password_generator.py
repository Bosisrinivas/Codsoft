import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 8:
                print("Password length should be at least 8 characters.")
                continue
            password = generate_password(length)
            print(f"Generated Password: {password}")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()



