'''
coding: utf-8
authors: @Etienne, @Thomas, @Maxence
date: 2/12/2022
license: Aucune
'''

from random import randint # Importation module random
import requests # Importation request pour envoyer les données au serveur
import webbrowser


#Initialisation des variables
characters_tab = []
dico = {}
sortdict = {}
moyenne = 0


def modeselection():
    '''
    Fonction qui permet de choisir le mode de jeu, et lance un fonction selon le choix
    Valeur d'entrée: Aucune
    Valeur de sortie: Aucune
    '''
    mode = input('Choisissez le mode de jeu (Harry Potter(HP) ou Je joue(JJ)): ') 
    if mode == 'HP' or mode == 'Harry Potter':
        print('Vous avez choisi le mode "Harry Potter"')
        partieHP()
    elif mode == 'Je joue' or mode == 'JJ':
        print('Vous avez choisi le mode "Je joue"')
        partieJJ()
    else:
        print('Vous n\'avez pas choisi un mode valide')
        modeselection() #relance si le mode de jeu n'est pas valide

def loadjoueurs():
    '''
    Fonction qui charge les joueurs
    Valeur d'entrée: Aucune
    Valeur de sortie: Dictionnaire
    '''
    with open('Characters.csv', mode='r', encoding='utf-8') as f:
        lines = f.readlines() #Lecture des lignes du fichier
        key_line = lines[0].strip()
        keys = key_line.split(";") 
        for line in lines[1:]: #Pour chaque ligne du fichier
            line = line.strip()
            values = line.split(';') 
            dico = {}
            dico[keys[1]] = values[1]
            characters_tab.append(dico)
        return characters_tab #Retourne le tableau de dictionnaires

def partieJJ():
    '''
    Fonction qui permet de jouer au mode "Je joue"
    Valeur d'entrée: Aucune
    Valeur de sortie: Aucune
    '''
    listmots = ['fleur', 'tournevis', 'nsi', 'chemin'] #Liste des mots qui peuvent être choisis
    correct = listmots[randint(0, listmots.__len__()-1)]
    finalcorrect = correct
    score = 11 #Score initial
    display = '_'*correct.__len__() #Affichage initial
    while score != 0 and correct != '': #Tant que le score n'est pas à 0 et que le mot n'est pas trouvé
        print(display)
        reponse = input('Entrer une lettre ? ')
        if reponse in correct and reponse.__len__() < 2:
            indice = finalcorrect.find(reponse)
            display = display[:indice] + reponse + display[indice+1:] 
            correct = correct.replace(reponse, '')
        else:
            print('Ce n\'est pas la bonne lettre il vous reste', score-1, "essais")
            score -= 1
    print('\033[92mVous avez gagné !')
    request('jj', finalcorrect, score) #Envoie les données au serveur avec les paramètres

def partieHP():
    '''
    Fonction qui permet de jouer au mode "Harry Potter"
    Valeur d'entrée: Aucune
    Valeur de sortie: Aucune
    '''
    for joueur in loadjoueurs(): #Pour chaque joueur
        globalscore = 0 #Score incrementé a chaque partie pour chaque joueur
        for _ in range(10): #10 parties
            score = 11
            essais = 0
            letter = "abcdefghijklmnopqrstuvwxyz" #Liste des lettres
            reponse = 'nsi'
            while essais < 11 and reponse != '':
                choix = letter[randint(0, letter.__len__()-1)] #Choix d'une lettre au hasard
                letter = letter.replace(choix, '') #Suppression de la lettre choisie
                if choix in reponse:
                    reponse = reponse.replace(choix, '') #Suppression de la lettre choisie dans le mot
                else:
                    score -= 1
                    essais += 1
            globalscore += score #Ajout du score de la partie au score global du joueur
        dico[joueur['Name']] = globalscore #Ajout du score global du joueur au dictionnaire
    sortdict = sort(dico)
    moyennejoueurs = moyenne(sortdict) #Calcul de la moyenne des joueurs
    request('hp', sortdict, moyennejoueurs) #Envoie les données au serveur avec les paramètres

def sort(dico):
    '''
    Fonction qui permet de trier le dictionnaire
    Valeur d'entrée: Dictionnaire
    Valeur de sortie: Dictionnaire trié
    '''
    convertedlist = list(dico.items())  # Convertir le dictionnaire en liste
    l = len(convertedlist)
    for i in range(l-1):
        for j in range(i+1,l):
                if convertedlist[i][1] < convertedlist[j][1]: #verifie si le score du joueur a l'indice i est plus petit que le score du joueur a l'indice j
                    t = convertedlist[i]
                    convertedlist[i] = convertedlist[j] #si oui, on inverse les deux joueurs et donc leurs scores
                    convertedlist[j] = t 
    sortdict = dict(convertedlist) #on transforme la liste en dictionnaire
    return sortdict



def moyenne(sortdict):
    '''
    Fonction qui permet de calculer la moyenne des scores
    Valeur d'entrée: Dictionnaire
    Valeur de sortie: Entier
    '''
    somme = 0 
    for joueur in sortdict:
        somme += sortdict[joueur] #Somme des scores
    moyenne = somme/len(sortdict) #Moyenne des scores
    result = ("%.2f" % round(moyenne, 2)) #Arrondi a 2 chiffres apres la virgule
    return result

def request(type, value1, value2):
    '''
    Fonction qui permet d'envoyer les données au serveur
    Valeur d'entrée: Chaine de caractères, dictionnaire, entier
    Valeur de sortie: Aucune
    '''
    if type == 'hp':
        out = dict(list(value1.items())[0: 4])  # On ne prend que les 4 premiers joueurs
        pseudo = input('Les scores vont être envoyés sur le serveur, entrez un pseudo: ') #Demande du pseudo
        url = 'https://nsi1.maxence.live/auth/hp' #URL du serveur
        x = requests.post(url, json={'content': value1, 'owner': pseudo, 'moyenne': value2, 'first': out})  # Envoie des données au serveur
        print("Copier l'identifiant de votre partie: ", x.text[1:-1]) #Affichage de l'identifiant de la partie
        webbrowser.open_new_tab('https://nsi1.maxence.live/') #Ouverture de la page web
        
    elif type == 'jj': 
        pseudo = input('Les scores vont être envoyés sur le serveur, entrez un pseudo: ') #Demande du pseudo
        url = 'https://nsi1.maxence.live/jj' #URL du serveur
        x = requests.post(url, json={'owner': pseudo, 'word': value1, 'try': value2}) # Envoie des données au serveur
        webbrowser.open_new_tab('https://nsi1.maxence.live?owner='+pseudo+'&word='+value1+'&try='+ str(value2) +'&id='+x.text[1:-1]) #Ouverture de la page web
        print("Rendez vous sur: "+'https://nsi1.maxence.live?owner='+pseudo+'&word='+value1+'&try='+ str(value2) +'&id='+x.text[1:-1]) #Affichage de l'URL de la partie
 

modeselection() # Choix du mode de jeu # initialisation du jeu
