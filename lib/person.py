

class Person:
    def __init__(self, name):  # Accepts a name argument
        self.name = name
        print(f"{name} is born!")

    def talk(self):
        print("Good Morning {name}?")

    def walk(self):
        print("The person is walking.")


Mzalendo = Person("Mzalendo")
Zakayo = Person("Zakayo")
Pabro = Person("Pabro")
Lyn = Person("Lyn")
Davi = Person("Davi")
