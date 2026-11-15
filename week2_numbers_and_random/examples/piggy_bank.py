
"""
Assignment: Piggy Bank
Course: Stanford Code in Place X
Week: 2 - Numbers and Random
Folder: examples
Description: Keeps accepting coin amounts until the
total savings reach at least $10.
"""

def main():
    # Add your code here!
    # Initialize
    sum = float(0)
    
    # Input from user
    amount = float(input("Enter an amount to add: "))

    # Add to sum
    sum = float(sum + amount)

    # print the answer
    print(f"You have saved ${sum}")

    # Loop till reach 10
    while sum < 10:
        amount = float(input("Enter an amount to add: "))
        sum = float(sum + amount)
        print(f"You have saved ${sum}")
    print("You saved enough!")




if __name__ == "__main__":
    main()
