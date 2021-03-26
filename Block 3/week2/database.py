import sqlite3


def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql_query = "SELECT name, description, quantity " \
                "FROM product " \
                "NATURAL JOIN stock"
    cursor.execute(sql_query)
    all_products = cursor.fetchall()
    print(f"There are {len(all_products)} products in the catalogue.")
    print("The stock level for each product is as follows:")
    print()
    for product in all_products:
        print(f"Product: {product[0]}")
        print(f"Description: {product[1]}")
        print(f"Stock level: {product[2]}")
        print()
    db.close()


def display_product_supplier():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql_query = "SELECT p.name, s.name as 'supplier' " \
                "FROM product p " \
                "INNER JOIN supplier s ON p.supplier_id = s.id"
    cursor.execute(sql_query)
    all_products_supplier = cursor.fetchall()
    print("The suppliers for each product are as follows:")
    print()
    for products_supplier in all_products_supplier:
        print(f"Product: {products_supplier[0]}, Supplier: {products_supplier[1]}")
    db.close()


def display_product_supplier_locations():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql_query = "SELECT p.name, s.name as 'supplier', l.city, l.country " \
                "FROM product p " \
                "INNER JOIN supplier s ON p.supplier_id = s.id " \
                "INNER JOIN location l ON s.location_id = l.id"
    cursor.execute(sql_query)
    all_products_supplier = cursor.fetchall()
    print("The suppliers for each product are as follows:")
    print()
    for products_supplier in all_products_supplier:
        print(f"Product: {products_supplier[0]}, Supplier: {products_supplier[1]}, Supplier Location: {products_supplier[2]},{products_supplier[3]}")
    db.close()


def display_products_missing_suppliers():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql_query = "SELECT p.name, s.name as 'supplier', l.city, l.country " \
                "FROM product p " \
                "LEFT OUTER JOIN supplier s ON p.supplier_id = s.id " \
                "LEFT OUTER JOIN location l ON s.location_id = l.id"
    cursor.execute(sql_query)
    all_products_supplier = cursor.fetchall()
    print("The suppliers for each product are as follows:")
    print()

    for products_supplier in all_products_supplier:

        print(f"Product: {products_supplier[0]}, Supplier: {products_supplier[1]}", end="")
        if products_supplier[1] != None:
            print(f"Supplier Location: {products_supplier[2]},{products_supplier[3]}")

    db.close()


def display_suppliers_missing_products():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql_query = "SELECT  s.name as 'supplier', p.name " \
                "FROM supplier s " \
                "LEFT OUTER JOIN  product p ON p.supplier_id = s.id"
    cursor.execute(sql_query)
    all_products_supplier = cursor.fetchall()
    print("The suppliers for each product are as follows:")
    print()

    for products_supplier in all_products_supplier:

        print(f"Supplier: {products_supplier[0]}, Product: {products_supplier[1]}")

    db.close()