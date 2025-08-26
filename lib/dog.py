

class Dog:
    def __init__(self, name, breed="Mutt"):  # Default breed is set to "Mutt"
        self.name = name
        self.breed = breed
    # print(f"The {name} is a  {breed} Dog")
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")


Tom = Dog("Tom")
Tom.name()

# German Shepherd = Dog("German Shepherd")
# German Shepherd.breed()