"""
Assignment: Dog Years
Course: Stanford Code in Place X
Week: 2 - Numbers and Random
Description: Converts a human age in calendar years
into equivalent dog years using a multiplier of 7.18.
"""

# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18


def main():
    age = float(input("Enter an age in calendar years: "))
    dog_years = age * DOG_YRS_MULTIPLIER
    print(f"That's {dog_years} in dog years!")


if __name__ == "__main__":
    main()
