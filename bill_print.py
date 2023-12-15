class Bill:
    def __init__(self, date, products, unit_price, quantity):
        self.date = date
        self.products = products
        self.unit_price = unit_price
        self.quantity = quantity

    def bill_head(self):
        print("\t\t Welcome to Food city \t\t")
        print("\n")
        print("date : {:35s}".format(self.date))

    def bill_footer(self):
        print("Thank you come again")

    def get_total(self):
        product_count = len(self.products)
        sub_total_list = []
        for value in range(product_count):
            sub_total = int(self.unit_price[value]) * int(self.quantity[value])
            sub_total_list.append(sub_total)
        return sum(sub_total_list)
    
    def bill_print(self):
        # self.bill_head()
        product_count = len(self.products)
        print("Name | Quantity | unit price | price")
        for value in range(product_count):
            product = self.products[value]
            quantity = self.quantity[value]
            unit_price = self.unit_price[value]
            sub_total = int(quantity) * int(unit_price)
            print(product, quantity , unit_price, sub_total)
            # print("\n")
        
        total = self.get_total()
        print(total)


# product_list = ["apple", "mango"]
# unit_price = [10,20]
# quantity = [10,10]

# bil_12 = Bill(2020,product_list,unit_price,quantity)
# total = bil_12.bill_print()
# print(total)
    
# bill_1 = Bill(2020,10,20,33)
# bill_1.print_bill_head()