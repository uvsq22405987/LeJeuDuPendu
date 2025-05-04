#bouton indice amélioré -> voir les 2 fonctions (ligne 28 et ligne 82) + creation de la variable nb_indices_restants (ligne 34)

import tkinter as tk
from tkinter import *
import random
import json
from tkinter import messagebox

def Page_jeu():
    global root2, Nb_lettres, Longueur_texte, Afficher_mot, mot_cache, Validation_nb, Validation_lettres, Nb_erreurs, Lettres,canvas_pendu
    root2 = tk.Tk()

    root2.title("Le jeu du pendu")
    root2.geometry("1080x720")
    root2.config(bg="black")

Page_jeu()

##########################################################################################################################
#################### VARIABLE DU JEU ############################
lettres_trouvees=[]
lettres_fausses=[]
longueur = {}

########################################################################################
#######################  FONCTION POUR LA PAGE DE JEU ################################

#fonction qui détermine le nb d'indices en fonction de la longueur du mot
def nb_indices() :
    global longueur

    if longueur == 4: 
        indices = 1
    elif longueur == 5 :
        indices = 2
    elif longueur == 6: 
        indices = 3
    elif longueur == 7: 
        indices = 3
    elif longueur == 8: 
        indices = 4
    elif longueur == 9: 
        indices = 4
    elif longueur == 10: 
        indices = 5
    # else :              #au cas où je ne sais pas comment l'utilisateur parviant à entrer une longueur qui n'est pas acceptée
    #     indices = 0
    return indices 

#Fonction qui valide la longueur du mots et le nombre d'essais maximum et qui enlève la visibilité de ces labels
def Validation_longueur():
    global Nb_lettres, longueur, nb_essais_max, nb_indices_restants

    longueur=int(Nb_lettres.get())
    nb_essais_max = int(Nb_erreurs.get())
    nb_indices_restants = nb_indices() #variable initialisée en dehors de la fonction bouton_indice car sinon elle sera tjrs = à 3 chaque nouveau clic sur le bouton et donc le if sera toujours vrai : pas de stop 
    
    Nb_lettres.place_forget()
    Validation_nb.place_forget()
    Nb_erreurs.place_forget()
    
    Validation_lettres.place(x=600,y=450)
    Indice.place(x=0,y=360)
    jeu()
    return nb_essais_max

#Fonction qui afficher le mot et le nombre erreurs
def affichage_mot_et_erreurs(nb_essais_max, lettres_trouvees, lettres_fausses, mot_choisi):
    global Essais_restants

    Essais_restants=nb_essais_max-len(lettres_fausses)
    mot_cache = "".join([tentative if tentative in lettres_trouvees else "*" for tentative in mot_choisi])

    Afficher_mot=tk.Label(root2,text=mot_cache, font=("Arial",20),width=30)
    Afficher_mot.place(x=350,y=350)
    Afficher_essais_restants=tk.Label(root2,text=("Essais restants", Essais_restants), font=("Arial",20),width=30)
    Afficher_essais_restants.place(x=10,y=10)


#######################################################################################

# FONCTIONS POUR LE BOUTON INDICE ICI :

def bouton_indice(mot_choisi, nb_essais_max) : #mot_choisi issu de la fonction jeu(), resultat de choisir_mot(longueur) ; nb_essai issu de validation_longueur
    global lettres_trouvees, nb_indices_restants

    if nb_indices_restants > 0 :
        for lettre in mot_choisi :
            if lettre not in lettres_trouvees : #rappel : lettre = variable qui contient la lettre saisie par l'utilisateur
                lettres_trouvees.append(lettre)
                break #revele qu'1 seule lettre

        affichage_mot_et_erreurs(nb_essais_max, lettres_trouvees, lettres_fausses, mot_choisi)
        nb_indices_restants = nb_indices_restants - 1

    elif nb_indices_restants == 0 :  
        messagebox.showerror(title="STOP", message="Vous avez déjà utilisé le nombre maximum d'indices disponibles")
        Indice.config(state=tk.DISABLED)  # Désactive le bouton Indice

    Afficher_indices_restants=tk.Label(root2,text=("Indices restants", nb_indices_restants), font=("Arial",20),width=30)
    Afficher_indices_restants.place(x=20,y=100)



#####################################################################################
############################ FONCTIONS DU JEU :
#Fonction d'initialisation du jeu (à modifier peut être)
def jeu():
    global mot_choisi, Longueur_texte
    mot_choisi=choisir_mot(longueur)
    Longueur_texte.destroy()
    affichage_mot_et_erreurs(nb_essais_max,lettres_trouvees,lettres_fausses,mot_choisi)
    Lettres.place(x=300,y=400)
    return


#Fonction qui choisi un mot aléatoirement en fonction de la longueur de celui ci en 'piochant' dans le fichier Liste_mots
def choisir_mot(longueur_mot):
    #with open("Liste_mots.json","r") as fichier_mots:
    with open("c:/Users/klerv/OneDrive/Bureau/fondements de l'info z S2/projet/Liste_mots.json", "r") as fichier_mots:
        mots=json.load(fichier_mots)
    return random.choice(mots[str(longueur_mot)])


#Fonction qui vérifie les lettres entrées
def verification_lettres(lettres_trouvees,lettres_fausses,nb_essais_max):
        tentative = Lettres.get().lower()
        Lettres.delete(0, tk.END)
        if not tentative.isalpha() or len(tentative) != 1 :
            messagebox.showerror(title="Problème", message="Veuillez entrer qu'une seule lettre de l'alphabet")
            return

        if (tentative in lettres_trouvees) or (tentative in lettres_fausses) :
            messagebox.showwarning(title="Problème",message="Vous avez déja entré cette lettre")
            return

        if tentative in mot_choisi :
            lettres_trouvees.append(tentative)
        else :
            lettres_fausses.append(tentative)
            print(lettres_fausses)

        mot_cache = "".join([tentative if tentative in lettres_trouvees else "*" for tentative in mot_choisi])
        affichage_mot_et_erreurs(nb_essais_max,lettres_trouvees,lettres_fausses,mot_choisi)

        if Essais_restants==0:
            messagebox.showerror(title="Partie terminée",message=f"Vous avez malheureusement perdu\nLe mot à deviner était : {mot_choisi}")

        if mot_cache == mot_choisi :
            messagebox.showinfo(title="Victoire", message=f"Bravo vous avez deviné le mot : {mot_choisi}")

        return lettres_fausses,lettres_trouvees



    #Choix de la longueur du mot
Longueur_texte=tk.Label(root2,text="Choisis la longueur du mot      Et le nombre d'erreurs acceptés",font=("Arial",20),width=50)
Longueur_texte.place(x=200,y=350)

Nb_lettres=tk.Spinbox(root2, from_=4, to=10,font=("Arial",25),width=5)
Nb_lettres.place(x=400,y=400)

Nb_erreurs=tk.Spinbox(root2, from_=4, to=7,font=("Arial",25),width=5)
Nb_erreurs.place(x=700,y=400)

    #Saisie des lettres
Lettres=tk.Entry(root2,width=30,font=("Arial",25))

    #Boutons
Validation_nb=tk.Button(root2,text="Valider le choix",command=Validation_longueur)
Validation_nb.place(x=550,y=450)

Validation_lettres=tk.Button(root2,text="Valider la lettre",command=lambda: verification_lettres(lettres_trouvees,lettres_fausses,nb_essais_max))
Validation_lettres.place_forget()

Indice=tk.Button(root2,text="Indice", font=("Arial",15), command= lambda : bouton_indice(mot_choisi, nb_essais_max))
Indice.place_forget()


root2.mainloop()


