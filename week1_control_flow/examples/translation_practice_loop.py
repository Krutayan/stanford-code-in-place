"""
Assignment: Translation Practice, Again
Course: Stanford Code in Place X
Description: In the last lesson you built a language practice tool that quizzed the user on a single word. 
Now use a while loop to keep quizzing them until they want to stop[cite: 16].
"""

from ai import call_gpt

def main():
    language = input("What language do you want to practice? ")
    word_english = input("Type a word in English, or done to quit: ")
    word_english_lower = word_english.lower()
    word = input("Type the word in Spanish: ")
    
    while word_english_lower != "done":
        respond = call_gpt(f"user has chooses {language} language and entered a word '{word_english}' in english and guessed word '{word}' in {language} for this, you check whether it is correct or not answer in yes or no only not even full stop")
        respond_lower = respond.lower()
        answer = call_gpt(f"translation of {word_english} in {language}")
        
        if respond_lower == "yes":
            print("Wahoo! You and GPT agreed on the translation.")
        else:
            print(f"Oh no! GPT said that the translation is {answer}")
            
        word_english = input("Type a word in English, or done to quit: ")
        word_english_lower = word_english.lower()
        
        if word_english_lower != "done":
            word = input("Type the word in Spanish: ")
            
    print("Nice practicing with you!")


if __name__ == "__main__":
    main()
