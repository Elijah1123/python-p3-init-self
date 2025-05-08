

class Dog:
    def __init__(self, name, breed="Mutt"):  # Default breed is set to "Mutt"
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
