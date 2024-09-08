import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    
    characters = string.ascii_lowercase  

    if use_uppercase:
        characters += string.ascii_uppercase  

    if use_digits:
        characters += string.digits  

    if use_special:
        characters += string.punctuation  

    
    if len(characters) == 0:
        print("You must include at least one character set (uppercase, digits, or special characters).")
        return None

    
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    print("Welcome to the Password Generator!")

    
    while True:
        try:
            length = int(input("Enter the desired length for the password (e.g., 8, 12, 16): "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

   
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    
    password = generate_password(length, use_uppercase, use_digits, use_special)

    if password:
        
        print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()
