"""
Practice Example: Echo Until Done
Course: Stanford Code in Place X
Description: Echo back everything the user types, until they type done.[cite: 15]
"""

def main():
    message = input("Type a message, or done: ")
    message_lower = message.lower()
    while message_lower != "done":
        print(f"{message}")
        message = input("Type a message, or done: ")
        message_lower = message.lower()


if __name__ == "__main__":
    main()
