"""
Practice Example: Secret Word
Course: Stanford Code in Place X
Description: Keep asking for a secret word until the user types it correctly. The secret word is sunrise.[cite: 14]
"""

def main():
    word = input("Type the secret word: ")
    word_lower = word.lower()
    while word_lower != "sunrise":
        print("Try again!")
        word = input("Type the secret word: ")
        word_lower = word.lower()
    print("Ready!")


if __name__ == "__main__":
    main()
