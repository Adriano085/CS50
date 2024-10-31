def main():
    msg_in = input("Input: ")
    msg_out = remove_vowels(msg_in)
    print(msg_out)

def remove_vowels(msg):
    vowels_list = ["a","e","i","o","u"]
    msg_without_vowels = ""

    for letter in msg:
        if letter.lower() not in vowels_list:
            msg_without_vowels += letter
    return msg_without_vowels

if __name__ == "__main__":
    main()
