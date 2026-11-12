"""
Assignment: AI Joke Bot
Course: Stanford Code in Place X
Description: Write a program that tells jokes! Your program will greet the user, 
ask if they'd like to hear a joke, and then use AI to come up with one. As long 
as the user keeps saying "yes," your program should keep the jokes coming. 
When they finally say "no," the program ends.
"""

from ai import call_gpt

def main():
    print("Hello! I am an AI joke bot.")
    answer = input("Do you want to hear a joke? Type yes or no: ")
    answer_lowercase = answer.lower()

    while answer_lowercase == "yes":
        joke = call_gpt("Tell a joke!")
        print(f"{joke}")
        answer = input("Do you want to hear a joke? Type yes or no: ")
        answer_lowercase = answer.lower()

if __name__ == "__main__":
    main()
