from update_products import Products
from bill_print import Bill
import datetime

class SellerSection:
    def __init__(self):
        pass

    def run(self):
        print("Welcome to Seller Section\n")

        while True:
            print("Enter a number to access the system :\n")
            print("Seller Task :\n 1: Type 1 create a bill \n 2: Type 2 add new item \n 3: Type 3 update quantity \n 4: Type 4 goto back\n")
            number = input("Enter a number : ")
            if number.isdigit():
                number = int(number)
                if (number == 1):
                    print("Create new bill")
                elif (number == 2):
                    print("Add new Item")
                elif (number == 3):
                    print("Update Quantity")
                elif (number == 4):
                    break
                else:
                    print("Invalid input")
            else:
                print("Input must be digit")

    def get_all_products(self):
        print("Available Products and Unit Price")
        product_price_list = []
        
        with open("_product_price.txt") as file:
            for line in file:
                product_price = line.strip()
                product_price_list.append(product_price)
            return product_price_list
    
    def display_total(self, product_names, ordered_quantity, products):
        product_list = product_names
        unit_price_list = []
        item = 0

        for product in product_list:
            for one_product in products:
                if (product in one_product):
                    unit_p = int(one_product.split(" ")[1])
                    unit_price_list.append(unit_p)
                    product_remove = Products(product, unit_p)
                    product_remove.auto_update_quantity(ordered_quantity[item])
            item += 1

        today = str(datetime.datetime.now())
        bill = Bill(today, product_list, unit_price_list, ordered_quantity)
        print (bill.get_total())

        while True:
            try:
                paid_amount = int(input("Enter paid amount : LKR "))
                break
            except ValueError:
                print("Please enter digit")

        bill.bill_print(paid_amount)
        print("\n")

    def create_bill(self, ordered_list, products):
        product_names = []
        ordered_quantity = []
        total = 0

        for value in ordered_list:
            if (value == '#'):
                break
            item_info = value.split(" ")
            product_names.append(item_info[0])
            ordered_quantity.append(item_info[1])     

        if (len(product_names) == 0):
            return "No item selected"
        
        self.display_total(product_names, ordered_quantity, products)

    def task_1(self):
        products = self.get_all_products()
        print("\n Create new bill")
        print("Enter : Product name and Order quantity")
        ordered_list = []
        get_total = ""
        i = 1

        while (get_total != "#"):
            print("ADD ITEM PRESS \'1\' AND GET TOTAL PRESS \'#\'")
            get_total = input("PRESS : ")
            if (get_total == "1"):
                item = input("Item" + str(i) + " : ")
                quantity = input("Quantity : ")
                ordered_list.append(item + " " + quantity)
                print("Add Success")
            else:
                ordered_list.append(get_total)
            i += 1
        self.create_bill(ordered_list, products)

    def add_new_item(self, product_name, unit_price, stock):
        product = Products(product_name, unit_price)
        product.manual_update_quantity(stock)
        print("New item added")
        print("\n")

    def task_2(self):
        print("Add new item")

        while True:
            product_name = input("Enter product name : ")
            unit_price = input("Enter unit price : LKR ")
            stock = input("Enter uantity : ")
            if ((product_name.isalpha()) and (unit_price.isdigit()) and (stock.isdigit())):
                product_name = product_name
                unit_price = int(unit_price)
                stock = int(stock)
                break
            else:
                print("Invalid input product name or unit price or quantity")

        self.add_new_item(product_name, unit_price, stock)

    def update_add_stock(self, product_name, unit_price, stock):
        product = Products(product_name, unit_price)
        product.manual_update_quantity(stock)
        print("Stock updated")
        print("\n")

    def update_remove_stock(self, product_name, unit_price, stock):
        product = Products(product_name, unit_price)        
        product.auto_update_quantity(stock)
        print("Stock updated")
        print("\n")

    def task_3(self):
        print("Update Stock")

        while True:
            product_name = input("Enter Product name : ")
            unit_price = input("Enter unit price : LKR ")
            stock = input("Enter quantity : ")
            if ((product_name.isalpha()) and (unit_price.isdigit()) and (stock.isdigit())):
                product_name = product_name
                unit_price = int(unit_price)
                stock = int(stock)
                break
            else:
                print("Invalid input product name or unit price or quantity")

        self.update_add_stock(product_name, unit_price, stock)