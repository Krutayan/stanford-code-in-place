"""
Practice Example: Agreement Bot
Course: Stanford Code in Place X
Description: Write a program which asks the user what their favorite animal is, 
and then always responds with "My favorite animal is also ___!" 
(the blank should be filled in with the user-inputted animal).
"""

def main():
    animal = input("What's your favorite animal? ")
    print(f"My favorite animal is also {animal}!")


if __name__ == "__main__":
    main()
