from tkinter import *

def fenetre_jeu():
    jeu = Tk()
    jeu.title("Ma partie")
    jeu.geometry("1080x720")
    jeu.minsize(720, 480)
    jeu.config(background='#F5f5dc')

    #on crée une zone
    zone_jeu = Frame(jeu, bg='#F5f5dc', bd=2)
    zone_jeu.pack(expand=YES)
    
def interface():
    #on crée une fenêtre
    fenetre = Tk()

    # on la personnalise

    fenetre.title("Bienvenue")
    fenetre.geometry("1080x720")
    fenetre.minsize(480, 360)
    fenetre.config(background='#2d224a')

    #on crée une zone
    zone = Frame(fenetre, bg='#2d224a', bd=2)

    #on affiche le titre
    premier_message = Label(zone, text = "Cliquez ici pour commencer la partie !", font = ("helvetica", 40), bg = '#2d224a', fg = 'white')
    premier_message.pack()

    zone.pack(expand=YES)

    #on crée un boutoncommand
    bouton = Button(zone, text="démarrer", font = ("helvetica", 40), bg = '#dcd6ff', fg = '#2d224a', relief=SUNKEN, command=fenetre_jeu)
    bouton.pack(pady=25, fill=X)

    fenetre.mainloop()

interface()
