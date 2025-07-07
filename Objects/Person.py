class Person:

    # define state: what are the variables of the object
    # The best way to show an object's variables (aka attributes or fields)
    # is to show how an object is instantiated.
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._ssn = -1 # private please
        self._dob = None

    # define behavior: what are the method the object offers?
    def introduce(self):
        print(f"\nHello, my name is {self.first_name}")

p1 = Person("Lula", "Robertson")
p2 = Person("Ben", "Hansen")

p2.introduce()