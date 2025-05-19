#afficher les lettres déjà essayées : voir ligne 57

import tkinter as tk
from tkinter import *
import webbrowser
import random
import json
from tkinter import messagebox

# PENSER A TELECHARGER LE FICHIER LISTE_MOTS AVANT DE LANCER LE PROGRAMME
############################################################################################################################"
######################## FONCTION POUR LA PAGE D'ACCUEIL ############################
# Fonction pour ouvrir les règles du jeu
def open_rules():
    webbrowser.open_new("https://champagnole.circo39.ac-besancon.fr/wp-content/uploads/sites/9/2020/04/jeu-du-pendu.pdf")

# Fonction pour démarrer le jeu
def start_game():
    global window
    window.destroy()
    Page_jeu()

##########################################################################################################################
#################### VARIABLE DU JEU ############################
lettres_trouvees=[]
lettres_fausses=[]

########################################################################################
#######################  FONCTION POUR LA PAGE DE JEU ################################
#Fonction qui valide la longueur du mots et le nombre d'essais maximum et qui enlève la visibilité de ces labels
def Validation_longueur():
    global Nb_lettres, longueur, nb_essais_max
    longueur=int(Nb_lettres.get())
    nb_essais_max = int(Nb_erreurs.get())
    Nb_lettres.place_forget()
    Validation_nb.place_forget()
    Nb_erreurs.place_forget()
    Validation_lettres.place(x=600,y=450)
    Indice.place(x=0,y=360)
    jeu()
    return nb_essais_max

#Fonction qui afficher le mot et le nombre erreurs

def affichage_mot_et_erreurs(nb_essais_max,lettres_trouvees,lettres_fausses,mot_choisi):
    global Essais_restants

    Essais_restants=nb_essais_max-len(lettres_fausses)
    mot_cache = "".join([tentative if tentative in lettres_trouvees else "*" for tentative in mot_choisi])

    Afficher_mot=tk.Label(root2,text=mot_cache, font=("Arial",20),width=30)
    Afficher_mot.place(x=350,y=350)

    Afficher_erreurs_restantes=tk.Label(root2,text=("Essais restants", Essais_restants), font=("Arial",20),width=30)
    Afficher_erreurs_restantes.place(x=10,y=10)

    Afficher_lettres_essayees=tk.Label(root2, text=("Lettres déjà essayées", lettres_fausses), font=("Arial", 20), width=25)
    Afficher_lettres_essayees.place(x=10,y=550)

#fonction commande du bouton indice :    
mot_choisi = None

def bouton_indice(mot_choisi, nb_essais_max) : #mot_choisi issu de la fonction jeu(), resultat de choisir_mot(longueur) ; nb_essai issu de validation_longueur
    global lettres_trouvees 

    for k in mot_choisi :
        if k not in lettres_trouvees : #rappel : k correspond à la lettre du coup, k prend la valeur de chaque lettre du mot 1 par 1
            lettres_trouvees.append(k)
            break #revele qu'1 seule lettre
        
    affichage_mot_et_erreurs(nb_essais_max, lettres_trouvees, lettres_fausses, mot_choisi)

#fonction pour le bouton quitter :
def bouton_quitter() :
    root2.destroy()

#Fonction du dessin du pendu
def dessin_pendu(erreurs):
        if erreurs >= 0:
            canvas_pendu.create_line(500,100,500,300, fill='white', width=2)
            canvas_pendu.create_line(500,100,600,100, fill='white', width=2)
        if erreurs >=1:
            canvas_pendu.create_line(600,100,600,110, fill='white', width=2)
        if erreurs >=2:
            canvas_pendu.create_oval(580,110,620,150, fill='white', width=2)
        if erreurs >=3:
            canvas_pendu.create_line(600,150,600,200, fill='white', width=2)
        if erreurs >=4:
            canvas_pendu.create_line(600,150,575,175, fill='white', width=2)
        if erreurs >=5:
            canvas_pendu.create_line(600,150,625,175, fill='white', width=2)
        if erreurs >=6:
            canvas_pendu.create_line(600,200,575,225, fill='white', width=2)
        if erreurs >=7:
            canvas_pendu.create_line(600,200,625,225, fill='white', width=2)

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


# #Fonction qui vérifie les lettres entrées

