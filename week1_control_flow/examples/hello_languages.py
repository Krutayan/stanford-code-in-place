"""
Practice Example: Hello in Many Languages
Course: Stanford Code in Place X
Description: Say hello to a user in many different languages! Start with a variable called 
language that holds one language name. Then write a separate if statement for each language, 
so that only the matching greeting prints[cite: 16].
"""

def main():
    language = "French"
    
    if language == "English":
        print("Welcome!")
    if language == "Spanish":
        print("¡Bienvenido!")
    if language == "French":
        print("Bienvenue!")
    if language == "Italian":
        print("Benvenuto!")


if __name__ == "__main__":
    main()
