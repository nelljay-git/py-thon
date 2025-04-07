item_name = ["N"]
item_price = ["N"]

while True:
    print("List your shopping list!: ")
    shopping_item = input("Enter your item name: ")
    shopping_price = int(input("Enter your item price: "))

    print(f"{shopping_item} added to your list with the cost of {shopping_price}")

    item_name.append(shopping_item)
    item_price.append(shopping_price)
    total_items = len(item_name)
    print(f"Total items on the list: {total_items}")
    print("1. See lists 2. Delete items")

    confirm = int(input("Enter your choice: "))

    
    if confirm == 1:
        for i in range(total_items):
            print(f"{[i]}. {item_name[i]}, {item_price[i]}")
    elif confirm == 2:
        for i in range(total_items):
            print(f"{[i]}. {item_name[i]}, {item_price[i]}")
        delete = int(input("Choose a number to delete: "))
        item_name.pop(delete)
        item_price.pop(delete)
        