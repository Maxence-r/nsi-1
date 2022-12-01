from tkinter import *
import webbrowser

def sitescores():
    webbrowser.open_new("https://fr.wikipedia.org/wiki/Loi_de_Wien")


#on crée une fenêtre
fenetre = Tk()

# on la personnalise

fenetre.title("Ma partie")
fenetre.geometry("1080x720")
fenetre.minsize(480, 360)
fenetre.config(background='#2d224a')

#on crée une zone
zone = Frame(fenetre, bg='#2d224a', bd=2)

#on affiche le titre
premier_message = Label(zone, text = "Cliquez ici pour commencer la partie !", font = ("helvetica", 40), bg = '#2d224a', fg = 'white')
premier_message.pack()

zone.pack(expand='yes')

#on crée un bouton
bouton = Button(zone, text="démarrer", font = ("helvetica", 40), bg = '#dcd6ff', fg = '#2d224a', relief=SUNKEN, command=sitescores)
bouton.pack(pady=25, fill=X)



fenetre.mainloop()
