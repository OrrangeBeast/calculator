from functions import *

def main():
    print('Hello! Welcome to my calculator. Type "quit" to quit.')
    name = get_input("Enter your name: ")
    print(f"\nHi, {name.strip()}!")
    
    first_num = get_input("Enter your first number.\n")
    
    operator = get_input("\nEnter your operation. (+, -, *, /)\n")
    while operator.strip() not in ["+", "-", "*", "/"]:
        print("\nINVALID OPERATOR.")
        operator = get_input("Invalid operator. Try again.\n")

    second_num = get_input("\nEnter your second number.\n")

    try:
        print(f"\n{first_num} {operator} {second_num} = {get_solution(first_num, operator, second_num)}")
    except ValueError:
        print(f'\nIVALID PROBLEM: "{first_num} {operator} {second_num}"\nEXITING...')

if __name__ == "__main__":
    main()