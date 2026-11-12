"""
Practice Example: Spanish Quiz
Course: Stanford Code in Place X
Description: Quiz the user on one Spanish word, using != to check their answer. 
Ask the user how to say Hello in Spanish. If their response is not Hola, 
print That is incorrect. Otherwise, print This is correct![cite: 13]
"""

def main():
    answer = input("How do you say Hello in Spanish? ")
    if answer != "Hola":
        print("That is incorrect.")
    else:
        print("This is correct!")


if __name__ == "__main__":
    main()
