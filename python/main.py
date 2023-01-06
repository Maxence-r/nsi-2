#coding: utf-8
'''
Auteur : Loris, Maxence, Sarah
Date : 06/01/2022
Version : 1.0
Description : Programme de rendu de monnaie
'''
# Importation des modules
from random import randint, random
import random
import webbrowser
# Déclaration des variables

items_achetable = {
"5e34c85e" : ["Baguette en bois de Botruc", 212],
"2a08b386" : ["Baguette en crin de dragon", 591],
"acf28d02" : ["Baguette de Victor Krum", 435],
"682de2f8" : ["Baguette élémentaire de l’eau", 895],
"eb1079da" : ["Baguette de Luna Lovegood", 304],
"87b2063b" : ["Baguette de Harry Potter", 400],

"37811069" : ["Echarpe Gryffondor", 275],
"c2c1fb1c" : ["Maillot de Quidditch Poufsouffle", 366],
"d3fa9d37" : ["Chaussettes Serpentard", 405],
"946f8990" : ["Bonnet Serdaigle", 489],
"3ba83b6b" : ["Sac à dos Serpentard", 741],
"8e57f68d" : ["Set Quidditch Gryffondor", 823],

"9a7a6965" : ["Défense contre la magie noire", 396],
"33427572" : ["Sorts et sortilèges niveau 1", 252],
"d4aed9b5" : ["Histoire de la magie", 141],
"220540c4" : ["Histoire du Quidditch", 175],
"1da54a7d" : ["Contes de Beedle la Barde", 347],
"7c238f99" : ["Initiation à la transfiguration", 194],
}

personnages_harry_potter = ['Harry Potter', 'Hermione Granger',
 'Ron Weasley', 'Albus Dumbledore', 'Severus Rogue', 'Voldemort', 
 'Draco Malfoy', 'Sirius Black', 'Rubeus Hagrid', 'Minerva McGonagall', 
 'Ginny Weasley', 'Fred Weasley', 'George Weasley', 'Neville Longbottom', 
 'Luna Lovegood', 'Cho Chang', 'Cedric Diggory', 'Dobby', 'Fleur Delacour', 
 'Gilderoy Lockhart', 'Ginny Weasley', 'Hedwig', 'Kreacher', 'Lavande Brown', 
 'Lee Jordan', 'Lily Potter', 'Luna Lovegood', 'Madame Maxime', 'Madame Pomfrey', 
 'Molly Weasley', 'Neville Longbottom', 'Nymphadora Tonks', 'Percy Weasley', 
 'Petunia Dursley', 'Rita Skeeter', 'Rubeus'] # Liste des personnages de Harry Potter

inventaire = [] # Liste des items achetés

personnage = random.choice(personnages_harry_potter) # Choix aléatoire d'un personnage de Harry Potter
argent_disponible = randint(500, 2000) # Choix aléatoire d'un montant d'argent disponible
webbrowser.open('https://nsi2.maxence.live') # Ouverture du site web
# Fonctions / procédures
def monnaie_a_rendre(argent):
    '''
    Fonction qui donne la monnaie à rendre en fonction d'un montant donné.
    A l'aide d'une liste qui contient les différentes monnaie qu'on puisse rendre,
    on parcours cette liste et on regarde si la valeur séléctionnée peut être déduite
    de la somme donnée en argument. Si la valeur séléctionnée peut être déduite, on sort de la boucle 
    et on recommence à parcourir la liste des différentes monnaie qu'on peut potentiellement rendre.
    On effectue cela jusqu'à ce que la somme mise en argument sois égale à 0.


    Entrée ------> int, une somme dont on veut connaître la somme a rendre

    Sortie ------> int, la somme à rendre
    '''
    monnaies = [500, 200, 100, 50, 20, 10, 5, 2, 1] # Liste des monnaies
    rendu = []
    while argent > 0:
        for monnaie in monnaies: # On parcours la liste des monnaies
            if monnaie <= argent: # Si la valeur de la monnaie est inférieur ou égale à la somme mise en argument
                argent -= monnaie
                rendu.append(monnaie)
                break
    return rendu



