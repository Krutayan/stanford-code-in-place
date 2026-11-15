
"""
Assignment: Split the Bill
Course: Stanford Code in Place X
Week: 2 - Numbers and Random
Folder: examples
Description: Divides a total bill among multiple people
and rounds each person's share to two decimal places.
"""

def main():
    # Take input from user for bill
    bill = float(input("Enter the total bill: "))

    # Take input from user for number of people
    people = int(input("Enter the number of people: "))

    # Calculate each person's share
    answer = bill / people
    answer = round(answer, 2)   # to round of decimal places

    # Print the answer
    print(f"Each person owes ${answer}")


if __name__ == "__main__":
    main()
