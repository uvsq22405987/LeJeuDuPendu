import tkinter as tk
from tkinter import *
import webbrowser
import random

## FONCTION POUR LA PAGE D'ACCUEIL ##
# Fonction pour ouvrir les règles du jeu
def open_rules():
    webbrowser.open_new("https://champagnole.circo39.ac-besancon.fr/wp-content/uploads/sites/9/2020/04/jeu-du-pendu.pdf")

# Fonction pour démarrer le jeu
def start_game():
    global window
    window.destroy()
    Page_jeu()


#########################################
## FONCTION POUR LA PAGE DE JEU ##
def Validation_longueur():
    global Nb_lettres, longueur
    longueur=int(Nb_lettres.get())
    Nb_lettres.place_forget()
    Validation_nb.place_forget()
    Nb_erreurs.place_forget()
    Validation_lettres.place(x=600,y=450)
    jeu()

def affichage_mot_et_erreurs():
    global mot_cache
    mot_cache = "".join([tentative if tentative in lettres_trouvees else "*" for tentative in mot_choisi])
    Afficher_mot=tk.Label(root2,text=mot_cache, font=("Arial",20),width=30)
    Afficher_mot.place(x=350,y=350)
    Afficher_erreurs_restantes=tk.Label(root2,text=("Essais restants", Essais_restants), font=("Arial",20),width=30)
    Afficher_erreurs_restantes.place(x=10,y=10)


#def Indice():

def dessin_pendu(erreurs):
        if erreurs >= 0:
            root2.create_line(500,100,500,300, fill='white', width=2)
            root2.create_line(500,100,600,100, fill='white', width=2)
        if erreurs >=1:
            root2.create_line(600,100,600,110, fill='white', width=2)
        if erreurs >=2:
            root2.create_oval(580,110,620,150, fill='white', width=2)
        if erreurs >=3:
            root2.create_line(600,150,600,200, fill='white', width=2)
        if erreurs >=4:
            root2.create_line(600,150,575,175, fill='white', width=2)
        if erreurs >=5:
            root2.create_line(600,150,625,175, fill='white', width=2)
        if erreurs >=6:
            root2.create_line(600,200,575,225, fill='white', width=2)
        if erreurs >=7:
            root2.create_line(600,200,625,225, fill='white', width=2)
#################################################


## FONCTIONS DU JEU :

def jeu():
    global mot_choisi, Longueur_texte
    choisir_mot(longueur)
    Longueur_texte.destroy()
    jeu_pendu(mot_choisi)
    affichage_mot_et_erreurs()

def choisir_mot(longueur_mot):
    global mot_choisi
    mots = {4:["loup","lots","jour","chat","aide","code"],
    5:["loupe","soupe","livre","sable","fleur","glace","neige","nuage","terre","pomme","table","chien","liste","photo"],
    6:["soleil","maison","raison","animal","moteur","projet"],
    7:["bonjour","hopital","voiture","trousse","aimable","chateau","costume","horloge","famille","bonheur","travail"],
    8:["amoureux","cartable","voyageur","magicien","patience","correcte","sagesse"],
    9:["mangouste","confusion","isolation","imprudent","solitaire","certitude","optimiste"],
    10:["silencieux","maintenant","importance","abonnement","impression"]}
    mot_choisi = random.choice(mots[longueur_mot])
    return mot_choisi

def jeu_pendu(mot_choisi) :
    global nb_erreurs, mot_cache, lettres_trouvees, Essais_restants
    lettres_trouvees = []
    lettres_fausses = []
    nb_essais_max = int(Nb_erreurs.get())
    nb_erreurs = 0
    Essais_restants=nb_essais_max-nb_erreurs

def verification_lettres():
        global nb_erreurs
        #faire une variable "Tentative" pour enregistrer la lettre saisie par l'utilisateur
        if not tentative.isalpha() or len(tentative) != 1 :
            print("veuillez entrer qu'une seule lettre de l'alphabet")

        if (tentative in lettres_trouvees) or (tentative in lettres_fausses) :
            print("vous avez déjà essayé cette lettre")

        if tentative in mot_choisi :
            lettres_trouvees.append(tentative)
            mot_cache = "".join([tentative if tentative in lettres_trouvees else "*" for tentative in mot_choisi])

        else :
            print(tentative, "vous vous êtes trompé")
            lettres_fausses.append(tentative)
            print(lettres_fausses)
            Nb_erreurs += 1
            dessin_pendu(len(lettres_fausses))
            """root.update()"""

        print(mot_cache)  ##mis à la fin, après avoir traité la lettre (la fameuse tentative), car comme ça le joueur peut voir l'avancée de son mot au fur et à mesure.
        nb_erreurs = len(lettres_fausses)

        if mot_cache == mot_choisi :
            print("c'est gagné !")

        """if mot_cache != mot_choisi :
            print("vous avez atteint le nombre maximum d'essais. Le mot à deviner était", mot_choisi)"""

#############################################

#################################################### CREATION DES CANVAS
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
    global root2, Nb_lettres, Longueur_texte, Afficher_mot, mot_cache, Validation_nb, Validation_lettres, Nb_erreurs
    root2 = tk.Tk()

    root2.title("Le jeu du pendu")
    root2.geometry("1080x720")
    root2.config(bg="black")

    #L'entrée de saisie pour les lettres
    #A faire ici

    #Choix de la longueur du mot
    Longueur_texte=tk.Label(root2,text="Choisis la longueur du mot      Et le nombre d'erreurs acceptés",font=("Arial",20),width=50)
    Longueur_texte.place(x=200,y=350)

    Nb_lettres=tk.Spinbox(root2, from_=4, to=10,font=("Arial",25),width=5)
    Nb_lettres.place(x=400,y=400)

    Nb_erreurs=tk.Spinbox(root2, from_=4, to=7,font=("Arial",25),width=5)
    Nb_erreurs.place(x=700,y=400)

    #Boutons
    Validation_nb=tk.Button(root2,text="Valider le choix",command=Validation_longueur)
    Validation_nb.place(x=550,y=450)

    Validation_lettres=tk.Button(root2,text="Valider la lettre",command=verification_lettres)
    Validation_lettres.place_forget()

    Indice=tk.Button(root2,text="Indice", font=("Arial",15))
    Indice.place(x=0,y=360)


#######################################
## PROGRAMME PRINCIPAL
if __name__ == "__main__":
    page_accueil()


root2.mainloop()