import random

def getX(str):
    return(float(str[:4]))
def getY(str):
    return(float(str[-4:]))

class Positional:
    def __init__(self,cords,size):
        self.cords = cords
        self.age = 0
        self.size = size
class Plant(Positional):
    def __init__(self, cords, size):
        super(Plant, self).__init__(cords, size)
class Bush(Plant):
    def __init__(self, cords):
        super(Bush, self).__init__(cords,1.0)
class Tree(Plant):
    def __init__(self,cords):
        super(Tree, self).__init__(cords,0.5)
class Animals(Positional):
    def __init__(self,cords,size):
        super(Animals, self).__init__(cords,size)
        self.speed = 0
        self.hunger = 10
        self.visionAngle = 0
        self.visionRange = 0
class Wolf(Animals):
    def __init__(self,cords):
        super(Wolf, self).__init__(cords,0.3)
        self.visionAngle = 360
        self.visionRange = 30
class Horse(Animals):
    def __init__(self,cords):
        super(Horse, self).__init__(cords,0.2)
        self.visionAngle = 120
        self.visionRange = 20
class Controller:
    def __init__(this, width, height):
        this.width = width
        this.height = height
        this.plantList = [Tree('5000//5000')]
        this.animalList = []
    def createPlants(this, n, opt = '0'):
        tr = 0
        bu = 0
        this.opt = opt
        for i in range(n):
            this.spawnMatch = True
            plantType = random.randrange(0,2,1)
            if plantType == 1:
                this.size = 0.5
                while this.spawnMatch == True:
                    this.xCord = round(random.uniform(0,this.width),1)
                    this.yCord = round(random.uniform(0, this.height),1)
                    this.ctrlString = '{0}'.format(this.xCord).zfill(4) + '//' + '{0}'.format(this.yCord).zfill(4)
                    this.m = len(this.plantList)
                    this.c = 0
                    for a in this.plantList:
                        if (abs(getX(this.ctrlString) - getX(a.cords)) >= (this.size + a.size))|(abs(getY(this.ctrlString) - getY(a.cords)) >= (this.size + a.size)):
                            this.c += 1
                    if this.m == this.c:
                        this.spawnMatch = False
                this.plantList.append(Tree(this.ctrlString))
                tr += 1
            else:
                this.size = 0.5
                while this.spawnMatch == True:
                    this.xCord = round(random.uniform(0,this.width),1)
                    this.yCord = round(random.uniform(0, this.height),1)
                    this.ctrlString = '{0}'.format(this.xCord).zfill(4) + '//' + '{0}'.format(this.yCord).zfill(4)
                    this.m = len(this.plantList)
                    this.c = 0
                    for a in this.plantList:
                        if (abs(getX(this.ctrlString) - getX(a.cords)) >= (this.size + a.size))|(abs(getY(this.ctrlString) - getY(a.cords)) >= (this.size + a.size)):
                            this.c += 1
                    if this.m == this.c:
                        this.spawnMatch = False
                this.plantList.append(Bush(this.ctrlString))
                bu += 1
        this.plantList.__delitem__(0)
        if (this.opt == 'showList'):
            for i in this.plantList:
                print("X: {0}   Y: {1}   -   {2}".format(i.cords[:4],i.cords[-4:],i.__class__.__name__))
        print("Added {0} trees and {1} bushes".format(tr,bu))
i = Controller(45,45)
#Необязательный параметр showList - показать список созданных объектов
i.createPlants(50, 'showList')
