class Order:
    # order details
        def __init__(self, customer_info, items, shipping_address, item_available):
            self.customer_info = customer_info
            self.items = items
            self.shipping_address = shipping_address
            self.item_available = item_available

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
            return False

class OrderConfirmation(OrderValid):
    def printEmail(order, item_available):
        if(OrderValid.validateOrder(order, order.item_available, order.shipping_address)) == True:
            print("Your order has been confirmed!")

class Inventory(Order):
    @staticmethod
    def removeItem(order, item_available):
        if(OrderValid.validateOrder(order, order.item_available, order.shipping_address) == True):
            order.item_available -= len(order.items)
            print("Inventory updated")
        else:
            print("Error updating inventory")

    def addItem(num):
        item_available =+ num
        return item_available


def main():

    order_items = [{'name': 'dummy1', 'price': 20, 'quantity': 2}, {'name': 'dummy2', 'price': 50, 'quantity': 1}]
    customer_info = {'name': 'Neil Harris', 'email': 'neil@example.com'}
    shipping_address = "321 Main St"
    item_available = 10
    order = Order(customer_info, order_items, shipping_address, item_available)
    # Calculate total
    total = OrderCalculation.calcTotal(order, 0.08, 5)
    # Validate order
    is_valid = OrderValid.validateOrder(order, 10, shipping_address)
    # Confirm order
    OrderConfirmation.printEmail(order, item_available)
    # Update inventory
    Inventory.removeItem(order, 10)
    Inventory.addItem(20)

if __name__ == "__main__":
    main()        