# Algorithme de monnaie limitée
def argent_avec_caisse_limite(argent):
    '''
    Fonction qui donne la monnaie à rendre en fonction d'un montant donné.
    Différence avec la fonction monnaie_a_rendre, cette fonction prend en compte
    la limite de monnaie qu'on peut rendre. 

    Entrée ------> int, une somme dont on veut connaître la somme a rendre

    Sortie ------> int, la somme à rendre
    '''
    monnaies_limite = {200: 1, 100: 3, 50: 1, 20: 1, 10: 1, 2: 5} # Dictionnaire des monnaies et de leur limite
    result = []
    for monnaie, limit in monnaies_limite.items():
        while limit > 0 and argent >= monnaie: # Tant que la limite est supérieur à 0 et que la somme mise en argument est supérieur ou égale à la monnaie
            result.append(monnaie)
            argent -= monnaie
            limit -= 1
    if argent == 0:
        return result
    else:
        return f"Je ne peux pas vous rendre cet argent je suis limité mais voici ce que je peux vous rendre {result}"


# Algorithme de monnaie avec caisse infinie mais avec conversion
def argent_min_avec_conversion(gallions, mornilles, noises):
  '''
    Cet fonction prend en compte 3 monnaies différentes et convertis les monnaies pour rendre le moins possible.
    On convertis les monnaies en noises, on calcul le nombre de gallions, mornilles et noises à rendre.

    Entrée ------> int, 3 sommes dont on veut connaître la somme a rendre

    Sortie ------> int, les sommes à rendre
    '''
  
  totale_des_noises = gallions * 17 * 29 + mornilles * 29 + noises #Convertis les monnaies en noises
  
  min_gallions = totale_des_noises // (17 * 29) #Calcul le nombre de gallions
  totale_des_noises -= min_gallions * 17 * 29 #Soustrait le nombre de gallions au total des noises
  min_mornilles = totale_des_noises // 29 #Calcul le nombre de mornilles
  min_noises = totale_des_noises % 29 #Calcul le nombre de noises
  
  return (min_gallions, min_mornilles, min_noises)

def mode1():
    '''
    Fonction qui permet de tester les fonctions du programme.

    Entrée ------> Aucun, Procedure, affiche les options disponibles

    Sortie ------> Procedure, redirige vers la fonction correspondante
    '''
    print('4 options sont disponibles : ')
    print('1 - Rendu de monnaie sans limite')
    print('2 - Rendu de monnaie avec limite')
    print('3 - Rendu de monnaie avec conversion')
    print('4 - Quitter le programme')
    choix = input('Quel mode voulez-vous utiliser ? ')
    if choix == '1':
        argent = int((input('Entrez un montant : ')))
        resultat = monnaie_a_rendre(argent)
        print(f'La monnaie à rendre est de {resultat}')
        mode1()
    elif choix == '2':
        argent = int(input('Entrez un montant : '))
        print(argent_avec_caisse_limite(argent))
        mode1()
    elif choix == '3':
        gallions = int(input('Entrez le nombre de gallions : '))
        mornilles = int(input('Entrez le nombre de mornilles : '))
        noises = int(input('Entrez le nombre de noises : '))
        resultat = argent_min_avec_conversion(gallions, mornilles, noises)
        print(f'Je vous rend {resultat[0]} gallions, {resultat[1]} mornilles et {resultat[2]} noises')
        mode1()
    elif choix == '4':
        print('Au revoir !')
        exit()
    else:
        print('Erreur, veuillez entrer 1, 2, 3 ou 4')
        mode1()


