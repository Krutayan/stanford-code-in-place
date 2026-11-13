"""
Twist: Easy Mode (Guess My Animal)
Course: Stanford Code in Place X
Description: Added easy mode selection where GPT appends small clues to incorrect answers[cite: 6].
"""

from animal import get_random_animal
from ai import call_gpt

def main():
    # Choose a random animal
    animal = get_random_animal()
    
    # Ask the player if they want easy mode
    mode = input("Easy mode? Type yes or no: ")
    mode = mode.lower()
    
    # Print the initial message to the user
    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")

    if mode == "yes":
        question = input("Ask me a yes or no question: ")

        # Use GPT to get a yes, no, or correct with a clue
        prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. if not correct add a small clue also."
        gpt_response = call_gpt(prompt)
    
        # Keep letting the user guess as long as its not correct
        while gpt_response != "Correct":
            # Output GPT's response with clue
            print(f"{gpt_response}.")

            # Get the next question
            question = input("Ask me a yes or no question: ")

            # Use GPT to get the response with clue
            prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. if not correct add a small clue also."
            gpt_response = call_gpt(prompt)
    
        print("Correct!")
    else:
        # Standard mode
        question = input("Ask me a yes or no question: ")
 
        # Use GPT to get a strict yes, no, or correct
        prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
        gpt_response = call_gpt(prompt)
    
        # Keep letting the user guess as long as its not correct
        while gpt_response != "Correct":
            # Output GPT's response
            print(f"{gpt_response}.")

            # Get the next question
            question = input("Ask me a yes or no question: ")

            # Use GPT to get the response
            prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
            gpt_response = call_gpt(prompt)
    
        print("Correct!")

if __name__ == "__main__":
    main()
