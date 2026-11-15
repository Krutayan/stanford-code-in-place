
"""
Assignment: Even or Odd
Course: Stanford Code in Place X
Week: 2 - Numbers and Random
Folder: examples
Description: Determines whether a user-entered integer
is even or odd using the modulo operator.
"""

def main():
    # Take input from user
    number = int(input("Enter a number: "))
    remainder = number % 2

    if remainder == 0:
        print(f"{number} is even!")
    else:
        print(f"{number} is odd!")


if __name__ == "__main__":
    main()
