"""
Assignment: Guess My Animal
Course: Stanford Code in Place X
Description: Implement a fun guessing game called Guess My Animal. The program 
randomly picks an animal, and the user guesses which animal it is by asking 
yes or no questions using call_gpt.
"""

from animal import get_random_animal
from ai import call_gpt

def main():
    animal = get_random_animal()
    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")
    answer = input("Ask me a yes or no question: ")
    
    while answer != animal:
        respond = call_gpt(f"user is guessing the animal {animal}. They asked: {answer}. Respond with yes or no based on whether it describes the animal.")
        print(f"{respond}")
        answer = input("Ask me a yes or no question: ")
        
    print("Correct!")

if __name__ == "__main__":
    main()
