import tkinter as tk
from tkinter import *

root2 = tk.Tk()

def Page_jeu():
    

    root2.title("Le jeu du pendu")
    root2.geometry("1080x720")
    root2.config(bg="black")

    view_canvas = tk.Canvas(root2, width=1200, height=600, bg="black")

    #Choix de la longueur du mot
    #Nb_lettres=tk.Spinbox(view_canvas, from_=4, to=10,font=("Arial",25),width=30,command=)
    #Nb_lettres.place(x=300,y=400)

    #Boutons
    #Validation_nb=tk.Button(view_canvas,text="Valider",command=)
    #Validation_nb.place(x=600,y=450)

    #Validation_lettres=tk.Button(view_canvas,text="Valider la lettre",command=)
    #Validation_lettres.place_forget()"""

    #Longueur_texte=tk.Label(view_canvas,text="Choisis la longueur du mot",font=("Arial",20),width=30,command=)
    #Longueur_texte.place(x=350,y=350)

    Indice=tk.Button(root2,text="Indice", font=("Arial",15))
    Indice.grid(column=0, row=360)


lettre_saisie = tk.StringVar()  #stringvar = type d'objet propre à tkinter : il s'agit d'un str variable

valeur_str=lettre_saisie.get()  #je nomme valeur_str (str car c'est une str, c'etait pour mieux m'y retrouver) la valeur que je récupère de la variable valeur saisie (grâce au .get())


def bouton_ok():    #programmation du bouton ok : bouton qui va
    
    bienvenue = tk.Label(root2, text="à vous de jouer !", font=("helvetica", "25"))  #dans cette 2e fenêtre je choisi d'afficher un message indiquant le début du jeu : c'est là qu'il y aura le dessin du pendu
    bienvenue.grid(column=2, row=360)  #placement du texte créé dans la fenêtre
        
    label = tk.Label(root2, text=(valeur_str), font=("helvetica", "20")) #création de l'affichage de la lettre
    label.grid(column=20, row=20)  #placement de la lettre
            
valeur_label = tk.Label(root2, text = "Choisir une lettre de l'alphabet :", font=('helvetica',10, 'bold')) #dans la fenêtre 2, création du texte qui demande à l'utilisateur de saisir la lettre... (texte en gras)    
valeur_entry = tk.Entry(root2,textvariable = lettre_saisie, font=('helvetica',10))  #création du widget Entry : widget pour que l'utilisateur entre sa lettre


bouton=tk.Button(root2,text = 'Valider', command = bouton_ok)  #création du widget bouton ok

valeur_label.grid(row=0,column=0)  #placement des 3 widget que l'on vient de créer
valeur_entry.grid(row=0,column=1)

bouton.grid(row=2,column=1)
 

#######################################
## PROGRAMME PRINCIPAL
# if __name__ == "__main__":
#     page_accueil()

Page_jeu()

# longueur_mot = int(input("Choisir la longueur du mots entre 4 et 10"))
# choisir_mot(longueur_mot)
# jeu_pendu(mot_choisi)

root2.mainloop()