import tkinter as tk
from tkinter import *

root2 = tk.Tk()

def Page_jeu():
    

    root2.title("Le jeu du pendu")
    root2.geometry("1080x720")
    root2.config(bg="black")

    view_canvas = tk.Canvas(root2, width=1200, height=600, bg="black")


#BOUTONS:

#Choix de la longueur du mot

texte_longueur_mot=tk.Label(root2,text="Choisir la longueur du mot", font=("Arial",20), width=20)
texte_longueur_mot.grid(column=0, row=4)

Nb_lettres=tk.Spinbox(root2, from_=4, to=10,font=("Arial",25),width=5)
Nb_lettres.grid(column=0, row=6)


longueur_validee = 0 #je prédéfini la variable avant de la modifier dans la fonction validation_longueur (cela m'évitera des erreurs par la suite)

def Validation_longueur() :
    global longueur_validee   #j'indique que la variable longueur_validee existe déjà et qu'il faut écraser le 0 avec la nouvelle valeur sélectionnéee par l'utilisateur
    longueur_validee = int(Nb_lettres.get())   #recupere la valeur de la spinbox
    return longueur_validee
 

mot = tk.Label(root2, text="*"*longueur_validee, font=("Arial", 20), width=10) #je prédéfini la variable mot avant de la modifier plus tard dans la fonction affiche_mot (pour l'instant longueur_validee = 0 donc le mot est inexistant)
mot.grid_forget() #le mot est inexistant mais le label (vide) existe donc il faut le cacher

def affiche_mot() :
    mot.config(text="*" * longueur_validee)
    return mot.grid(column= 1, row=10)

def actions_du_bouton_valider_longueur() : #fonction qui compile les deux actions que le bouton validation_long doit effectuer 
    Validation_longueur()
    affiche_mot()

Validation_long=tk.Button(root2,text="Valider le choix", command=actions_du_bouton_valider_longueur)
Validation_long.grid(column=0, row=7)

root2.mainloop()