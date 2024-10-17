from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

calc_operation = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator():
    print(logo)

    continue_calc = True
    ans = 0
    first_num = float(input("What's the first number?: "))
    while continue_calc:

        for op in calc_operation:
            print(op)
        operation = input("Pick an operation: ")
        next_num = float(input("What's the next number:"))

        for op in calc_operation:
            if op == operation:
                ans = calc_operation[op](first_num,next_num)
        print(f"{first_num} {operation} {next_num} = {ans}")

        calc = input(f"Type 'y' to continue calculating with {ans}, or type 'n to start a new calculation:").lower()
        if calc == "y":
            continue_calc = True
            first_num = ans
        else:
            ans = 0
            continue_calc = False
            print("\n"*50)
            calculator()

calculator()




