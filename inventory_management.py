# Initial inventory - a list of dictionaries, each representing an item
inventory = [
    {"id": 1, "name": "Laptop", "quantity": 10},
    {"id": 2, "name": "Mouse", "quantity": 25},
    {"id": 3, "name": "Keyboard", "quantity": 15}
]

# Function to display current inventory
def display_inventory():
    print("\nCurrent Inventory:")  # Print heading
    print("{:<5} {:<15} {:<10}".format("ID", "Item Name", "Quantity"))  # Print column headers with formatting

    for item in inventory:  # Loop through each item in the inventory
        print("{:<5} {:<15} {:<10}".format(item['id'], item['name'], item['quantity']))  # Print item details
    print()  # Add empty line for spacing

# Function to add a new item to the inventory
def add_item():
    name = input("Enter item name: ")  
    quantity = int(input("Enter quantity: ")) 
    item_id = max([item['id'] for item in inventory], default=0) + 1  
    inventory.append({"id": item_id, "name": name, "quantity": quantity}) 
    print(f"{name} added with quantity {quantity}.")  # Confirm addition

# Function to update the quantity of an existing item
def update_quantity():
    display_inventory()  # Show current inventory
    item_id = int(input("Enter item ID to update quantity: "))  # Ask user for item ID
    for item in inventory:  # Loop through inventory
        if item['id'] == item_id:  # Check if ID matches
            new_quantity = int(input(f"Enter new quantity for {item['name']}: "))  # Get new quantity
            item['quantity'] = new_quantity  # Update quantity
            print(f"{item['name']} updated to quantity {new_quantity}.")  # Confirm update
            return  # Exit function after update
    print("Item not found.")  # If ID not found

# Function to remove an item from inventory
def remove_item():
    display_inventory()  # Show current inventory
    item_id = int(input("Enter item ID to remove: "))  # Ask for item ID to remove
    for i, item in enumerate(inventory):  # Loop through inventory with index
        if item['id'] == item_id:  # Check if ID matches
            removed = inventory.pop(i)  # Remove item from list
            print(f"{removed['name']} removed from inventory.")  # Confirm removal
            return  # Exit function
    print("Item not found.")  # If ID not found

# Main function to run the program
def main():
    while True:  # Infinite loop until user chooses to exit
        print("\nInventory Management Menu:")  # Menu heading
        print("1. Display Inventory")  # Option 1
        print("2. Add Item")  # Option 2
        print("3. Update Quantity")  # Option 3
        print("4. Remove Item")  # Option 4
        print("5. Exit")  # Option 5
        
        choice = input("Choose an option (1-5): ")  # Get user's menu choice
        
        if choice == '1':  # If choice is 1
            display_inventory()  # Call display function
        elif choice == '2':  # If choice is 2
            add_item()  # Call add function
        elif choice == '3':  # If choice is 3
            update_quantity()  # Call update function
        elif choice == '4':  # If choice is 4
            remove_item()  # Call remove function
        elif choice == '5':  # If choice is 5
            print("Exiting Inventory System.")  # Goodbye message
            
            break  # Exit the loop and end program
        else:
            print("Invalid option. Please try again.")  # Handle invalid input

# Run the main function to start the program
main()
