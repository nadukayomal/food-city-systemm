class Products:
    def __init__(self, product_name, unit_price):
        self.product_name = product_name
        self.unit_price = unit_price

    def auto_update_quantity(self, bought_quantity):
        product_list = []
        product_quantity_list = []

        with open("_product_quantity_list.txt","r") as file_1:
            for line in file_1:
                product,quantity = line.strip().split(" ")
                product_list.append(product)
                product_quantity_list.append(int(quantity))

            if (self.product_name in product_list):
                index = product_list.index(self.product_name)
                if (product_quantity_list[index] >= int(bought_quantity)):
                    product_quantity_list[index] -= int(bought_quantity)
                else:
                    print("This stock lacks the capacity.")
            else:
                print("Out of Stock")
