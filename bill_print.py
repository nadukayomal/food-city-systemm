class Bill:
    def __init__(self, date, product_list, unit_price, quantity):
        self.date = date
        self.product_list = product_list
        self.unit_price = unit_price
        self.quantity = quantity

    def print_bill_head(self):
        print("\t\t Welcome to Food city \t\t")
        print("\n")

# bill_1 = Bill(2020,10,20,33)
# bill_1.print_bill_head()