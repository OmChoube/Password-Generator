import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                     use_numbers=True, use_symbols=True):
    """
    Generate a random password that ensures at least one character 
    from each selected category.
    
    Args:
        length (int): Length of the password (must be at least as long as the selected character types)
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_numbers (bool): Include numbers
        use_symbols (bool): Include special symbols
        
    Returns:
        str: Securely generated password
    """
    if length < 4:  
        raise ValueError("Password length must be at least 4.")

    # Define character sets
    char_sets = []
    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)
    if use_numbers:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append(string.punctuation)
        
    if not char_sets:
        raise ValueError("At least one character type must be selected.")

    # Secure random generator
    secure_random = random.SystemRandom()

    # Ensure at least one character from each selected type
    password_chars = [secure_random.choice(char_set) for char_set in char_sets]

    # Fill the rest of the password length
    all_chars = ''.join(char_sets)
    password_chars.extend(secure_random.choice(all_chars) for _ in range(length - len(password_chars)))

    # Shuffle to randomize order
    secure_random.shuffle(password_chars)
    
    return ''.join(password_chars)


def get_yes_no_input(prompt):
    """Helper function to get a yes/no user input."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Invalid input! Please enter 'y' or 'n'.")


def main():
    print("==== Random Password Generator ====")

    while True:
        try:
            # Get user input for password length
            length = int(input("Enter password length (8-50): "))
            if not 8 <= length <= 50:
                print("Password length must be between 8 and 50 characters.")
                continue  # Re-prompt
            
            # Get character type preferences
            use_uppercase = get_yes_no_input("Include uppercase letters? (y/n): ")
            use_lowercase = get_yes_no_input("Include lowercase letters? (y/n): ")
            use_numbers = get_yes_no_input("Include numbers? (y/n): ")
            use_symbols = get_yes_no_input("Include special symbols? (y/n): ")

            # Validate character selection
            if not any([use_uppercase, use_lowercase, use_numbers, use_symbols]):
                print("Error: You must select at least one character type.")
                continue  # Re-prompt

            # Generate and display password
            password = generate_password(
                length, use_uppercase, use_lowercase, use_numbers, use_symbols
            )
            print("\nYour generated password is:")
            print(password)

            break  # Exit loop after successful generation

        except ValueError as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()
