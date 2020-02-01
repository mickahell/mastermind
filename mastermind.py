# MASTERMIND
# Règles : 12 chances, 5 billes, 8 couleurs

import random

# y = yellow ; b = blue ; g = green ; r = red ; w = white ; p = purple ; i = invisible ; o = orange
couleurs = ['y', 'b', 'g', 'r', 'w', 'p', 'i', 'o']
tour = 2

humain = 1
partie = 1

#player = str(input("Qui décode, une machine ou un humain ? machine/humain : "))
#if player == "humain":
#    humain = 1

################## Creation du code
# Random si codeur is machine
code = []
i = 0
while len(code) < 5:
    sample = random.choice(couleurs)
    code.insert(i, sample)
    i += 1

while partie == 1:
    ################ Proposition du joueur / machine
    print("#############################################")
    print("y = yellow ; b = blue ; g = green ; r = red ; w = white ; p = purple ; i = invisible ; o = orange")
    proposition = []
    x = 0
    while len(proposition) < 5:
        sample = str(input("Choisie une couleur : "))
        proposition.insert(x, sample)
        x += 1

    ################## Check result
    if code == proposition:
        print("%s = %s" % (proposition, code))
        print("#################################")
        print("You wiiiiin !")
        partie = 0
    else:
        result = []
        restecode = [] # Méthode de matheux, comme avec une division
        resteprop = [] # Méthode de matheux, comme avec une division
        check = 0
        # Check si bonne couleur & bonne place
        while check < 5:
            if proposition[check] == code[check]:
                result.insert(check, '*')
            else:
                restecode.insert(check, code[check])
                resteprop.insert(check, proposition[check])
            check += 1

        #check si bonne couleur mais mauvaise place
        check = len(restecode) -1
        while check >= 0:
            for eld in resteprop:
                if eld == restecode[check]:
                    result.insert(check, '+')
            check -= 1
        print("#############################################")
        print("Resultat : %s || %s" % (proposition, result))
        tour -= 1
        print("Tours restant : ", tour)
        if tour == 0:
            partie = 0
            print("#############################################")
            print("You lose !!!")
# Graph
