"""
Assignment: Translation Practice
Course: Stanford Code in Place X
Description: Build a simple language practice tool that asks the user for a language, 
an English word, and their translation, then uses call_gpt to check correctness[cite: 14].
"""

from ai import call_gpt

def main():
    language = input("What language do you want to practice? ")
    word_english = input("Type the word in English: ")
    word = input(f"Type the word in {language}: ")
    word_lower = word.lower()
    
    respond = call_gpt(f"user has chooses {language} language and entered a word '{word_english}' in english and guessed word '{word}' in {language} for this, you check whether it is correct or not answer in yes or no only not even full stop")
    respond_lower = respond.lower()
    
    answer = call_gpt(f"translation of {word_english} in {language}")
    
    if respond_lower == "yes":
        print("Wahoo! You and GPT agreed on the translation.")
    else:
        print(f"Oh no! GPT said that the translation is {answer}")


if __name__ == "__main__":
    main()
