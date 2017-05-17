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
        this.plantList = [Tree(-1,-1)]
        this.animalList = []
    def createPlants(this, n, opt = 0):
        tr = 0
        bu = 0
        this.opt = opt
        for i in range(n):
            plantType = random.randrange(0,2,1)
            if (plantType == 1):
                while True:
                    this.xCord = random.randrange(0,this.width,1)
                    this.yCord = random.randrange(0, this.height, 1)
                    this.m = len(this.plantList)
                    this.c = 0
                    for a in this.plantList:
                        if (this.xCord != a.x)&(this.yCord != a.y):
                            this.c += 1
                    if this.m == this.c:
                        break
                this.plantList.append(Tree(this.xCord,this.yCord))
                tr += 1
            else:
                while True:
                    this.xCord = random.randrange(0,this.width,1)
                    this.yCord = random.randrange(0, this.height, 1)
                    this.m = len(this.plantList)
                    this.c = 0
                    for a in this.plantList:
                        if (this.xCord != a.x)&(this.yCord != a.y):
                            this.c += 1
                    if this.m == this.c:
                        break
                this.plantList.append(Bush(this.xCord,this.yCord))
                bu += 1
        if (this.opt == 'showList'):
            for i in this.plantList:
                print("xCord: {0}   Y: {1}   -   {2}".format(i.x,i.y,type(i)))
        print("Added {0} trees and {1} bushes".format(tr,bu))
i = Controller(30,30)
#Необязательный параметр showList - показать список созданных объектов
i.createPlants(75, 'showList')