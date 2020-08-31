#!/usr/bin/env python3
import json

f = open("inputs.txt", "r")
open("outputs.txt", "w").close()
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
    placedOrders = []

    for item in orders:
        requested = orders[item]
        print("~~~~~ Item = ", item, " ||| Requested = ", requested, "~~~~~")
        # answer = [] 
        for wh in inventories:
            print("Current warehouse name = ", wh)
            print("Current warehouse ivty = ", inventories[wh])
            print("Current requested = ", requested)
            if(requested == 0):
                break
            else:
                # if(item in inventories[wh] and requested <= inventories[wh][item]): #TODO: Need to see if the requested amount exists across ALL warehouses...
                if(item in inventories[wh] and inventories[wh][item] != 0):
                    # If the requested amount is EQUAL or GREATER than the current wh's stock, take all of that stock from the wh
                    if(requested >= inventories[wh][item]):
                        requested -= inventories[wh][item]
                        pair = {}
                        stock = {}
                        # Take the full amount of stock from the warehouse:
                        stock[item] = inventories[wh][item]
                        pair[wh] = stock
                        placedOrders.append(pair)

                        # The warehouse then has depleted stock of that item
                        inventories[wh][item] = 0 
                
                    # If the requested amount is LESS than the current wh's stock, take just the requested amount, then reduce requested to 0
                    else:
                        remainingStock = inventories[wh][item] - requested
                        inventories[wh][item] = remainingStock
                        # requested -= (inventories[wh][item] - remainingStock) # 5 - (5) = 0
                        pair = {}
                        stock = {}
                        stock[item] = requested
                        pair[wh] = stock
                        placedOrders.append(pair)
                        
                        # The requested amount is reduced to 0 since it can be fulfilled by this current wh
                        requested = 0

            print("ANSWERS IN PROGRESS = ", placedOrders)
        print("REMAINING = ", requested)
        output = open("outputs.txt", "a")
        if(requested > 0):
            placedOrders = []
            break

        # for subItem in answer:
        #     placedOrders.append(subItem)
            
    print("REMAINING = ", requested)
    output = open("outputs.txt", "a")
    if(requested <= 0):
        print("ANSWERS = ", placedOrders)
        formatOutput = str(placedOrders).replace('\'', '').replace('{', '{ ').replace('}',' }')
        output.write(formatOutput + '\n')
    else:
        # print("REQUESTED COULD NOT BE FULLFILLED...")
        # print("ANSWERS = ", answer)
        print([])
        output.write(str([]) + '\n' )
    output.close()

    print("================================== LINE ENDING ==================================")

f.close()
