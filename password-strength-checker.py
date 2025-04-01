import re

# Expanded list of common passwords (could be loaded from a file or external source)
common_passwords = {
    "123456", "password", "123456789", "12345", "1234", "qwerty", "abc123", 
    "password1", "123123", "welcome", "letmein", "admin", "password123", "qwerty123",
    "123qwe", "iloveyou", "monkey", "sunshine", "123321", "qwertyuiop", "1q2w3e4r5t",
    "football", "princess", "dragon", "mypassword", "baseball", "trustno1", "starwars",
    "qazwsx", "1qaz2wsx", "letmein1", "welcome123", "shadow", "master", "hello123",
    "123abc", "qwerty1234", "qwerty1", "123qwe123", "abcdef", "superman", "qwertyuiop123",
    "password1a", "football123", "letmein123", "12345abc", "monkey123", "1234qwerty",
    "1qazxsw2", "123qwe123456", "123456a", "password12", "1password", "asdfghjkl"
}

def check_password_strength(password: str) -> str:
    # Password length should be at least 8 characters
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        return "Password must contain at least one digit."
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."
    
    # Check if the password is too common
    if password.lower() in common_passwords:
        return "Password is too common and easily guessable."
    
    # If all conditions are satisfied
    return "Password is strong!"

# Test the function
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))