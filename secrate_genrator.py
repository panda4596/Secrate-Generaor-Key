import secrets

def generate_key(length):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    special = "!@#$%^&*"

    characters = upper + lower + number + special

    secrets.choice(characters)

    key = ""
    for i in range(length):
        char = secrets.choice(characters)
        key = key + char
    return key

def check_strength(key):
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    for char in key:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        else:
            has_special = True

    if has_upper and has_lower and has_number and has_special:
        return "Strong"
    elif has_upper and has_lower and has_number:
        return "Moderate"
    else:
        return "Weak"

def main():
    while True:
        n = int(input("Enter Key Length: "))
        key = generate_key(n)
        strength = check_strength(key)
        print(key)
        print(strength)

        again = input("Do you want another key (y/n): ")
        if again.lower() == "n":
            break

main()
print("Disclaimer - Do not show your key in public")

