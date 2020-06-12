#!/usr/bin/python

class InventoryAllocator:
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory
        self.distribution = []
    
    # Add the inventory items to the distribution list
    def addToList(self, name, item, qty):
        for wh in self.distribution:
            if name in wh: # warehouse is in list
                # add the inventory and leave the function
                wh[name][item] = qty
                return
        
        # if it reaches here, then the warehouse wasn't in the distribution list yet
        self.distribution.append({name: {item: qty}})
        return

    # Search to see if the given item and quantity is available from the warehouses
    def searchInWarehouse(self, item, qty):
        for wh in self.inventory:
            whInv = wh['inventory']
            if item in whInv:
                if whInv[item] >= qty:
                    whInv[item] -= qty
                    self.order[item] -= qty
                    self.addToList(wh["name"], item, qty)
                    if self.order[item] == 0:
                        return
                else:
                    self.order[item] -= whInv[item]
                    whInv[item] = 0
                    self.addToList(wh["name"], item, qty)

        # at this point, we've looked at all warehouses, if we still don't have enough, then no allocation
        if self.order[item] > 0:
            self.distribution = []

    # Go through inventory to try and fulfill the order
    def allocateInventory(self):
        # Go through each item in the order and search for it in the warehouses
        for item in self.order:
            if self.order[item] > 0:
                self.searchInWarehouse(item, self.order[item])
