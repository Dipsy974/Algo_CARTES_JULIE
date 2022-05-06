from card import Card
from crystal import Crystal
from creature import Creature
from blast import Blast
from mage import Mage

gameOver = False
turn = 0

player1 = Mage("Mathieu")
player2 = Mage("Julie")

currentPlayer = player1
currentOpponent = player2

carte1 = Creature("Slime", 1, "Méchant slime", 2, 3)
carte2 = Card("Clairvoyance", 3, "Révèle 2 cartes de la main de l'adversaire")
carte3 = Crystal("Emeraude", 0, "Jolie", 2)
carte4 = Creature("Slime plus fort", 2, "Méchant slime plus fort", 4, 5)
carte5 = Blast("Boum", 2, "Attaque créature ou joueur", 3)

player1.setHand([carte1, carte2, carte3, carte4, carte5])
player2.setHand([carte1, carte2, carte3, carte4, carte5])




# BOUCLE DE JEU PAS TERMINEE (beaucoup de cas à prendre en compte). Scenario complet en bas

while not gameOver:
    if turn%2 == 0:
        currentPlayer = player1
        currentOpponent = player2
    else:
        currentPlayer = player2
        currentOpponent = player1

    print("A toi de jouer, ", currentPlayer.getName(), " ! ")
    print("Mana : " ,currentPlayer.getMana(), " / ", currentPlayer.getMaxMana())
    print("Main :", end=" ")
    for card in currentPlayer.getHand():
        print(card.getName(), "(", card.getCost() ,")", end =" ")
    print()
    print()

    print("Zone de jeu :", end=" ")
    for card in currentPlayer.getZone():
        print(card.getName(), end=" ")
    print()
    print()

    print("Défausse :", end=" ")
    for card in currentPlayer.getDiscardPile():
        print(card.getName(), end=" ")
    print()

    choixAction = int(input("Voulez-vous jouer une carte ou attaquer ? (0-1)"))

    if choixAction == 0:
        index = int(input("Quelle carte voulez vous jouer ? (0-1-...)"))
        currentPlayer.play(currentPlayer.getHand()[index])
    
    turn = turn + 1






# SCENARIO AVEC TOUTES LES FONCTIONNALITES


# print("Main du joueur 1 :", end=" ")
# for card in player1.getHand():
#     print(card.getName(), "(", card.getCost() ,")", end =" ")
# print()

# print("Zone de jeu :", end=" ")
# for card in player1.getZone():
#     print(card.getName(), end=" ")
# print()

# print("Défausse :", end=" ")
# for card in player1.getDiscardPile():
#     print(card.getName(), end=" ")
# print()

# print("Mana : " ,player1.getMana(), " / ", player1.getMaxMana())


# #Joueur 1 pose  sa carte "Slime plus fort" et son émeraude qui augmente son mana max
# player1.play(carte4)
# player1.play(carte3)
# #Joueur 2 pose sa carte "Slime" et attaque le slime de joueur 1 mais ce dernier contre attaque donc le Slime de joueur 2 meurt et se retrouve dans la défausse
# player2.play(carte1)
# player2.attack(carte1,player1,carte4)


# print("Main du joueur 1 :", end=" ")
# for card in player1.getHand():
#     print(card.getName(), "(", card.getCost() ,")", end =" ")
# print()

# print("Zone de jeu :", end=" ")
# for card in player1.getZone():
#     print(card.getName(), end=" ")
# print()

# print("Défausse :", end=" ")
# for card in player1.getDiscardPile():
#     print(card.getName(), end=" ")
# print()

# print("Mana : " ,player1.getMana(), " / ", player1.getMaxMana())


# print("Main du joueur 2 :", end=" ")
# for card in player2.getHand():
#     print(card.getName(), "(", card.getCost() ,")", end =" ")
# print()

# print("Zone de jeu :", end=" ")
# for card in player2.getZone():
#     print(card.getName(), end=" ")
# print()

# print("Défausse :", end=" ")
# for card in player2.getDiscardPile():
#     print(card.getName(), end=" ")
# print()

# print("Mana : " ,player2.getMana(), " / ", player2.getMaxMana())

# #Joueur 2 utilise son blast sur le slime de joueur 1 
# player2.play(carte5)
# player2.useBlast(carte5, player1, player1.getZone()[0])

# #Joueur 1 utilise son blast sur joueur 2 
# player1.play(carte5)
# player2.useBlast(carte5, player2, player2)

# print("Main du joueur 1 :", end=" ")
# for card in player1.getHand():
#     print(card.getName(), "(", card.getCost() ,")", end =" ")
# print()

# print("Zone de jeu :", end=" ")
# for card in player1.getZone():
#     print(card.getName(), end=" ")
# print()

# print("Défausse :", end=" ")
# for card in player1.getDiscardPile():
#     print(card.getName(), end=" ")
# print()

# print("Mana : " ,player1.getMana(), " / ", player1.getMaxMana())

# print()

# print("Main du joueur 2 :", end=" ")
# for card in player2.getHand():
#     print(card.getName(), "(", card.getCost() ,")", end =" ")
# print()

# print("Zone de jeu :", end=" ")
# for card in player2.getZone():
#     print(card.getName(), end=" ")
# print()

# print("Défausse :", end=" ")
# for card in player2.getDiscardPile():
#     print(card.getName(), end=" ")
# print()

# print("Hp : " ,player2.getHp(), " / 20 ")




