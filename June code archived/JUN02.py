# JUNE 02
# Functions, booleans, lists, and dictionaries

def form_letter(recipient, promise):
    """Prints a form letter for an aspiring local politician, thanking their voters
    and promising things.

    Inputs
    ------
    recipient : string
      The name of the voter the letter is sent to
    promise : string
      The promise to the voter
    """
    print("Dear " + recipient + ",")
    print("Thank you for voting for me.")
    print("I promise to ")
    print(promise)
    print()

# Simplistic dictionary to demonstrate the concept. Using first names as keys in 
# a dictionary is not a good idea. Keys must be unique and names are not. There 
# are two voters with the same name below, but only one of them will receive a
# form letter -- the most recent one with the same name.

my_voters = {
    # KEY     : VALUE (or values)
    "Richard" : "build a park in your backyard",
    "Lula"    : "fix your sidewalk",
    "Ana"     : "call a friend in DC for a pardon",
    "Cesar"   : "add a bus stop in your living room",
    "Ana"     : "fix the potholes" 
}

# for every voter:
#   call the function form letter passing to it the
#   voter's and my most insincere promise to them.

for name, promise in my_voters.items():
    form_letter(name, promise)

# A better dictionary using objects -- this is advanced stuff and shown here
# as a reference and a goal for the course.

# Create an object for voters. Each voter is defined by personal information (name,
# address, and the promise made to them).
class Voter:
    def __init__(self, first_name, last_name, street_address, promise):
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.promise = promise

# Create a database of voter objects
my_better_voters = {
    "frodo@shire" : Voter("Frodo", "Baggins", "123 Underhill Lane", "destroy the ring"),
    "sam@shire" : Voter("Sam", "Gamgee", "5 Gardeners Rd", "cater your wedding"),
    "gandalf@istari" : Voter("Gandalf", "the Grey", "81 Wizard's Manor", "help you defeat Sauron"),
    "sam@ecthelion" : Voter("Sam", "Fidor", "201 Tower Av", "rebuild the city")
}

# Write a function to produce a form letter using a voter object as an input
def better_form_letter(voter):
    print()
    print(f"{voter.first_name} {voter.last_name}")
    print(f"{voter.street_address}")
    print(f"Gondor, Middle Earth")
    print("")
    print(f"Dear {voter.first_name}")
    print(f"Thank you for voting for me. I promise to\n{voter.promise}")
    print()
    print("Sincerely,")
    print("Lord Voldemort")

# Produce the letters by evaluating the voters dictionary, pulling one 
# voter object at a time and passing it to the form letter function.

for voter in my_better_voters.values():
    better_form_letter(voter)