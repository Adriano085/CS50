items_list = []
while True:
    try:
        item = input()
        if item:
            items_list.append(item)
    except EOFError:
        print()
        break

unique_items = set(items_list)

for item in sorted(unique_items):
    print(f'{items_list.count(item)} {item.upper()}')