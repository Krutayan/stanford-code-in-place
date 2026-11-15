
"""
Assignment: Double It
Course: Stanford Code in Place X
Week: 2 - Numbers and Random
Description: Repeatedly doubles a user-entered number
and prints each result until the value exceeds 100.
"""

def main():
    number = int(input("Enter a number: "))

    while number <= 100:
        new_number = number * 2
        number = new_number
        print(f"{new_number}")


if __name__ == "__main__":
    main()
