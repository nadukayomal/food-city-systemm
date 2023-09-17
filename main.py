


print("####----------Welcome to Food city----------####")
print("+-----Enter a number to access the system------+")
print("\n System ; \n Type 1 : Enter shop management system. \n Type 2 : Enter to customer section. \n Type 3 : Quit the program \n")

while True:
    number = input("Enter a number : ")
    if number.isdigit():
        number = int(number)
        if number == 1:
            while True:
                user_name = input("Enter the user name : ") # user name == seller123
                password = input("Enter password : ") # password = sel12345
                if user_name == "seller123" and password == "sel12345" :
                    print("Log in success!")                
                    # run seller section
                    break
                else:
                    print("Invalid username or password")
        elif number == 2:
            print("Hello Customer")
            # enter customer section
        elif number == 3:
            print("Thank you, come again!")
            quit()
        else:
            print("Enter number must between 0-3")
            number = input("Enter a number : ")
    else:
        print("Input must be digits")

