import random
class Positional:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.age = 0
        self.size = size
class Plant(Positional):
    def __init__(self, x, y, size):
        super(Plant, self).__init__(x, y, size)
class Bush(Plant):
    def __init__(self, x, y):
        super(Bush, self).__init__(x,y,1.0)
class Tree(Plant):
    def __init__(self,x,y):
        super(Tree, self).__init__(x,y,0.5)
class Animals(Positional):
    def __init__(self,x,y,size):
        super(Animals, self).__init__(x,y,size)
        self.speed = 0
        self.hunger = 10
        self.visionAngle = 0
        self.visionRange = 0
class Wolf(Animals):
    def __init__(self,x,y):
        super(Wolf, self).__init__(x,y,0.3)
        self.visionAngle = 360
        self.visionRange = 30
class Horse(Animals):
    def __init__(self,x,y):
        super(Horse, self).__init__(x,y,0.2)
        self.visionAngle = 120
        self.visionRange = 20
class Controller:
    def __init__(this, width, height):
        this.width = width
        this.height = height
    def createPlants(this, n):                                 #PLUS IS FOR BUSH, MINUS IS FOR EMPTY
        this.m = {}
        this.field = []
        this.finString = ""
        for l in range(this.height):
            this.string = []
            for e in range(this.width):
                this.string.append("-")
            this.field.append(this.string)
        for l in range(n):
            this.m[l] = Bush(random.randrange(0,this.width, 1),random.randrange(0,this.height,1))
            this.field[this.m[l].y][this.m[l].x] = "+"
        for l in this.field:
            for e in l:
                this.finString += e + "  "
            this.finString += "\n"
        print(this.finString)
i = Controller(30,30)
i.createPlants(75)
#githubCoopTestDone
