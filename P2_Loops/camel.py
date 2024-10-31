def main():
    string = input("camelCase: ")
    print(snake_case(string))

def snake_case(camel_case):
    snake_case = ""
    for letter in camel_case:
        if letter == letter.upper():
            snake_case += "_"
        snake_case += letter.lower()

    return snake_case


main()
