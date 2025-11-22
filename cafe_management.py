menu = {
    "pizza": 149,
    "burger": 99,
    "coffee": 40,
    "tea": 15,
    "sandwich": 70,
    "pasta": 120,
}

print("\n\t\t\t---Welcome To Diva Cafe---")
print("Choose item From the Menu :-")
user_choice = input("\npizza : 149\nburger : 99\ncoffee : 40\ntea : 15\nsandwich : 70\npasta : 120\n\nChoose :-")

total = 0  # ✅ Initialize total at the start

if user_choice in menu:
    quantity1 = int(input("Enter Quantity: "))
    print(f"Your order {user_choice} - {menu[user_choice]} will be added")
    total += menu[user_choice] * quantity1   # ✅ Add first item to total

    print("Want to add another item in list: yes/no")
    choice = input()

    if choice == "yes":
        user_choice2 = input("Enter Item: ")

        if user_choice2 in menu:
            quantity2 = int(input("Enter Quantity: "))
            print(f"item {user_choice2} - {menu[user_choice2]} will be added")
            total += menu[user_choice2] * quantity2   # ✅ Add second item to total
        else:
            print("Sorry we couldn't find any item related to", user_choice2)

else:
    print("Sorry we couldn't find any item related to", user_choice)

print("\n--- Your Bill ---")
print(f"Total Amount: ₹{total}.00")
print("Thanks for visiting Diva Cafe!")
print("Have a Beautiful Day... ")
