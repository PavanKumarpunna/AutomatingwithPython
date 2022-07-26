class dog:

    def __init__(self, name, breed, color, age):
        # state
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    # behavior
    def barkAtStrangers(self):
        print("Bark at strangers")

    def eatMeats(self):
        print("Will eat Meats")

    def wakeAtNight(self):
        print("Will sleep in day time")


d1 = dog("ADog", "Bulldog", "white", 5)
d2 = dog("BDog", "pup", "black", 2)
print(d1.name)
d1.eatMeats()
print(d2.name)
d2.eatMeats()

print(dog("Edog","Ebreed","yellow",2).eatMeats())