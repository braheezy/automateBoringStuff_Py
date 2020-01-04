inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + f" {k}")
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for newItem in addedItems:
        if inventory.setdefault(newItem, 1) != 1:
            # already exists, so increment
            inventory[newItem] += 1

    displayInventory(inventory)


addToInventory(inv, dragonLoot)