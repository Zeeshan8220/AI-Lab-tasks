def remove_punctuation(text):
    result = ""
    for char in text:
        if char.isalnum() or char.isspace():
            result += char
    return result

text = input("Enter a string with punctuation: ")
print(remove_punctuation(text))
