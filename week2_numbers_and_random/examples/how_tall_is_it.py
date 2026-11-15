
"""
Assignment: How Tall Is It?
Course: Stanford Code in Place X
Week: 2 - Numbers and Random
Folder: examples
Description: Uses AI to estimate a landmark's height
and calculates how many people stacked together
would reach its top.
"""

from ai import call_gpt


def main():
    # Add your code here!
    # Input of landmark name and their height from user
    name = input("Name a landmark: ")
    user = float(input("How tall are you in meters? "))
    prompt = f"how tall {name} is, in meters. only answer with a number"
    gpt_response = float(call_gpt(prompt))
    answer = float(gpt_response / user)
    answer = round(answer, 2) #Rounding till 2 decimal.

    #Print the final answers
    print(f"The {name} is {gpt_response} meters tall.")
    print(f"That is about {answer} of ypu stacked up!")


if __name__ == "__main__":
    main()
