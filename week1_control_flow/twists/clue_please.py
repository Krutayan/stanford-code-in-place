"""
Twist: Clue Please! (Guess My Animal)
Course: Stanford Code in Place X
Description: Added hint support allowing players to type 'hint' to receive a clue from GPT[cite: 5].
"""

from animal import get_random_animal
from ai import call_gpt

def main():
    # Choose a random animal
    animal = get_random_animal()
    
    # Print the initial message to the user
    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")

    # Get their first guess
    question = input("Ask me a yes or no question: ")

    # Use GPT to get a yes, no, or correct
    prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
    gpt_response = call_gpt(prompt)
    
    # Keep letting the user guess as long as its not correct
    while gpt_response != "Correct":
        # Output GPT's response
        print(f"{gpt_response}.")

        # Get the next question or hint request
        question_hint = input("Ask me a yes or no question, or type hint: ")
        question_hint_lower = question_hint.lower()

        # Handle hint requests in a loop if the user asks for hints multiple times
        while question_hint_lower == "hint":
            hint_prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked for a hint. Please provide a helpful clue about the animal without giving it away entirely."
            gpt_response = call_gpt(hint_prompt)
            print(f"{gpt_response}")
            
            question_hint = input("Ask me a yes or no question, or type hint: ")
            question_hint_lower = question_hint.lower()

        # Use GPT to get the response for a regular question
        prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question_hint}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
        gpt_response = call_gpt(prompt)
    
    print("Correct!")

if __name__ == "__main__":
    main()
