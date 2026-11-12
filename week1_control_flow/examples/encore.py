"""
Practice Example: Encore
Course: Stanford Code in Place X
Description: Play the concert finale again for as long as the user keeps asking for an encore[cite: 16].
"""

def main():
    respond = input("Type encore to hear the finale again: ")
    respond_lower = respond.lower()
    
    while respond_lower == "encore":
        print("The band plays the finale!")
        respond = input("Type encore to hear it again: ")
        respond_lower = respond.lower()
        
    print("The concert is over!")


if __name__ == "__main__":
    main()
