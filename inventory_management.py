 # Initial inventory
inventory = {
    "Apple": 100,
    "Banana": 80,
    "Orange": 120
}

# Display current inventory
print("Current Inventory:")
for item, qty in inventory.items():
    print(f"- {item}: {qty} units")

    print()

# Updates to apply
updates = [
    {"item": "Banana", "qty": -10},
    {"item": "Apple", "qty": 30},
    {"item": "Grapes", "qty": 50}
]

# Apply updates
for update in updates:
    item = update["item"]
    qty = update["qty"]

    if item in inventory:
        inventory[item] += qty
        print(f"Updated '{item}' by {qty} units.")
    else:
        inventory[item] = qty
        print(f"Added new item '{item}' with {qty} units.")

# Display updated inventory
print("\nAfter Updates:")
for item, qty in inventory.items():
    print(f"- {item}: {qty} units")