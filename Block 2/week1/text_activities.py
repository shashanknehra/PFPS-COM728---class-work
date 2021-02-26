# imports
import os

# Activity 1 start ------------------------
def cwd():
    path = os.getcwd()
    print("Current Working Directory: {path}".format(path=path))
    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)


def run_activity_1():
    print("Processing...")
    cwd()

# Activity 1 End ------------------------

# Activity 2 start ------------------------
def display_chars(path, number_of_chars):
    with open(path) as text_file:
        read_chars = text_file.read(number_of_chars)
        print(read_chars)


def display_line(path):
    with open(path) as text_file:
        readline = text_file.readline().strip()
        print(readline)


def display_text(path):
    with open(path) as text_file:
        for line in text_file.readlines():
            print(line.strip())


def run_activity_2():
    display_chars("files/library.txt", 5)
    display_line("files/library.txt")
    display_text("files/library.txt")

# Activity 2 End ------------------------

# Activity 3 Start ------------------------
def search(path):
    print("Searching...")
    with open(path) as text_file:
        for line in text_file:
            print("Looked in {location}".format(location=line.strip()))
        print("...Done!")


def run_activity_3():
    search("files/library.txt")


# Activity 4 Start ------------------------
def search_library(path):
    print("Searching...", end="")
    sections = ""
    books = "Books:\n"
    with open(path) as file:
        for line in file:
            if line[:7] == "Section":
                sections += line
            else:
                books += line
    print("Done!")
    #print("\n{sectionsText}\n{booksText}".format(sectionsText=sections, booksText=books))

    return "{sectionsText}\n{booksText}".format(sectionsText=sections, booksText=books)


def save(path,data):
    print("Saving...", end="")
    with open(path,"w") as file:
        file.write(data)

    print("Done!")


def run_activity_4():
    data = search_library("files/books.txt")
    save("files/section-books.txt", data)

# Activity 4 End ------------------------