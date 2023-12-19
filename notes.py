# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    # functions ha star with __ are not intended to be called.
    def __init__(self, n = "", fc = "", a = 0, ff = ""):
        """ creates an insance of he dog class and sets he atrributes"""
        self.name = n
        self.furColor = fc
        self.age = a
        self.favoriteFood = ff
        self.fetchCount = 0

    def __str__(self) -> str:
            '''returns a string representation of a dog'''
            s = "Dogs name is " + self.name + "\n"
            s += "and age is " + str(self.age) + "\n"
            s += "and fur color is " + self.furColor + "\n"
            s += "they have played fetch " + str(self.fetchCount) + "\n"
            
    def __playfetch__(self, numTimes):
        self.fetchCount += numTimes

myDog = Dog("Logan", "Black", 7, "Salmon")
chrisDog = Dog("Luna", "black & white", 6, "they have played fetch 12 times")

print(myDog)
print(chrisDog)

myDog.__playfetch__
chrisDog.__playfetch__