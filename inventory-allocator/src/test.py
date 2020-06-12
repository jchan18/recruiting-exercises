import unittest
from InventoryAllocator import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):
    def test_happyPath(self):
        order = {"apple": 1}
        inventory = [{"name": "owd", "inventory": {"apple": 1}}]
        expected = [{"owd": {"apple": 1}}]

        ia = InventoryAllocator(order, inventory)
        ia.allocateInventory()

        self.assertEqual(ia.distribution, expected)
    
    def test_splitAcross(self):
        order = { 'apple': 5, 'banana': 5, 'orange': 5 }
        inventory = [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ]
        expected = [{"owd": {"apple": 5, "orange": 5}}, {"dm": {"banana": 5}}]
        
        ia = InventoryAllocator(order, inventory)
        ia.allocateInventory()

        self.assertEqual(ia.distribution, expected)

    def test_noInventory(self):
        order = { 'apple': 1 }
        inventory = [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]
        expected = []

        ia = InventoryAllocator(order, inventory)
        ia.allocateInventory()

        self.assertEqual(ia.distribution, expected)
    
    def test_someHasInventory(self):
        order = { 'apple': 5, 'banana': 10 }
        inventory = [{ 'name': 'owd', 'inventory': { 'apple': 5, 'banana': 5 } }]
        expected = []

        ia = InventoryAllocator(order, inventory)
        ia.allocateInventory()

        self.assertEqual(ia.distribution, expected)
    
    def test_choosesCheapestOption(self):
        order = {'apple': 5}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'de', 'inventory': {'apple': 5}}]
        expected = [{'owd': {'apple': 5}}]

        ia = InventoryAllocator(order, inventory)
        ia.allocateInventory()

        self.assertEqual(ia.distribution, expected)


if __name__ == '__main__':
    unittest.main()