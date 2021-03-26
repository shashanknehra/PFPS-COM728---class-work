
def gang():
    print("Loading gang...")
    friends = ["Scooby Doo", "Shaggy Rogers", "Fred Jones", "Daphne Blake", "Velma Dinkley"]
    print(friends)
    print("...Done!")
    return friends


def phrases(friends):
    quotes = {}
    for friend in friends:
        print(f"What does {friend} say?")
        quote = input()
        quotes[friend] = quote
    return quotes


def save(quotes):
    with open("quotes.txt", "w") as text_file:
        for key in quotes.keys():
            text_file.write(f"{key}: {quotes[key]}\n")





friends = gang()
quotes = phrases(friends)
save(quotes)
