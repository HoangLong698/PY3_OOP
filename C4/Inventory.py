from cmath import exp


class Inventory:
    def lock(self, item_type):
        """Select the type of item that is going to be manipulated. this method will lock the item so 
        nobody else can manipulate the inventory until it's returned. This prevents selling the same item
        to two different customers."""
        pass

    def unlock(self, item_type):
        """Release the given type so that other customers can access it."""
        pass

    def purchase(self, item_type):
        """If the item is not locked, raise an exception. If the itemtype does not exists,
        raise an exception. If the item is currently out of stock, raise an exception. If the item
        is a available, subtract one item and return the number of items left."""
        pass

class InvalidItemType(Exception):
    pass

class OutOfStock(Exception):
    pass

item_type = 'widge'

inv = Inventory()
inv.lock(item_type)
try:
    num_left = inv.purchase(item_type)
except InvalidItemType:
    print("Sorry, we don't sell {}".format(item_type))
except OutOfStock:
    print("Sorry, that item is out of stock")
else:
    print("Purchase complete. There are {} {} left".format(num_left, item_type))
finally:
    inv.unlock(item_type)