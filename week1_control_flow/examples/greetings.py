"""
Practice Example: Greetings!
Course: Stanford Code in Place X
Description: Ask the user what part of the day it is for them, then greet them accordingly. 
If they answer morning, print Good morning! Otherwise, print Good evening! 
Then print Have a great day! — no matter what they answered.
"""

def main():
    time = input("Is it morning or night? ")
    
    if time == "morning":
        print("Good morning!")
    else:
        print("Good evening!")
        
    print("Have a great day!")


if __name__ == "__main__":
    main()
