
def directions():
    return ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]


def run_activity1():
    print(directions())
# Activity 1 Finished --------------------------------


def movements():
    return ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]


def run_activity2():
    print("Moving.....")
    path = movements()

    for current_index in range(0, len(path), 2):
        print(f"{path[current_index]} for {path[current_index+1]} steps")
# Activity 2 Finished --------------------------------


def menu():
    print("Please select a direction:")
    direction = directions()
    for index in range(len(direction)):
        print(f"{index}: {direction[index]}")


def run_activity3():
    menu()

# Activity 3 Finished --------------------------------


def menu_with_input():
    print("Please select a direction:")
    direction = directions()
    for index in range(len(direction)):
        print(f"{index}: {direction[index]}")

    user_input = int(input())

    if user_input >= len(direction):
        print("Please select a valid direction next time (╬≖_≖)")
        print("Forced to move forward (⩺_⩹)")
        return direction[0]

    return direction[user_input]


def run_activity():
    print("Working out escape route...")
    route = []

    for count in range(5):
        route.append(menu_with_input())

    print(f"Escape route: {route}")


run_activity()
# Activity 4 Finished --------------------------------