def verification_lettres(lettres_trouvees,lettres_fausses,nb_essais_max):
        global Lettres
        tentative = Lettres.get().lower()
        Lettres.delete(0, tk.END)
        if not tentative.isalpha() or len(tentative) != 1 :
            messagebox.showerror(title="Problème", message="Veuillez entrer qu'une seule lettre de l'alphabet")
            return

        if (tentative in lettres_trouvees) or (tentative in lettres_fausses) :
            messagebox.showwarning(title="Problème",message="Vous avez déjà entré cette lettre")
            return

        if tentative in mot_choisi :
            lettres_trouvees.append(tentative)
        else :
            lettres_fausses.append(tentative)
            print(lettres_fausses)
            dessin_pendu(len(lettres_fausses))

        mot_cache = "".join([tentative if tentative in lettres_trouvees else "*" for tentative in mot_choisi])
        affichage_mot_et_erreurs(nb_essais_max,lettres_trouvees,lettres_fausses,mot_choisi)

        if Essais_restants==0:
            messagebox.showerror(title="Partie terminée",message=f"Vous avez malheureusement perdu\nLe mot à deviner était : {mot_choisi}")

        if mot_cache == mot_choisi :
            messagebox.showinfo(title="Victoire", message=f"Bravo vous avez deviné le mot : {mot_choisi}")

        return lettres_fausses,lettres_trouvees


##########################################################################################################################
#################################################### CREATION DES PAGES
def page_accueil():
    global window
    # Création de la fenêtre principale
    window = Tk()
    window.title("JEU DU PENDU")
    window.geometry("1080x720")
    window.config(bg='#2E3440')  # Fond sombre et moderne

    # Bouton "Aide" en haut à gauche (orange)
    button_help = Button(
        window,
        text="Aide",
        font=("Helvetica", 14, "bold"),
        bg='#FFA500',  # Orange
        fg='white',
        activebackground='#FF8C00',  # Orange plus foncé au survol
        activeforeground='white',
        relief=FLAT,
        bd=0,
        padx=15,
        pady=10,
        command=open_rules
    )
    button_help.place(x=20, y=20)  # Position en haut à gauche

    # Frame principale
    frame = Frame(window, bg='#2E3440', bd=1, relief=SUNKEN)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Premier titre
    label_titre = Label(
        frame,
        text="BIENVENUE AU JEU DU PENDU",
        font=("Helvetica", 30, "bold"),
        bg='#2E3440',
        fg='#88C0D0'  # Couleur pastel pour le texte
    )
    label_titre.grid(row=0, column=0, pady=20, padx=20)

    # Label "Fait par nous"
    label_subtitre = Label(
        frame,
        text="Fait par Klervi,Mathis,Chelsea,Ali",
        font=("Helvetica", 15, "italic"),
        bg='#2E3440',
        fg='#D8DEE9'  # Texte gris clair
    )
    label_subtitre.grid(row=1, column=0, pady=10)

    # Bouton "Jouer" avec style moderne
    button_play = Button(
        frame,
        text="Jouer",
        font=("Helvetica", 20, "bold"),
        bg='#5E81AC',  # Bleu moderne
        fg='white',
        activebackground='#81A1C1',  # Bleu plus clair au survol
        activeforeground='white',
        relief=FLAT,
        bd=0,
        padx=20,
        pady=10,
        command=start_game
    )
    button_play.grid(row=2, column=0, pady=20)

    # Ajouter un effet de survol au bouton "Aide"
    def on_enter_help(e):
        button_help.config(bg='#FF8C00')  # Orange plus foncé au survol

    def on_leave_help(e):
        button_help.config(bg='#FFA500')  # Retour à l'orange d'origine

    button_help.bind("<Enter>", on_enter_help)
    button_help.bind("<Leave>", on_leave_help)

    # Ajouter un effet de survol au bouton "Jouer"
    def on_enter_play(e):
        button_play.config(bg='#81A1C1')  # Bleu plus clair au survol

    def on_leave_play(e):
        button_play.config(bg='#5E81AC')  # Retour au bleu d'origine

    button_play.bind("<Enter>", on_enter_play)
    button_play.bind("<Leave>", on_leave_play)

    # Lancer la boucle Tkinter
    window.mainloop()

def Page_jeu():
    global root2, Nb_lettres, Longueur_texte, Afficher_mot, mot_cache, Validation_nb, Validation_lettres, Nb_erreurs, Lettres, canvas_pendu, Indice 
    root2 = tk.Tk()

    root2.title("Le jeu du pendu")
    root2.geometry("1080x720")
    root2.config(bg="black")

    #Canvas pour le pendu
    canvas_pendu = tk.Canvas(root2, width=900, height=350, bg="black")
    canvas_pendu.place(x=100, y=00)

    #Choix de la longueur du mot
    Longueur_texte=tk.Label(root2,text="Choisir la longueur du mot   |   Et le nombre d'erreurs acceptées",font=("Arial",20),width=50)
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

    Indice=tk.Button(root2, text="Indice", font=("Arial",15), command= lambda : bouton_indice(mot_choisi, nb_essais_max))
    Indice.place_forget()

    Quitter = tk.Button(root2, text="Quitter la partie", font=("Arial", 15), command=bouton_quitter)
    Quitter.place(x=1, y=50)

#######################################
## PROGRAMME PRINCIPAL
if __name__ == "__main__":
    page_accueil()
