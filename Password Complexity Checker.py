import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@#$%^&+=]', password) is not None

    
    criteria_met = sum([length_criteria, upper_case_criteria, lower_case_criteria,
                        digit_criteria, special_char_criteria])

    
    if criteria_met == 5:
        strength = "Strong"
    elif criteria_met >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength


password = input("Enter a password: ")
strength = check_password_strength(password)
print(f"The strength of your password is: {strength}")
