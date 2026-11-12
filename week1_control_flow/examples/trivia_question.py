"""
Practice Example: Trivia Question
Course: Stanford Code in Place X
Description: Write a program that asks the user for a topic. Then, using call_gpt, 
it generates one trivia question about that topic[cite: 13].
"""

from ai import call_gpt

def main():
    topic = input("What topic? ")
    answer = call_gpt(f"Ask one trivia question about {topic}.")
    print(answer)


if __name__ == "__main__":
    main()
