"""
Practice Example: Personalized Welcome Message (Welcome Message)
Course: Stanford Code in Place X
Description: Write a program that creates a personalized welcome message for the user. 
Ask them for their name and what city they are from, then print out a nice message.
"""

def main():
    name = input("What is your name? ")
    place = input("What city are you from? ")
    print(f"Hi {name}! It is nice to meet someone from {place}!")


if __name__ == "__main__":
    main()
