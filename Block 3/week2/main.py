import database

def menu():
    print("Please select one of the following options:")
    print("[1] Display stock levels")
    print("[2] Display suppliers")
    print("[3] Display supplier locations")
    print("[4] Display missing suppliers")
    print("[5] Display missing products")
    print()
    userSelection = int(input("Your selection: "))
    if userSelection == 1:
        database.display_products_with_stock_levels()
    elif userSelection == 2:
        database.display_product_supplier()
    elif userSelection == 3:
        database.display_product_supplier_locations()
    elif userSelection == 4:
        database.display_products_missing_suppliers()
    elif userSelection == 5:
        database.display_suppliers_missing_products()
menu()
