"""
Practice Example: Riddle Me This
Course: Stanford Code in Place X
Description: Use call_gpt to generate a riddle about the topic that the user inputs[cite: 21].
"""

from ai import call_gpt

def main():
    topic = input("Enter a topic: ")
    answer = call_gpt(f"make a riddle on {topic}")
    print(answer)

if __name__ == "__main__":
    main()
