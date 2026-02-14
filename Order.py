class Order:
    
    tax_percent = 5

    def __init__(self, order_id, customer_name, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.price = price
        self.placed = False
        self.cancelled = False

    def place_order(self):
        if not self.placed:
            self.placed = True
            print(f"Order {self.order_id} placed successfully")
        else:
            print("already placed")

   
    def cancel_order(self):
        if self.placed and not self.cancelled:
            self.cancelled = True
            print(f"Order {self.order_id} cancelled")
        else:
            print("Order cannot be cancelled")


    def calculate_total_price(self):
        if self.placed and not self.cancelled:
            tax = (self.price * Order.tax_percent) / 100
            total_price = self.price + tax
            print("Total price:", total_price)
            return total_price
        else:
            print("Order not active")
            return 0

    
    @classmethod
    def update_tax_percentage(cls, new_tax):
        cls.tax_percent = new_tax
        print("Tax percentage updated to:", new_tax)
o1 = Order(101, "Uma", 2000)

o1.place_order()
o1.calculate_total_price()

Order.update_tax_percentage(10)
o1.calculate_total_price()

o1.cancel_order()
