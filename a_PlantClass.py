
class Plant: #superclass with color as it's only attribute
    def __init__(self,color):
        self.__color = color

    def get_color(self):
        return self.__color


class Flower(Plant): #flower is subclass
    def __init__(self,color, petals):
        Plant.__init__(self,color) #have to initialize superclass first

        self.__petals = petals

    def get_petals(self): #after superclass is initilized then subclass can go
        return self.__petals
