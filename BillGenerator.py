import random
import string

discounts = ("TEN15", "TEN20", "TEN25", "FIVE10", "FIVE08", "FIVE05", "ONE03", "ONE04", "ONE05")
products = {}
products_num = 6
ordered = {}


def generate_prod():
    for i in range(products_num):
        product_name = "Computer-"+''.join(random.choice(string.ascii_uppercase) for i in range(3))
        product_price = random.randint(1, 5000)
        products.setdefault(product_name, product_price)

def print_prod():
    for key in products.keys():
       print("Name: ",key,"  Price: ",products.get(key))

def print_menu():
    print("<<<welcome to our shop>>>\n"+
          "1. print all the products\n"+
          "2. order products\n"+
          "3. generate bills\n"+
          "4. leave"
          )
generate_prod()
while True:

    print_menu()
    inp = input("Dear customer, please make your choice: ")
    if inp == "1":
        print_prod()
    elif inp == "2":
        while True:
            print("1. order new product\n"+
                "2. check order history\n"+
                "3. go back to main menu")
            order_inp = input("Please make your choice: ")
            if order_inp == "1":
                print_prod()
                product = input("Please enter a valid product name you would like to add to your cart: ")
                quantity = int(input("Please enter how many of this product you would like to order: "))
                for prod in products.keys():
                    if prod == product:
                        if product not in ordered.keys():
                            ordered.setdefault(product,quantity)
                        else:
                            for order in ordered.keys():
                                if order == product:
                                    ordered[order]+= quantity

            elif order_inp == "2":
                for o in ordered.keys():
                    print("Product name: ",o," Quantity: ",ordered.get(o))

            elif order_inp == "3":
                break
    elif inp == "3":
        bill_sum = 0
        for ord in ordered.keys():
            for prod in products.keys():
                if ord == prod:
                    bill_sum+= ordered[ord]*products[prod]
        print("\033[1;32;40m Total sum: ",bill_sum,"\033[0m")
        if 5000 > bill_sum > 1000:
            tuple_index = random.randint(6,8)
            print("\033[1;32;40m",discounts[tuple_index],"is applying for your bills \033[0m")
            print("\033[1;32;40m the final bill price will be after discount: ",
                  (100-int(discounts[tuple_index][-1]))/100*bill_sum,"\033[0m")
        if 10000 > bill_sum >5000:
            tuple_index = random.randint(3,5)
            print("\033[1;32;40m",discounts[tuple_index],"is applying for your bills \033[0m")
            if discounts[tuple_index][-2] == "0":
                print("\033[1;32;40m the final bill price will be after discount: ",
                      (100 - int(discounts[tuple_index][-1])) / 100 * bill_sum, "\033[0m")
            else:
                print("\033[1;32;40m the final bill price will be after discount: ",
                      (100 - int(discounts[tuple_index][-2:])) / 100 * bill_sum, "\033[0m")
        if bill_sum > 10000:
            tuple_index = random.randint(0,2)
            print("\033[1;32;40m",discounts[tuple_index],"is applying for your bills \033[0m")
            print("\033[1;32;40m the final bill price will be after discount: ",
                  (100-int(discounts[tuple_index][-2:]))/100*bill_sum,"\033[0m")
    elif inp == "4":
        break




