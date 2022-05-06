from card import Card

class Blast(Card):

    def __init__(self, name, cost, desc, value):
        Card.__init__(self, name, cost, desc)
        self.__value = value

    def getValue(self):
        return self.__value

    def blastTarget(self, target):
        target.loseHp(self.__value)
        



