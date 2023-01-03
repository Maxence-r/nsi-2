
# Algorithme Librairie



def monnaie_a_rendre(argent):
    '''
    Fonction qui donne la monnaie à rendre en fonction d'un montant donné.
    A l'aide d'une liste qui contient les différentes monnaie qu'on puisse rendre,
    on parcours cette liste et on regarde si la valeur séléctionnée peut être déduite
    de la somme donnée en argument. Si la valeur séléctionnée peut être déduite, on sort de la boucle 
    et on recommence à parcourir la liste des différentes monnaie qu'on peut potentiellement rendre.
    On effectue cela jusqu'à ce que la somme mise en argument sois égale à 0.


    Entrée ------> une somme dont on veut connaître la somme a rendre

    Sortie ------> la somme à rendre
    '''
    monnaies = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    rendu = []
    while argent > 0:
        for monnaie in monnaies:
            if monnaie <= argent:
                argent -= monnaie
                rendu.append(monnaie)
                break
    return rendu
'''
joueur = int(input("Combien d'argent à rendre ? :"))
for i in monnaie_a_rendre(joueur):
    print(f'il faut rendre {i} euro')

'''


# Algorithme du prêt-à-porter

def monnaie_limite(argent):
    monnaies_limite = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 2: 5}
    rendu_limite = []
    while argent > 0:
        for k in monnaies_limite:
            if k <= argent:
                if monnaies_limite.get(k) > 0:
                    monnaies_limite[k] = monnaies_limite.get(k) - 1
                    argent -= k
                    print(f'donner un billet de {k}')
                    break
        total = sum(monnaies_limite.values())
        if total == 0 and argent > 0:
            print('Plus de monnaie, plus aucune monnaie à rendre, vraiment plus de monnaie, désolé ! Revenez plus jamais !')
            break
    
'''       
monnaie_limite(497)
'''






# Algorithme de la baguette magique

'''
1 GALLION = 17 MORNILLES
1 MORNILLE = 29 NOISES
1 GALLION = 493 NOISES
'''


def gallion(mornille):
    monnaie_gallion = 17
    if mornille % monnaie_gallion == 0:
        return int(mornille/monnaie_gallion)
    else:
        reste_mornille = mornille % monnaie_gallion
        return reste_mornille, int(mornille/monnaie_gallion)

def mornille(noise):
    monnaie_mornille = 29
    if noise % monnaie_mornille == 0:
        return int(noise / monnaie_mornille)
    else:
        reste_noise = noise % monnaie_mornille
        return reste_noise, int(noise/monnaie_mornille)



'''
nb_noises = int(input("Nombre de noises : "))
nb_mornilles = int(input("Nombre de mornilles : "))
nb_gallion = int(input("Nombre de gallion : "))


def monnaie_sorcier(noi, mor, gal):
    return


print(f'il faut rendre {gallion(nb_mornilles)[1] + nb_gallion} gallions, rendre {gallion(nb_mornilles)[0] + mornille(nb_noises)[1]} mornilles, et rendre {mornille(nb_noises)[0]} noises')
'''