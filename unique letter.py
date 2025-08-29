text = input("Enter a sentence: ")

text = text.replace(" ", "").lower()

unique_letters = set(text)

print("Unique letters used:", unique_letters)