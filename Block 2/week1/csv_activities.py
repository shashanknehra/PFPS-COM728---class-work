import csv

# Activity 1 Start ---------------------
def run_activity_1(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)
        heading_text = next(csv_reader)
        print("Headings:\n{headings}".format(headings=heading_text))
        print("Values:")
        for values in csv_reader:
            print(values)


# run_activity_1("files/bots.csv")

# Activity 1 End ---------------------

# Activity 2 Start ---------------------
def run_activity_2(path):
    print("Extracting...")
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        names = ""

        for values in csv_reader:
            names += f'{values[1]}\n'
        print("Done! The extracted names are as follows:")
        print(names)


# run_activity_2("files/bots.csv")

# Activity 2 End ---------------------


# Activity 3 Start ---------------------
def export(path, bots_to_export):
    print("Exporting...")
    with open(path, "a") as csv_file:
        for i in range(bots_to_export):
            print("Requesting details for Bot {botNum}".format(botNum=i))
            bot_id = int(input("Please enter ID:\n"))
            bot_name = input("Please enter Name:\n")
            bot_paint = input("Please enter Paint:\n")
            csv_file.write("{id},{name},{paint}\n".format(id=bot_id, name=bot_name, paint=bot_paint))
    print("Done!")


export("files/exported_bots.csv", 2)

# Activity 3 End ---------------------