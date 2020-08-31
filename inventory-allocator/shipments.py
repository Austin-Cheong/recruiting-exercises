# !/usr/bin/env python3

def main(line):
    orders = {}
    inventories = {}
    # Make the orders into JSON format
    # Split the input into orders and inventories
    uglyInput = line.split(", [",1)
    uglyOrders = uglyInput[0]
    
    # Remove the first and last curly braces. Then separate each pair of items using split()
    uglyOrdersSplit = uglyOrders[2:-2].split(", ")
    
    # Add the key-value pairs to the dictionary
    for item in uglyOrdersSplit:        
        pair = item.split(": ")
        key = pair[0]
        val = pair[1]
        orders[key] = int(val)
    
    # Make the inventories into JSON format:    
    uglyInventories = uglyInput[1]

    # Do not include newline char and ending ']' bracket
    strippedInventories = uglyInventories.rstrip()[:-1]

    # Separate individual warehouses from the list
    warehouses = strippedInventories.split("}, {") 

    for item in warehouses:
        warehouseInventory = {}
        # Get the name of the warehouse
        name = item.split(", inventory: ")[0].split(": ")[1]
        # Get the respective inventory of the warehouse
        inventory = item.split(", inventory: ")[1].replace(" } }", " }")

        splitInventory = inventory[2:-2].split(", ")
        for pair in splitInventory:
            key = str(pair.split(": ")[0])
            val = int(pair.split(": ")[1])
            warehouseInventory[key] = int(val)
        
        inventories[name] = warehouseInventory

    #  Shipments logic start here:    
    # This list will contain the answer
    placedOrders = [] 

    for item in orders:
        requested = orders[item]
        for wh in inventories:
            if(requested == 0):
                break
            else:
                # If the desired item exists and is in stock
                if(item in inventories[wh] and inventories[wh][item] != 0):
                    # If the requested amount is EQUAL or GREATER than the current wh's stock, take all of that stock from the wh
                    if(requested >= inventories[wh][item]):
                        # Update the amount of the item being requested
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
                        # Update the amount of the item being requested
                        inventories[wh][item] -= requested

                        pair = {}
                        stock = {}
                         # Take the requested amount of stock from the warehouse:
                        stock[item] = requested
                        pair[wh] = stock
                        placedOrders.append(pair)
                        
                        # The requested amount is reduced to 0 since it can be completely fulfilled by this current wh
                        requested = 0

        # If there is some item requested remaining, then it can't be completely fulfilled by all of the warehouses, so the output is empty
        if(requested > 0): 
            placedOrders = []
            break 

    # Make the output similar to the format of the input (only applicable to nonempty list):
    formatOutput = str(placedOrders).replace('\'', '').replace('{', '{ ').replace('}',' }')
    
    return formatOutput
