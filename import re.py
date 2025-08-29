import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Missing uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Missing lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Missing digit")

    if re.search(r"[\W_]", password):
        score += 1
    else:
        feedback.append("Missing special character")

    common_words = ['password', 'admin', '1234', 'iloveyou', 'welcome']
    if not any(word in password.lower() for word in common_words):
        score += 1
    else:
        feedback.append("Contains common/dictionary word")

    # Result interpretation
    if score <= 2:
        level = "Weak"
    elif score <= 4:
        level = "Moderate"
    else:
        level = "Strong"
    return score, level, feedback

password = input("Enter a password to check strength: ")
score, level, feedback = check_password_strength(password)

print(f"\nPassword Strength: {level} ({score}/6)")
if feedback:
    print("Issues found:")
    for f in feedback:
        print(f"- {f}")
