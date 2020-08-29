#!/usr/bin/env python3
import json

# print("Hello World!")

    # # some JSON:
    # x =  '{ "name":"John", "age":30, "city":"New York"}'

    # # parse x:
    # y = json.loads(x)

    # # the result is a Python dictionary:
    # print(y["age"])

f = open("inputs.txt", "r")

for line in f:
    orders = {}
    inventories = {}

    print("Ugly Input = ", line.rstrip())

    uglyInput = line.split(", [",1)
    
    # Should simply be a dictionary
    uglyOrders = uglyInput[0]
    print("Ugly Orders = ", uglyOrders)
    # Remove the curly braces...
    uglyOrdersSplit = uglyOrders[2:-2].split(", ")
    print("Split ugly orders = ", uglyOrdersSplit)
    for item in uglyOrdersSplit:        
        pair = item.split(": ")
        key = pair[0]
        val = pair[1]
        orders[key] = int(val)
    print("Dict Orders = ", orders)

    print("============================================================================================================================")

    # Should be a list of dictionaries where each separate dictionary is a warehouse
    uglyInventories = uglyInput[1]
    # print("Ugly Inventory = ", "[" + uglyInventories)
    strippedInventories = uglyInventories.rstrip()[:-1]
    print("Ugly Inventory = ", strippedInventories)
    warehouses = strippedInventories.split("}, {") # TODO: Test with different amounts of warehouses instead of just 2... 
    print("Warehouses = ", warehouses)
    # print("Warehouses 0 = ", warehouses[0] + "}")
    # print("Warehouses 1 = ", "{" + warehouses[1])
    for item in warehouses:
        print("Current warehouse = ", item)
        name = item.split(", inventory: ")[0].split(": ")[1]
        print("Name = ", name)
        inventory = item.split(", inventory: ")[1].replace(" } }", " }")
        strippedInventory = inventory[2:-2]
        print("Inventory = ", strippedInventory)
        splitInventory = strippedInventory.split(", ")
        print("Split Inventory = ", splitInventory)
        for pair in splitInventory:
            key = str(pair.split(": ")[0])
            val = int(pair.split(": ")[1])
            print("Key = ", key)
            print("Val = ", val)
            inventories[key] = int(val)
    print("Dict Inventories = ", inventories)
            

f.close()
