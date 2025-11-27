import sys

def get_input(message):
    answer = input(message)
    if answer.lower() == "quit":
        print("\nUSER HAS QUIT.\nEXITING...")
        sys.exit()
    return answer

def get_solution(num_1, operator, num_2):
    if operator == "+":
        return num_1 + num_2
    if operator == "-":
        return num_1 - num_2
    if operator == "*":
        return num_1 * num_2
    if operator == "/":
        return num_1 / num_2