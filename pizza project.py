choose_pizza = input("enter the pizza name what you want?,supreme is pizza (1),paneer for (2),onion for (3)")
size = input("enter the size of the pizza,l = large,m = medium,s = small")
bill = 0
if choose_pizza == "1":
    print("you choose supreme pizza")
    if size == "l" or size == "L":
        bill += 500
        print("you choose large supreme pizza")
    elif size == "m" or size == "M":
        bill += 250
        print ("you choose medium supreme pizza")
    elif size == "s" or size == "S":
         bill += 150
         print("you choose small supreme pizza")

elif choose_pizza == "2":
    print("you choose paneer pizza")
    if size == "l" or size == "L":
        bill += 700
        print("you choose large paneer pizza")
    elif size == "m" or size == "M":
        bill += 500
        print("you choose medium paneer pizza")
    elif size == "s" or size == "S":
        bill += 250
        print("you choose small paneer pizza")

elif choose_pizza == "3":
    print("you choose onion pizza")
    if size == "l" or size == "L":
        bill += 400
        print("you choose large onion pizza")
    elif size == "m" or size == "M":
        bill += 200
        print("you choose medium onion pizza")
    elif size == "s" or size == "S":
        bill += 150
        print("you choose small onion pizza")

elif choose_pizza == "4":
    print("you choose cheese pizza")
    if size == "l" or size == "L":
        bill += 1000
        print("you choose large cheese pizza")
    elif size == "m" or size == "M":
        bill += 300
        print("you choose medium cheese pizza")
    elif size == "s" or size == "S":
        bill += 250
        print("you choose small cheese pizza")
        print(f" your bill is {bill}")


