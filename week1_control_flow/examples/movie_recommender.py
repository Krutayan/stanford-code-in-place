"""
Practice Example: Movie Recommender
Course: Stanford Code in Place X
Description: Write a program that asks the user what genre of movie they're in the mood for. 
Then, using call_gpt, it generates one movie recommendation and displays it.[cite: 22]
"""

from ai import call_gpt

def main():
    genre = input("What genre are you in the mood for? ")
    answer = call_gpt(f"Recommend one {genre} movie. Just the title.")
    print(answer)

if __name__ == "__main__":
    main()
