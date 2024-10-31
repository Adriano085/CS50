def greeting(msg):
    if msg[:5] == "hello":
        return "$0"
    elif msg[0:1] == "h":
        return "$20"
    else:
        return "$100"


msg = input("Greeting: ").lower().strip()

print(greeting(msg))