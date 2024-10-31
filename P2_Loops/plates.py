def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    if not s[:2].isalpha():
        return False

    has_number = False
    for char in s:
        if char == "0" and not has_number:
            return False

        if char.isnumeric() and not has_number:
            has_number = True

        if char.isalpha() and has_number:
            return False

        if char in ['.', '?', '!', ' ']:
            return False

    return True


main()