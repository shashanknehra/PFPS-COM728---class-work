import sqlite3


def retrieve_bot(id):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    param = (id)
    cursor.execute(f"SELECT * FROM bots where id = {id}")
    bot = cursor.fetchone()
    print(bot)
    db.close()


def retrieve_bots():
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql_query = "SELECT * FROM bots"
    cursor.execute(sql_query)
    all_bots = cursor.fetchall()
    print("All bots in the system:")
    for bot in all_bots:
        print(bot)
    db.close()


def get_bot_from_user():
    name = input("Please Enter name of your bot: ")
    max_speed = int(input("Please enter max speed of your bot: "))
    max_strength = int(input("Please enter max strength of your bot: "))
    date = input("Please enter the date of manufacture:  ")
    manufacture_id = int(input("Please enter manufacture ID:  "))
    return [name, max_speed, max_strength, date, manufacture_id]


def insert_bot_in_db():
    bot_data = get_bot_from_user()
    print(bot_data)

    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    params = (bot_data[0], bot_data[1], bot_data[2], bot_data[3], bot_data[4])
    sql = "INSERT INTO bots(name, max_speed, max_strength, created_on, manufacturer_id) VALUES(?,?,?,?,?)"
    cursor.execute(sql, params)
    db.commit()
    print("The record has been added to the database.")
    print(f"The record id is {cursor.lastrowid}")
    db.close()


def update_bot_in_db():
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = "UPDATE bots SET max_speed=50"
    cursor.execute(sql)

    db.commit()

    db.close()


retrieve_bot(6)