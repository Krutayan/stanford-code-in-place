"""
Assignment: Secret Code
Course: Stanford Code in Place X
Description: Write a program that asks the user to enter the secret code 
to unlock a treasure chest. The secret code is 'unicorn'. 
If correct, print 'The treasure chest opens!'; otherwise, print 
'Access denied! The treasure stays locked.'
"""

def main():
    # Add your code here!
    code = input("Enter the secret code: ")
    
    if code == "unicorn":
        print("The treasure chest opens!")
    else:
        print("Access denied! The treasure stays locked.")

if __name__ == "__main__":
    main()
