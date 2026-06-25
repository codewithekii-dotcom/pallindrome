def is_palindrome(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]
word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")