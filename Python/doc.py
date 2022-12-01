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

def main():
    """
    Function principal qui lance les actions 1 a 1
    Valeur d'entrée: Aucune
    Valeur de sortie: Aucune
    """
    loadjoueurs() # Charge les joueurs du csv
    modeselection() # Choix du mode de jeu


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
        modeselection()

def loadjoueurs():
    '''
    Fonction qui charge les joueurs
    Valeur d'entrée: Aucune
    Valeur de sortie: Aucune
    '''
    global characters_tab
    with open('Characters.csv', mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        key_line = lines[0].strip()
        keys = key_line.split(";")
        for line in lines[1:]:
            line = line.strip()
            values = line.split(';') 
            dico = {}
            dico[keys[1]] = values[1]
            characters_tab.append(dico)

def partieJJ():
    '''
    Fonction qui permet de jouer au mode "Je joue"
    Valeur d'entrée: Aucune
    Valeur de sortie: Aucune
    '''
    listjoueurs = ['fleur', 'tournevis', 'nsi', 'chemin']
    correct = listjoueurs[randint(0, listjoueurs.__len__()-1)]
    finalcorrect = correct
    score = 11
    print(correct)
    display = '_'*correct.__len__()
    while score != 0 and correct != '':
        print(display)
        reponse = input('Entrer une lettre ? ')
        if reponse in correct and reponse.__len__() < 2:
            indice = finalcorrect.find(reponse)
            display = display[:indice] + reponse + display[indice+1:] # do it for all occurences
            correct = correct.replace(reponse, '')
        else:
            print('Ce n\'est pas la bonne lettre il vous reste', score-1, "essais")
            score -= 1
    print('\033[92mVous avez gagné !')
    request('jj', finalcorrect, score)

def partieHP():
    '''
    Fonction qui permet de jouer au mode "Harry Potter"
    Valeur d'entrée: Aucune
    Valeur de sortie: Aucune
    '''
    for joueur in characters_tab:
        globalscore = 0
        for _ in range(10):
            score = 11
            essais = 0
            letter = "abcdefghijklmnopqrstuvwxyz"
            reponse = 'nsi'
            while essais < 11 and reponse != '':
                choix = letter[randint(0, letter.__len__()-1)]
                letter = letter.replace(choix, '')
                if choix in reponse:
                    reponse = reponse.replace(choix, '')
                    print('Le personnage est ', joueur['Name'], ' et le score est de ', score, 'avec', choix)
                else:
                    score -= 1
                    essais += 1
                    print('Le personnage est ', joueur['Name'], ' et le score est de ', score, 'sans', choix, 'IL RESTE', 11-essais, 'ESSAIS')
            globalscore += score
            print('Le score global du joueur ', joueur['Name'], ' est de ', globalscore)
        dico[joueur['Name']] = globalscore
    sortdict = sort(dico)
    moyennejoueurs = moyenne(sortdict)
    request('hp', sortdict, moyennejoueurs)

def sort(dico):
    '''
    Fonction qui permet de trier le dictionnaire
    Valeur d'entrée: Dictionnaire
    Valeur de sortie: Dictionnaire trié
    '''
    convertedlist = list(dico.items())
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
        somme += sortdict[joueur]
    moyenne = somme/len(sortdict)
    result = ("%.2f" % round(moyenne, 2))
    return result

def request(type, value1, value2):
    '''
    Fonction qui permet d'envoyer les données au serveur
    Valeur d'entrée: Chaine de caractères, dictionnaire, entier
    Valeur de sortie: Aucune
    '''
    if type == 'hp':
        out = dict(list(value1.items())[0: 4]) 
        pseudo = input('Les scores vont être envoyés sur le serveur, entrez un pseudo: ')
        url = 'http://localhost:3000/auth/hp'
        x = requests.post(url, json={'content': value1, 'owner': pseudo, 'moyenne': value2, 'first': out})
        print("Copier l'identifiant de votre partie: ", x.text[1:-1])
        webbrowser.open_new_tab('http://localhost:3000/')
        
    elif type == 'jj': 
        pseudo = input('Les scores vont être envoyés sur le serveur, entrez un pseudo: ')
        url = 'http://localhost:3000/jj'
        x = requests.post(url, json={'owner': pseudo, 'word': value1, 'try': value2})
        print("Copier l'identifiant de votre partie: ", x.text[1:-1])
main() # initialisation du jeu
