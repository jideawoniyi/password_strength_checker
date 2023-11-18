import re
import getpass

def check_password_strength(password):
    # Criteria checks
    min_length = 8

    has_lowercase = bool(re.search(r"[a-z]", password))
    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_number = bool(re.search(r"\\d", password))
    has_special = bool(re.search(r"[^a-zA-Z\\d\\s]", password))

    common_passwords = ["password", "1234", "qwerty", "admin"]
    is_common = any(common in password for common in common_passwords)

    # Rating password strength
    strength = "Weak"  # Default strength
    if len(password) >= min_length:
        if has_lowercase and has_uppercase and has_number and has_special and not is_common:
            strength = "Very Strong"
        elif (has_lowercase or has_uppercase) and has_number:
            strength = "Moderate"
        else:
            strength = "Weak"
    return strength

if __name__ == "__main__":
    password = getpass.getpass("Enter your password to check its strength: ")
    result = check_password_strength(password)
    print(f"Your password is {result}!")
