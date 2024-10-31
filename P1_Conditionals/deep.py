def answer(num):
    if num == "42" or num == "forty two":
        return "Yes"
    return "No"

num = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower().strip().replace("-", " ")
print(answer(num))