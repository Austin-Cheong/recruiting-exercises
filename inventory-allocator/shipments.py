#!/usr/bin/env python3
import json

f = open("inputs.txt", "r")
'''
{ apple: 5, banana: 5, orange: 5 }, [{ name: owd, inventory: { apple: 5, banana: 5 } }, { name: dm, inventory: { apple: 5, orange: 5 } }, { name: test, inventory: { apple: 1, banana: 2, orange: 3, dragonfruit: 4 } }]
{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]
{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]
{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]
{ apple: 2 }, [{ name: owd, inventory: { apple: 1 } }]
'''

# Make the input to similar format as JSON:
def prettyInput():

    # Make the orders into JSON format
    # print("Ugly Input = ", line.rstrip())

    # Split the input into orders and inventories
    uglyInput = line.split(", [",1)
    uglyOrders = uglyInput[0]
    # print("Ugly Orders = ", uglyOrders)
    
    # Remove the first and last curly braces. Then separate each pair of items using split..
    uglyOrdersSplit = uglyOrders[2:-2].split(", ")
    # print("Split ugly orders = ", uglyOrdersSplit)
    
    # Add the key-value pairs to the dictionary
    for item in uglyOrdersSplit:        
        pair = item.split(": ")
        key = pair[0]
        val = pair[1]
        orders[key] = int(val)
    
    # print("DICTIONARY Orders = ", orders)
    
#==============================================================================================
    # Make the inventories into JSON format:

    # Should be a list of dictionaries where each separate dictionary is a warehouse
    uglyInventories = uglyInput[1]
    # print("Ugly Inventory = ", "[" + uglyInventories)

    # Do not include newline char and ending ']' bracket
    strippedInventories = uglyInventories.rstrip()[:-1]
    # print("Ugly Stripped Inventory = ", strippedInventories)

    # Separate individual warehouses from the list
    warehouses = strippedInventories.split("}, {") 
        # TODO: Test with different amounts of warehouses instead of just 2... 
    # print("Warehouses = ", warehouses)
    # print("Warehouses 0 = ", warehouses[0] + "}")
    # print("Warehouses 1 = ", "{" + warehouses[1])

    for item in warehouses:
        warehouseInventory = {}
        # print("Current warehouse = ", item)
        name = item.split(", inventory: ")[0].split(": ")[1]
        # print("Name = ", name)

        inventory = item.split(", inventory: ")[1].replace(" } }", " }")
        strippedInventory = inventory[2:-2]
        # print("Inventory = ", strippedInventory)

        splitInventory = strippedInventory.split(", ")
        # print("Split Inventory = ", splitInventory)
        for pair in splitInventory:
            key = str(pair.split(": ")[0])
            val = int(pair.split(": ")[1])
            # print("Key = ", key)
            # print("Val = ", val)
            warehouseInventory[key] = int(val)
        
        # inventories = {name : warehouseInventory}
        inventories[name] = warehouseInventory
    
        # print("DICTIONARY Inventories = ", inventories)
        
def debugPrinting():
    print("Orders:")
    for item in orders:
        print(item, ": ", orders[item])

    print("------------")

    print("Inventories:")
    for item in inventories:
        print(item, ": ", inventories[item])

    # print("Test = ", inventories['owd']['apple'])


for line in f:
    orders = {}
    inventories = {}

    prettyInput()

    # debugPrinting()
    # print("================================== LINE ENDING ==================================")
    
    
    '''
    inventories = { name: { inventory } } 
    '''
    print("Orders = ", orders)
    print("Inventories = ", inventories)
    # print(inventories.keys())
    # print(inventories.values())

    for item in orders:
        requested = orders[item]
        print("Item = ", item)
        print("Requested = ", requested)

        for wh in inventories:
            print("Current warehouse name = ", wh)
            print("Current warehouse ivty = ", inventories[wh])

            if(item in inventories[wh] and requested <= inventories[wh][item]): #TODO: Need to see if the requested amount exists across ALL warehouses...
                print("IN STOCK")
            else:
                print("OUT OF STOCK")

    print("================================== LINE ENDING ==================================")

f.close()
