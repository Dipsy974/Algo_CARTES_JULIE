from card import Card

class Creature(Card):

    def __init__(self, name, cost, desc, atk, hp):
        Card.__init__(self, name, cost, desc)
        self.__atk = atk
        self.__hp = hp

    def getHp(self):
        return self.__hp

    def getAtk(self):
        return self.__atk

    def loseHp(self, value):
        self.__hp -= value
        



