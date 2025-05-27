itemsInventory = []

def display():
    if not itemsInventory:
        print('Inventory is empty')
    else:
        for item in set(itemsInventory):
            print(f"{item} : {itemsInventory.count(item)}")
        
def add(itemAdd: str):
    itemsInventory.append(itemAdd)
    
def remove(itemRemove: str):
    if itemRemove in itemsInventory:
        itemsInventory.remove(itemRemove)
        print(f"{itemRemove} has been removed")
    else:
        print('The item is not in the inventory')

while True:
    print("\nType an option to interact with the inventory")
    print("display - displays all items with the amount in stock")
    print("add     - adds an item to the inventory")
    print("remove  - removes an item from the inventory")
    
    UserChoice = input().strip().lower()
    
    if UserChoice == 'display':
        display()
        
    elif UserChoice == 'add':
        item = input('Enter the item to add')
        add(item)
        
    elif UserChoice == 'remove':
        item = input('Enter item to remove')
        remove(item)
    else:
        print('Invalid option')






    
    
    
    


        
    
    
   
