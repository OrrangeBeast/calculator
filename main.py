from operators import *

def main():
    print("Hello! Welcome to my calculator.")
    name = input("Enter your name: " )
    print(f"Hi, {name}!")
    first_num = input("Enter your first number.\n")
    while first_num != int:
        print("\nINVALID NUMBER.\nTry again.")
        first_num = input()
    operator = input("Enter your operation.\n")
    if operator != "+" or "-" or "*" or "/":
        print("\nINVALID OPERATOR.\nEXITING...")
        return
    second_num = input("Enter your second number.\n")
    if second_num != int:
        print("\nINVALID NUMBER.\nEXITING...")
        return
    print(f"The answer is {solution(int(first_num), operator, int(second_num))}.")
if __name__ == "__main__":
    main()