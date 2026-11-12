"""
Practice Example: Simple Chatbot
Course: Stanford Code in Place X
Description: Write a simple chatbot program where a user can continually ask questions 
to the AI model until they type "bye" to end the conversation[cite: 15].
"""

from ai import call_gpt

def main():
    message = input("You: ")
    message_lower = message.lower()
    
    while message_lower != "bye":
        answer = call_gpt(f"{message}")
        print(f"{answer}")
        message = input("You: ")
        message_lower = message.lower()
        
    print("Goodbye!")


if __name__ == "__main__":
    main()
