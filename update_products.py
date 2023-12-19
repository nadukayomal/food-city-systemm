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

        with open("_product_quantity_list.txt","w") as file_2:
            for i in range(len(product_list)-1):
                file_2.write(product_list[i] + " " + str(product_quantity_list[i]) + "\n")
            else:
                file_2.write(product_list[-1] + " " + str(product_quantity_list[-1]))    

    def manual_update_quantity(self, add_quantity):
        product_list = []
        quantity_list = []
        price_list = []

        with open("_product_quantity_list.txt") as file_3:
            for line in file_3:
                products, quantity = line.strip().split(" ")
                product_list.append(products)
                quantity_list.append(int(quantity))

        if (self.product_name in product_list):
            index = product_list.index(self.product_name)
            quantity_list[index] =+ add_quantity
        else:
            with open("_product_price.txt","r") as file_4:
                for line in file_4:
                    product,price = line.strip().split(" ")  
                    price_list.append(price)
          
        if (self.product_name in product_list):
            with open("_product_quantity_list.txt",) as file_5:
                for i in range(len(product_list)-1):
                    file_5.write(product_list[i] + " " + str(quantity_list[i]) + "\n")
                else:
                    file_5.write(product_list[-1] + " " + str(quantity_list[-1]) + "\n")
        else:
            with open("_product_price.txt","w") as file_6:
                for i in range(len(product_list)):
                    file_6.write(product_list[i] + " " + str(price_list[i]) + "\n")
                else:
                    file_6.write(self.product_name + " " + str(self.unit_price))
            with open("_product_quantity_list" , "w") as file_7:
                for i in range(len(product_list)):
                    file_7.write(product_list[i] + " " + str(quantity_list[i]) + "\n")
                else:
                    file_7.write(self.product_name + " " + str(add_quantity))