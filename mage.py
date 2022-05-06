from crystal import Crystal
from blast import Blast
from creature import Creature


class Mage:

    def __init__(self,name):
        self.__name = name
        self.__hp = 20
        self.__maxMana = 4
        self.__mana = 4
        self.__hand = []
        self.__discardPile = []
        self.__zone = []

    # Getters
    def getName(self):
        return self.__name

    def getHp(self):
        return self.__hp

    def getMaxMana(self):
        return self.__maxMana
    
    def getMana(self):
        return self.__mana
    
    def getHand(self):
        return self.__hand
    
    def getDiscardPile(self):
        return self.__discardPile

    def getZone(self):
        return self.__zone

    # Setters
    def setHand(self,cards):
        for card in cards:
            self.__hand.append(card)
        return self.__hand

    #Mage Methods

    def play(self, card):
        if self.__mana >= card.getCost():
            self.__hand.remove(card)
            self.__zone.append(card)
            self.__mana -= card.getCost()

            #Effets cristaux
            if isinstance(card, Crystal):
                self.__maxMana += card.getValue()

        else:
            print("Pas assez de mana")

    def recupMana(self):
        self.__mana = self.__maxMana
        return self.__mana


    def attack(self, attacker, playerTarget, target):
        target.loseHp(attacker.getAtk())
        #Contre-Attaque si la cible n'est pas morte
        if target.getHp() > 0:
            attacker.loseHp(target.getAtk())
            #Discard l'attaquant si il la contre attaque est fatale
            if attacker.getHp() <= 0:
                self.discard(attacker)
        else:
            playerTarget.discard(target)

    def useBlast(self, card, playerTarget, target):
        card.blastTarget(target)
        if isinstance(target, Creature) and target.getHp() <= 0:
            playerTarget.discard(target)
            self.discard(card)

    def discard(self, card):
        self.__zone.remove(card) 
        self.__discardPile.append(card)    

    def loseHp(self, value):
        self.__hp -= value

     



    

        

    