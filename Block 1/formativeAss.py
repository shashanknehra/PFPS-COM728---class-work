

def commence():
    # commence() function init
    print("The Avengers Initiative")
    # prompt user to enter days
    print("Please enter the number of days:")
    # read user input and validate in case its not int
    while True:
        try:
            days_input = int(input())
        except ValueError:
            print("Please Enter valid number of days.")
            continue
        else:
            break
    # print days input
    print("The Avengers Initiative will commence in {days} days.".format(days=days_input))


def lead(leader):
    # check if leader parameter is "tony stark" and print msg accordingly
    if leader.lower() == "tony stark":
        print("The Avengers are ready!")
    else:
        print("We need a better leader.")


def assemble(num_avengers):
    # commence() function init
    print("Assembling Avengers...")
    # for loop to print "...Avenger has assembled." num_avengers times
    for i in range(num_avengers):
        print("...Avenger has assembled.")

commence()
print("----------------")
print()
lead("Hulk") # Should display "We need a better leader."
lead("Tony Stark") # Should display "The Avengers are ready!"
print("----------------")
print()
assemble(5)

