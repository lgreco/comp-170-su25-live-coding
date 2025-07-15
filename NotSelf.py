class Person:

    def __init__(ego, first_name):
        ego.first_name = first_name
        ego.last_name = None
        ego.dob = None
    
    def __str__(obj):
        return f"[{obj.first_name}]"


if __name__ == "__main__":
    test = Person("Tom")
    print(test)