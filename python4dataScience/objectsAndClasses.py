# Python has many different kinds of data type each is an object
# Every object has the following: a type, internal representation, a set of functions called
# And methods to interact with the data.

class circule (object):
    def __init__(self,radius, color):
        self.radius = radius;
        self.color = color;


class rectangule(object):
    def __init__(self,color,height,width):
        self.height = height;
        self.width = width;
        self.color = color;


redCircule = circule(10, "red")
print(redCircule.radius)
