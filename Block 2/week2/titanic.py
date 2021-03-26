import csv

headings = []
records = []


def load_data(file_path):
    print("Loading data...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        for heading_values in next(csv_reader):
            headings.append(heading_values)
        for record in csv_reader:
            records.append(record)
    print("Done!")

    print(records)


def display_menu():
    print("""
          Please select one of the following options:
          [1] Display the names of all passengers
          [2] Display the number of passengers that survived
          [3] Display the number of passengers per gender
          [4] Display the number of passengers per age group
          [5] Display the number of survivors per age group
          [6] Quit
          """ )
    user_input = int(input("Type your option number here : "))
    return user_input


def display_passenger_names():
    print("The names of the passengers are...")
    for record in records:
        print(record[3])


def display_num_survivors():
    num_survived = 0
    for record in records:
        if record[1] == "1":
            num_survived += 1

    print(f"{num_survived} passengers survived")


def display_passengers_per_gender():
    females = 0
    males = 0
    for record in records:
        gender = record[4]
        if gender == "female":
            females += 1
        else:
            males += 1

    print(f"females: {females}, males: {males}")


def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        age = record[5]
        if age.strip() == "":
            continue
        float_age = float(age)
        if float_age < 18:
            children += 1
        elif float_age < 65:
            adults += 1
        else:
            elderly += 1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")
    return children, adults, elderly


def display_survivors_per_age_group():
    child_survivors = 0
    adult_survivors = 0
    elderly_survivors = 0
    survivors_not_included = 0

    for record in records:
        if record[1] == "1":
            age = record[5]
            if age.strip() == "":
                survivors_not_included += 1
                continue
            float_age = float(age)
            if float_age < 18:
                child_survivors += 1
            elif float_age < 65:
                adult_survivors += 1
            else:
                elderly_survivors += 1

    children, adults, elderly = display_passengers_per_age_group()

    print(f"children: {child_survivors}/{children}, adults: {adult_survivors}/{adults}, elderly: {elderly_survivors}/{elderly}")
    print(f"Number of Survivors not included: {survivors_not_included}")


def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")

    while True:
        selected_option = display_menu()
        print(f"You have selection option: {selected_option}")
        if selected_option == 1:
            display_passenger_names()
        elif selected_option == 2:
            display_num_survivors()
        elif selected_option == 3:
            display_passengers_per_gender()
        elif selected_option == 4:
            display_passengers_per_age_group()
        elif selected_option == 5:
            display_survivors_per_age_group()
        elif selected_option == 6:
            print("Quiting Program...")
            break
        else:
            print("Error! Option not recognised!")

        print("")
        print("Showing Main Menu....")


run()