def modemagasins():
    '''
    Fonction qui permet d'éffectuer des achats dans le magasin. 
    Et de se faire rembourser en utilisant les algorithmes de l'exercice.

    Entrée ------> Aucun, Procedure, affiche les options disponibles

    Sortie ------> Procedure, redirige vers la fonction correspondante
    '''
    global argent_disponible
    print('Bienvenue dans le mode aventure')
    print('1 - Acheter un article')
    print('2 - Se faire rembourser')
    print('3 - Quitter le magasin')
    choix = input('Quel mode voulez-vous utiliser ? ')
    if choix == '1':
        id = input('Entrez l\'identifiant d\'un article : ')
        if id in items_achetable:
            item_name, item_price = items_achetable[id] # On récupère le nom et le prix de l'article
            if item_price > argent_disponible: # Si le prix de l'article est supérieur à l'argent disponible
                print(f"Vous n'avez pas assez d'argent pour acheter {item_name} !")
            else:
                argent_disponible -= item_price
                print(f"Merci d'avoir acheté {item_name} pour {item_price} gemmes ! Ajouté a votre inventaire !")
                inventaire.append(item_name)
            mode2()
        else:
            print(f"{id} est un identifiant invalide !")
            modemagasins()
    elif choix == '2':
        if len(inventaire) == 0:
            print('Votre inventaire est vide')
            mode2()
        else:
            print('Voici votre inventaire : ')
            print(inventaire)
            item = input('Quel article voulez-vous rembourser ? (tapez le nom de l\'article)')
            if item in inventaire:
                id_article = input('Verification nécessaire, tapez l\'identifiant de l\'article pour confirmer :')
                if id_article not in items_achetable: # Si l'identifiant n'est pas dans la liste des articles achetables
                    print('Erreur, identifiant incorrect, verification annulée') # On annule la vérification
                    modemagasins()
                if items_achetable[id_article][0] != item:
                    print('Erreur, identifiant incorrect') # Si l'article n'est pas le même que celui demandé
                    modemagasins() # On annule la vérification
                argent_disponible += items_achetable[id_article][1] # On ajoute l'argent au joueur
                inventaire.remove(item) # On retire l'article de l'inventaire
                print(f'Vous avez été remboursé de {items_achetable[id_article][1]} gemmes')
                mode2()
            else:
                print('Cet article n\'est pas dans votre inventaire') # Si l'article n'est pas dans l'inventaire
                modemagasins()
    elif choix == '3':
        mode2()
    else:
        print('Erreur, veuillez entrer 1, 2 ou 3')
        modemagasins()

def mode2():
    '''
    Fonction qui permet de naviguer entre les différents modes du mode aventure.

    Entrée ------> Aucun, Procedure, affiche les options disponibles

    Sortie ------> Procedure, redirige vers la fonction correspondante
    '''
    print(f'1 - Magasin ({argent_disponible} gemmes disponibles)')
    print('2 - Inventaire')
    print('3 - Retour au menu principal')
    choix = input('Quel mode voulez-vous utiliser ? ') 
    if choix == '1':
        modemagasins() 
    elif choix == '2':
        if len(inventaire) == 0:
            print('Votre inventaire est vide')
            mode2()
        else:
            print('Voici votre inventaire : ')
            print(inventaire)
            mode2()
    elif choix == '3':
        main()
    else:
        print('Erreur, veuillez entrer 1, 2 ou 3')
        mode2()

def main():
    '''
    Fonction qui permet de choisir le mode de fonctionnement du programme.

    Entrée ------> Aucun, Procedure, affiche les options disponibles

    Sortie ------> Procedure, redirige vers la fonction correspondante
    '''
    print('Bienvenue 2 modes ce propose à vous : ')
    print('1 - Mode test permet de tester le rendu de monnaie, sans limite, avec limite et avec conversion')
    print('2 - Mode aventure permet de faire des achats dans un magasin')
    mode = input('Quel mode voulez-vous utiliser ? ')
    if mode == '1':
        mode1()
    elif mode == '2':
        print(f'Vous êtes {personnage} et vous avez {argent_disponible} gemmes disponibles pour faire vos achats, le magasin est ouvert ! Ou rdv sur nsi2.maxence.live')
        mode2()
    else:
        print('Erreur, veuillez entrer 1 ou 2')
        main()
main()
