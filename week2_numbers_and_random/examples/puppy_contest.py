
"""
Assignment: Puppy Contest
Course: Stanford Code in Place X
Week: 2 - Numbers and Random
Folder: examples
Description: Takes scores from three judges, calculates
their average, and prints the puppy's average score.
"""

def main():
    # Take input from the user
    a = int(input("Enter judge 1's score: "))
    b = int(input("Enter judge 2's score: "))
    c = int(input("Enter judge 3's score: "))

    # Calculate the total score
    total = a + b + c

    # Calculate the average
    answer = total / 3

    # Print the average
    print(f"The average score is {answer}")


if __name__ == "__main__":
    main()
