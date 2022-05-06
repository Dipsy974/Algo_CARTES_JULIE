from card import Card

class Crystal(Card):

    def __init__(self, name, cost, desc, value):
        Card.__init__(self, name, cost, desc )
        self.__value = value

    def getValue(self):
        return self.__value

    