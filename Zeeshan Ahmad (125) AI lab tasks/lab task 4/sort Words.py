def sort_words(text):
    words = text.split()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i].lower() > words[j].lower():
                words[i], words[j] = words[j], words[i]
    return " ".join(words)

text = input("Enter a sentence to sort: ")
print(sort_words(text))
