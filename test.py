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
    "Quitter",
]

#HEROS = [
#   "H1"
#   "H2"
#   "H3"
#   "H4"
#   "H5"
#]
HEROS = [
    {"nom": "H1", "pv": 30, "attaque": 8, "defense": 3},
    {"nom": "H2", "pv": 25, "attaque": 10, "defense": 2},
    {"nom": "H3", "pv": 40, "attaque": 6, "defense": 5},
    {"nom": "H4", "pv": 20, "attaque": 12, "defense": 1},
    {"nom": "H5", "pv": 35, "attaque": 7, "defense": 4},
]

#MONTRES = [
#   "M1"
#   "M2"
#   "M3"
#   "M4"
#   "M5"
#]
MONSTRES = [
    {"nom": "M1", "pv": 20, "attaque": 7, "defense": 2},
    {"nom": "M2", "pv": 30, "attaque": 9, "defense": 3},
    {"nom": "M3", "pv": 25, "attaque": 11, "defense": 1},
    {"nom": "M4", "pv": 40, "attaque": 8, "defense": 4},
    {"nom": "M5", "pv": 50, "attaque": 10, "defense": 5},
]

#Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
def afficher_menu():
    for i, texte in enumerate(MENU):
        print(f"{i + 1} - {texte}")

#Choix (options, erreur)
#   while True:
#       Recuperer choix utilisateur
#       Verifier si choix est valide
#       Si valide
#           return choix
#       Sinon
#           Lancer fonction erreur
def erreur():
    print("Choix invalide, réessaie !")

def choix_utilisateur(options, erreur):
    while True:
        reponse_utilisateur = input("Ton choix : ")
        if reponse_utilisateur.isdigit() and 1 <= int(reponse_utilisateur) <= len(options):
            return int(reponse_utilisateur)
        else:
            erreur()

def lancer_jeu():
    pseudo_joueur = creer_joueur()
    equipe_hero = creer_equipe()
    vague = combat_infini(equipe_hero)

def quitter_jeu():
    sys.exit()

def process():
    while True:
        afficher_menu()
        c = choix_utilisateur(MENU, erreur)
        if c == 1:
            lancer_jeu()
        elif c == 2:
            afficher_scores()
        else:
            quitter_jeu()

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
def creer_joueur():
    pseudo_joueur = ""
    print("Quel est ton pseudo ?")
    while True:
        reponse_utilisateur = input("Pseudo : ")
        if reponse_utilisateur != "":
            pseudo_joueur = reponse_utilisateur
            return pseudo_joueur
        else:
            erreur()

#   CREATION D'UNE EQUIPE
#       equipe = liste vide
#       Boucle sur tout les éléments de HEROS
#           afficher numero element et texte element
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
def creer_equipe():
    equipe_hero = []
    for i, hero in enumerate(HEROS):
        print(f"{i + 1} - {hero['nom']} (PV {hero['pv']}, ATK {hero['attaque']}, DEF {hero['defense']})")
    while len(equipe_hero) < 3:
        print(f"Choisis ton héros {len(equipe_hero) + 1}/3")
        c = choix_utilisateur(HEROS, erreur)
        equipe_hero.append(dict(HEROS[c - 1]))
    return equipe_hero

def equipe_est_en_vie(equipe_hero):
    for hero in equipe_hero:
        if hero["pv"] > 0:
            return True
    return False

#   COMBAT INFINIE
#   vague initialisé a 0
#   while 1 perso > pv = 0
def combat_infini(equipe_hero):
    nb_vague = 0
    monstre = tirer_monstre()
    while equipe_est_en_vie(equipe_hero):
        equipe_attaque(equipe_hero, monstre)
        if monstre["pv"] <= 0:
            print("Victoire !")
            nb_vague = nb_vague + 1
            monstre = tirer_monstre()
        else:
            monstre_attaque(equipe_hero, monstre)
    return nb_vague

#
#       TIRAGE DU MONSTRE
#       monstre = random.choice(MONSTRES)
#       afficher monstre
def tirer_monstre():
    monstre = dict(random.choice(MONSTRES))
    print("Un", monstre["nom"], "apparaît !")
    return monstre

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
def equipe_attaque(equipe_hero, monstre):
    for hero in equipe_hero:
        if hero["pv"] > 0 and monstre["pv"] > 0:
            degats = calculer_degats(hero["attaque"], monstre["defense"])
            monstre["pv"] = monstre["pv"] - degats
            print(hero["nom"], "inflige", degats, "dégâts")

#
#
#       MONSTRE ATTAQUE equipe
#           sinon
#               hero_cible choisis aleatoirement
#               degats = monstre.attaque - hero.defense
#               hero_cible.pv = hero_cible - degats
#               si hero_cible.pv <= 0
#                   afficher "hero KO"
def monstre_attaque(equipe_hero, monstre):
    hero_vivants = []
    for hero in equipe_hero:
        if hero["pv"] > 0:
            hero_vivants.append(hero)
    cible = random.choice(hero_vivants)
    degats = calculer_degats(monstre["attaque"], cible["defense"])
    cible["pv"] = cible["pv"] - degats
    print(monstre["nom"], "inflige", degats, "dégâts à", cible["nom"])
    if cible["pv"] <= 0:
        print(cible["nom"], "est KO")




def calculer_degats(attaque, defense):
    degats = attaque - defense
    if degats < 1:
        degats = 1
    return degats

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

process()