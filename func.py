def message(obj,size,cat,d_name):
    if size == "Reg":
        s = "Regular"
    elif size == "Med":
        s = "Medium"
    else:
        s = "Large"
    return "You have selected "+cat+" "+d_name+" "+s+" with {0} worth price Rs.{1}".format(obj.getIngredients(),obj.getPrice(size))

def d_tomchi(size):
    obj = Tomchi()
    cat = "Classic"
    d_name = "Tomchi"
    return message(obj,size,cat,d_name)

def d_caponito(size):
    obj = Caponito()
    cat = "Classic"
    d_name = "Caponito"
    return message(obj,size,cat,d_name)

def d_red_indian(size):
    obj = Red_Indian()
    cat = "Premium"
    d_name = "Red Indian"
    return message(obj,size,cat,d_name)

def d_party_lovers(size):
    obj = Party_Lovers()
    cat = "Premium"
    d_name = "Party Lovers"
    return message(obj,size,cat,d_name)

def d_american_heat(size):
    obj = American_Heat()
    cat = "Supreme"
    d_name = "American Heat"
    return message(obj,size,cat,d_name)

def d_re_union(size):
    obj = Re_Union()
    cat = "Supreme"
    d_name = "Re-Union"
    return message(obj,size,cat,d_name)

def cat_classic():
    print("""
1. Tomchi
2. Caponito
3. Quit
""")
    obj = Classic()
    dish = int(input("Choose a dish: "))
    os.system("cls")
    print("------------------Welcome to Pizza Shop-----------------")
    print()
    if dish == 3:
        exit()
    elif dish != 1 and dish != 2:
        print("Invalid Choice. Please select a dish from given options.")
        return cat_classic()
    else:
        size = chooseSize(obj)
        if dish == 1:
            return d_tomchi(size)
        else:
            return d_caponito(size)

def cat_premium():
    print("""
1. Red Indian
2. Party Lovers
3. Quit
""")
    obj = Premium()
    dish = int(input("Choose a dish: "))
    os.system("cls")
    print("------------------Welcome to Pizza Shop-----------------")
    print()
    if dish == 3:
        exit()
    elif dish != 1 and dish != 2:
        print("Invalid Choice. Please select a dish from given options.")
        return cat_premium()
    else:
        size = chooseSize(obj)
        if dish == 1:
            return d_red_indian(size)
        else:
            return d_party_lovers(size)

def cat_supreme():
    print("""
1. American Heat
2. Re-Union
3. Quit
""")
    obj = Supreme()
    dish = int(input("Choose a dish: "))
    os.system("cls")
    print("------------------Welcome to Pizza Shop-----------------")
    print()
    if dish == 3:
        exit()
    elif dish != 1 and dish != 2:
        print("Invalid Choice. Please select a dish from given options.")
        return cat_supreme()
    else:
        size = chooseSize(obj)
        if dish == 1:
            return d_american_heat(size)
        else:
            return d_re_union(size)

def final_step(ret):
    print(ret)
    print("""
    1. Order
    2. Cancel
    3. Quit
    """)
    ch = int(input("Confirm Your Order: "))
    if ch == 3:
        exit()
    elif ch == 1:
        return "Order Confirmed Successfully."
    elif ch == 2:
        return "Order Cancelled !!"
    else:
        print("Invalid Choice. Please select a dish from given options.")
        return final_step(ret)

def chooseSize(obj):
    print("""
       Size      Price
    -------------------
    1. Reg   -   {0}
    2. Med   -   {1}
    3. Large -   {2}
    4. Quit
    """.format(obj.Reg,obj.Med,obj.Large))
    
    size = int(input("Select a size: "))
    os.system("cls")
    print("------------------Welcome to Pizza Shop-----------------")
    print()
    if size == 1:
        return "Reg"
    elif size == 2:
        return "Med"
    elif size == 3:
        return "Large"
    elif size == 4:
        exit()
    else:
        print("Invalid Choice. Please select a size from given options.")
        return chooseSize(obj)


def cuis_regular():
    print("""
1. Classic
2. Premium
3. Supreme
4. Quit
""")
    cat = int(input("Choose a Category : "))
    os.system("cls")
    print("------------------Welcome to Pizza Shop-----------------")
    print()
    if cat == 1:
        return cat_classic()
    elif cat == 2:
        return cat_premium()
    elif cat == 3:
        return cat_supreme()
    elif cat == 4:
        exit()
    else:
        print("Invalid Choice. Please select a size from given options.")
        return cuis_regular()

def main():
    print("------------------Welcome to Pizza Shop-----------------")
    print("""
    1. Regular
    2. Jain
    3. Non-Veg
    4. Quit
    """)
    ch = int(input("Choose a Cuisine : "))
    os.system("cls")
    print("------------------Welcome to Pizza Shop-----------------")
    print()
    if ch == 1:
        return cuis_regular()
    elif ch == 2:
        print("jain not available")
        return main()
    elif ch == 3:
        print('non -veg not available')
        return main()
    elif ch == 4:
        exit()
    else:
        print('Invalid input. Choose from given options.')
        return main()

    print(final_step(ret))


