from operators import *

def main():
    print("Hello! Welcome to my calculator.")
    name = input("Enter your name: " )
    print(f"\nHi, {name}!")
    
    first_num = input("Enter your first number.\n")
    
    operator = input("\nEnter your operation.\n")
    while operator not in ["+", "-", "*", "/"]:
        print("\nINVALID OPERATOR.\nTry again.")
        operator = input()

    second_num = input("\nEnter your second number.\n")

    try:
        print(f"\nThe answer is {solution(int(first_num), operator, int(second_num))}.")
    except ValueError:
        print(f'\nIVALID PROBLEM: "{first_num} {operator} {second_num}"\nEXITING...')

if __name__ == "__main__":
    main()