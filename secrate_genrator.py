import secrets

# Make a random key

def generate_key(length):

    # Different type of characters
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    special = "!@#$%^&*"

    # Join all characters
    characters = upper + lower + number + special

    # Empty key to store generated characters
    key = ""
    for i in range(length):
        char = secrets.choice(characters)
        key = key + char
    return key

# Check how strong the key is
def check_strength(key):

    # Start with False
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    # Check every character in the key
    for char in key:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        else:
            has_special = True

    # Check the strength
    if has_upper and has_lower and has_number and has_special:
        return "Strong"
    elif has_upper and has_lower and has_number:
        return "Moderate"
    else:
        return "Weak"

# Main program
def main():

    # Keep generating until user says no
    while True:
        n = int(input("Enter Key Length: "))
        # Generate the key
        key = generate_key(n)
        # Check the strength of the key
        strength = check_strength(key)
        print(key)
        print(strength)

        # Ask user if they want another key
        again = input("Do you want another key (y/n): ")
        if again.lower() == "n":
            break

# Start the program
main()

# Never share generaated keys publically
print("Disclaimer - Do not show your key in public")

