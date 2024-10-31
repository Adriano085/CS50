def calculate(n1, operator, n2):
    match operator:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "/":
            return n1 / n2
        case "*":
            return n1 * n2
        case _:
            return "Invalid Operator!"

def main():
    operators = ["+", "-", "/", "*"]
    exp = input("Expression: ").strip()
    n1, operator, n2 = exp.split()

    if n1.isnumeric() and n2.isnumeric():
        n1 = float(n1)
        n2 = float(n2)
    else:
        return "Please! Enter a valid number."

    return calculate(n1, operator, n2)



if __name__ == "__main__":
    print(main())
