# JUNE 02
# Functions, booleans, lists, and dictionaries

def form_letter(recipient, promise):
    print("Dear " + recipient + ",")
    print("Thank you for voting for me.")
    print("I promise to ")
    print(promise)
    print()
    print()

my_voters = {
    "Richard" : "build a park in your backyard",
    "Lula"    : "fix your sidewalk",
    "Ana"     : "call a friend in DC for a pardon",
    "Cesar"   : "add a bus stop in your living room"
}

# for every voter:
#   call the function form letter passing to it the
#   voter's and my most insincere promise to them.

for name, promise in my_voters.items():
    form_letter(name, promise)