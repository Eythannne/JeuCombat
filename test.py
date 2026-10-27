#MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#]
#
#HEROS = [
#   "H1"
#   "H2"
#   "H3"
#   "H4"
#   "H5"
#]
#
#MONTRES = [
#   "M1"
#   "M2"
#   "M3"
#   "M4"
#   "M5"
#]
#
#
#Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
#Choix (options, erreur)
#   while True:
#       Recuperer choix utilisateur
#       Verifier si choix est valide
#       Si valide
#           return choix
#       Sinon
#           Lancer fonction erreur
#Process
#
#
#
#
#
#
#
#
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
#
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
#
#
#
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