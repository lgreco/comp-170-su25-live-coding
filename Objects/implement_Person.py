from Person import Person

persons = list()

a_hobit = (Person("Frodo", "Baggins"))
another_hobbit = (Person("Bilbo", "Baggins"))
bad_wizard = (Person("Saruman", "the White"))
good_wizard = (Person("Gandal", "the Gray"))

a_hobit.set_dob(1900, 1, 1)
another_hobbit.set_dob(1800, 1, 1)
bad_wizard.set_dob(1200, 1, 1)
good_wizard.set_dob(1200, 2, 2)

if good_wizard == bad_wizard:
    print(f"{good_wizard.get_name()} is same age as {bad_wizard.get_name()}")