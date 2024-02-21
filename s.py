class Order:
    # order details
        def __init__(self, customer_info, items, shipping_address):
            self.customer_info = customer_info
            self.items = items
            self.shipping_address = shipping_address

        def addItem(self, item):
            self.items.append(item)
        
        def removeItem(self, item):
            self.items.remove(item)

class OrderCalculation:
    @staticmethod
    def calcTotal(order, tax_rate, discount) -> float:
        subTot = sum(item['price'] * item['quantity'] for item in order.items)
        tax = subTot * tax_rate
        total = subTot + tax - discount # assuming dicount is in $ and not %
        return total

class OrderValid(Order):
    @staticmethod
    def validateOrder(order, item_available, customer_address) -> bool:
        if( len(order.items) <= item_available and customer_address == order.shipping_address):
            return True
        else:
            print("Could not validate order")
            return false

class OrderConfirmation(OrderValid):
    def printEmail(order):
        if(OrderValid.validateOrder(order, order.item_available, order.shipping_address)) == True:
            print("Your order has been confirmed!")

class Inventory(Order):
    @staticmethod
    def removeItem(order, item_available):
        if(order.validateOrder == True):
            item_available -= order
        else:
            print("Error updating inventory")

    def addItem(num):
        item_available =+ num



        