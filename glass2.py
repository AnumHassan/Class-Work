class shape():
    def __init__(self,sides,color):
        self.sides=sides
        self.color=color

    def showsides(self):
        print(" The Side are", self.sides) # self.side is saving in other call
    def showcolor(self):
        print(" The color are", self.color) # self.side is saving in other call
traingle = shape(3,"yellow")
traingle.showcolor()
traingle.showsides()
print(traingle.sides)
def return_shape():
    return shape(3,"red")
def set_color(shape,color):
    shape.color=color

