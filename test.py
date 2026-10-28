import random
import sys

from pymongo import MongoClient
from pymongo.errors import PyMongoError


#MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#]
MENU = [
    "Lancer Jeu",
    "Afficher les scores",
    "Quitter"
]

#
#HEROS = [
#   "H1"
#   "H2"
#   "H3"
#   "H4"
#   "H5"
#]
#
HEROS = [
    "H1",
    "H2",
    "H3",
    "H4",
    "H5"
]

#MONTRES = [
#   "M1"
#   "M2"
#   "M3"
#   "M4"
#   "M5"
#]
MONSTRES = [
    "M1",
    "M2",
    "M3",
    "M4",
    "M5"
]

#JOUEURS = []
JOUEURS = []

#Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
def menu():
    for numero, texte in enumerate(MENU, start=1):
        print(f"{numero}. {texte}")

#Choix (options, erreur)
#   while True:
#       Recuperer choix utilisateur
#       Verifier si choix est valide
#       Si valide
#           return choix
#       Sinon
#           Lancer fonction erreur
def erreur(message="Choix invalide, réessaie."):
    print(message)

def choix(options, erreur):
    while True:
        reponse = input("Ton choix :").strip()
        if reponse in [str(i) for i in range(1, len(options) + 1)]:
            return int(reponse)
        erreur()

menu()
numero = choix(MENU, erreur)
print("Tu as choisi :", numero)

#
#
#JEU
#   CREATION D'UN JOUEUR
#       pseudo = ""
#       Demander le pseudo
#           while True
#               Recuperer reponse utilisateur
#               Si !vide
#                   pseudo = reponse utilisateur
#                   return pseudo
#               Sinon
#                   Lancer fonction erreur

def creation_joueur():
    while True:
        reponse = input("Choisis ton pseudo :").strip()
        if len(reponse) > 3 and len(reponse) < 15:
            return reponse
        erreur()


pseudo = creation_joueur()
print("ton pseudo est : ", pseudo)


#   CREATION D'UNE EQUIPE
#       equipe = liste vide
#       Boucle sur tout les éléments de HEROS
#           afficher numero element et texte element

def afficher_heros():
    for numero, hero in enumerate(HEROS, start=1):
        print(f"{numero}. {hero}")

#       Choix (options, erreur)
#           while True:
#               si equipe < 3
#                   Recuperer choix utilisateur
#                   Verifier si choix est valide
#                   Si valide
#                    equipe.append(choix)
#                    return choix
#                Sinon
#                    Lancer fonction erreur
#            sinon
#                return equipe

def creation_equipe():
    equipe = []
    while True:
        if len(equipe) < 3:
            afficher_heros()
            numero = choix(HEROS, erreur)
            hero = HEROS[numero - 1]
            if hero in equipe:
                erreur("Ce personnage est déjà dans ton équipe.")
            else:
                equipe.append(hero)
                print("Ton équipe :", equipe)
        else:
            return equipe

equipe = creation_equipe()
print("Équipe faite au complet :", equipe)

#
#   COMBAT INFINIE
#   vague initialisé a 0
#   while 1 perso > pv = 0
#
#       TIRAGE DU MONSTRE
#       monstre = random.choice(MONSTRES)
#       afficher monstre
#           
#       EQUIPE ATTAQUE MONSTRE
#           pour chaque hero vivant
#               si monstre.pv <= 0
#                   sortir de la boucle
#               degats = hero.attaque - monstre.defense
#               monstre.pv = monstre.pv - degats
#
#           si monstre.pv <= 0
#               afficher "Victoire"
#               vague = vague + 1
#
#
#       MONSTRE ATTAQUE EQUIPE
#           sinon
#               hero_cible choisis aleatoirement
#               degats = monstre.attaque - hero.defense
#               hero_cible.pv = hero_cible - degats
#               si hero_cible.pv <= 0
#                   afficher "hero KO"
#
#   ENREGISTRER LE SCORE
#       Affchier "Defaite" et le nombre de vague final
#       Ouvrir la bdd
#       acceder a la bdd
#       inserer le score(pseudo, vague) dans la collection score
#
#   AFFICHER LE SCORE
#       Lancer la fonction "Afficher les scores"
#
#
#
#SCORE    
#   Afficher les scores
#       Recuperer scores base
#           ouvrir base
#           acceder a collection score
#           find
#           convertir curseur en list
#       filtrer les 3 meilleurs
#           trie le tableau sur element.waves
#           prendre 3 derniers elements
#               array[-3:-1]
#       Affiche les score
#   Quitter
#       sys.exit()
#