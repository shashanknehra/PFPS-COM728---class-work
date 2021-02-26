def if_task():
    val = input("What type of book is this?")
    if val.lower() == "adventure":
        print('I like {bookType} books!'.format(bookType='adventure'))


def if_else_task():
    val = input("Please enter the activity to be performed.")
    if val.lower() == "calculate":
        print("Performing calculations...")
    else:
        print('Performing activity...')
    print("Activity completed!")


def if_elif_else_task():
    val = input("Towards which direction should I paint (up, down, left or right)?")
    if val.lower() == "up":
        print("I am painting in the upward direction!")
    elif val.lower() == "down":
        print("I am painting in the downward direction!")
    elif val.lower() == "left":
        print("I am painting in the left direction!")
    elif val.lower() == "right":
        print("I am painting in the right direction!")
    else:
        print('Unknown direction')



def modulo_task():
    val = int(input("Please enter a whole number."))
    if val%2 != 0:
        print('The number {numberIn} is an odd number.'.format(numberIn=val))
    else:
        print('The number {numberIn} is an even number.'.format(numberIn=val))


def comparison_task():
    firstNumber = int(input("Please enter first number :- "))
    secondNumber = int(input("Please enter second number :- "))

    if firstNumber > secondNumber:
        print("The second number is the smallest.")
    elif firstNumber < secondNumber:
        print("The first number is the smallest.")
    elif firstNumber == secondNumber:
        print("Both are equal!")
    else:
        print('Unknown Numbers')


def counter_task():
    first_number = int(input("Please enter first number :- "))
    second_number = int(input("Please enter second number :- "))
    third_number = int(input("Please enter third number :- "))

    numbers = [first_number, second_number, third_number]

    even_counter = 0
    odd_counter = 0

    for number in numbers:
        if number%2 == 0:
            even_counter += 1
        else:
            odd_counter += 1

    print(f'There were {even_counter} even and {odd_counter} odd numbers.')


def nested_loop_task():
    rows = int(input("How many rows should I have? "))
    columns = int(input("How many columns should I have? "))

    for row in range(rows):
        for column in range(columns):
            print(":-)", end="")
        print()
    print("Done!")


def nesting_task():
    seq = input("Please enter a sequence :- ")
    character = input("Please enter the character for the marker :- ")
    is_counter_started = False
    distance_counter = 0
    for char in seq:
        if char.lower() == character.lower():
            if is_counter_started:
                is_counter_started = False
                break
            else:
                is_counter_started = True
        elif char == "-":
            if is_counter_started:
                distance_counter += 1
    print('The distance between the markers is {count}.'.format(count=distance_counter))


nesting_task()
