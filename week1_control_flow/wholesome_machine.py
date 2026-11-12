"""
Assignment: Wholesome Machine
Course: Stanford Code in Place X
Description: Write a program which prompts the user to type the affirmation 
"I can do anything I put my mind to." until they type it correctly.
"""

def main():
    # Add your code here!
    answer = input("Please type the following affirmation: I can do anything I put my mind to. ")
    answer_lower = answer.lower()
    solution = "i can do anything i put my mind to."
    
    while answer_lower != solution:
        print("That was not the affirmation.")
        answer = input("Please type the following affirmation: I can do anything I put my mind to. ")
        answer_lower = answer.lower()
    print("That's right! :)")

if __name__ == "__main__":
    main()
