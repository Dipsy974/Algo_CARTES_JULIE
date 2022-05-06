class Card:

    def __init__(self,name, cost, desc):
        self.__name = name
        self.__cost = cost
        self.__desc = desc

    def getName(self):
        return self.__name

    def getDesc(self):
        return self.__desc

    def getCost(self):
        return self.__cost

        

    