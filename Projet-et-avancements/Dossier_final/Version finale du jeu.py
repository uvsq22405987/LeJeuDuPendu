import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser
import random
import json
import os
from tkinter import messagebox

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

#### Fonctions pour ajouter des mots au fichier texte Liste_mots ####

fichier_mots = "Liste_mots.json"
def charger_mots(fichier): # Fonction pour charger les mots du fichier JSON
    if os.path.exists(fichier): # Vérifie si le fichier existe
        with open(fichier, "r", encoding="utf-8") as f: # Ouvre le fichier en mode lecture
            return json.load(f) # Charge le contenu du fichier JSON
    else: # Si le fichier n'existe pas, on crée un dictionnaire par défaut
        return {
            "4": ["loup", "lots", "jour", "chat", "aide", "code"],
            "5": ["loupe", "soupe", "livre", "sable", "fleur", "glace", "neige", "nuage", "terre", "pomme", "table", "chien", "liste", "photo"],
            "6": ["soleil", "maison", "raison", "animal", "moteur", "projet"],
            "7": ["bonjour", "hopital", "voiture", "trousse", "aimable", "chateau", "costume", "horloge", "famille", "bonheur", "travail"],
            "8": ["amoureux", "cartable", "voyageur", "magicien", "patience", "correcte", "sagesse"],
            "9": ["mangouste", "confusion", "isolation", "imprudent", "solitaire", "certitude", "optimiste"],
            "10": ["silencieux", "maintenant", "importance", "abonnement", "impression"]
        } # Dictionnaire par défaut

#Sauvegarde du dictionnaire dans le fichier JSON
def sauvegarder_mots(fichier, mots): # Définition de la fonction sauvegarder_mots
    with open(fichier, "w", encoding="utf-8") as f: # Ouverture du fichier en mode écriture
        json.dump(mots, f, ensure_ascii=False, indent=4) # Sauvegarde du dictionnaire dans le fichier JSON

def ajout_nouveau_mot(nouveau_mot, mots, fichier): # Fonction pour ajouter un nouveau mot au dictionnaire
    nouveau_mot = nouveau_mot.lower() # Met le mot en minuscules

    if not nouveau_mot.isalpha(): # Vérifie si le mot contient des caractères non alphabétiques
        messagebox.showerror("Erreur", "Veuillez entrer uniquement des lettres.") # Affiche un message d'erreur si le mot contient des caractères non alphabétiques
        return ## Si le mot contient des caractères non alphabétiques, on affiche un message d'erreur

    longueur = len(nouveau_mot) # Calcule la longueur du mot
    if longueur < 4 or longueur > 10: # Vérifie si la longueur du mot est entre 4 et 10 lettres
        messagebox.showerror("Erreur", "Veuillez entrer un mot entre 4 et 10 lettres.") # Affiche un message d'erreur si la longueur du mot n'est pas entre 4 et 10 lettres
        return # Si la longueur du mot n'est pas entre 4 et 10 lettres, on affiche un message d'erreur

    cle = str(longueur) # Convertit la longueur du mot en chaîne de caractères

    if nouveau_mot not in mots[cle]: # Vérifie si le mot n'est pas déjà dans la liste
        mots[cle].append(nouveau_mot) # Si le mot n'est pas déjà dans la liste, on l'ajoute
        sauvegarder_mots(fichier, mots) # Sauvegarde le dictionnaire mis à jour dans le fichier JSON
        messagebox.showinfo("Succès", f"Le mot '{nouveau_mot}' a été ajouté.") # Affiche un message de succès si le mot a été ajouté avec succès
    else: # Si le mot est déjà dans la liste, on affiche un message d'information
        messagebox.showinfo("Info", f"Le mot '{nouveau_mot}' est déjà dans le dictionnaire.") # Affiche un message d'information si le mot est déjà dans la liste

def ouvrir_popup_ajout(): # Fonction pour ouvrir la fenêtre d'ajout de mot
    global entry, popup
    popup = Toplevel(window) # Crée une nouvelle fenêtre (popup)
    popup.title("Ajouter un mot") # Titre de la fenêtre
    popup.geometry("300x150") # Dimensions de la fenêtre
    popup.config(bg='#ECEFF4') # Couleur de fond de la fenêtre

    label = Label(popup, text="Entrez un mot :", font=("Helvetica", 12), bg='#ECEFF4') # Crée un label pour le mot
    label.pack(pady=10) # Ajoute un espacement vertical

    entry = Entry(popup, font=("Helvetica", 12)) # Crée un champ de saisie pour le mot
    entry.pack(pady=5) # Ajoute un espacement vertical

    bouton_valider = Button(popup, text="Ajouter", font=("Helvetica", 12, "bold"), bg="#A3BE8C", fg="white", command=valider) # Crée un bouton pour valider l'ajout du mot
    bouton_valider.pack(pady=10) # Ajoute un espacement vertical

def valider(): # Fonction pour valider l'ajout du mot
        mot = entry.get() # Récupère le mot saisi dans le champ de saisie
        ajout_nouveau_mot(mot, mots, fichier_mots) # Appelle la fonction pour ajouter le mot au dictionnaire
        popup.destroy() # Détruit la fenêtre popup après l'ajout du mot


#Fonctions pour le tableau des scores
fichier_score="fichier_tab_score.json"
def Afficher_tableau_score():
    if not os.path.exists(fichier_score):
        messagebox.showinfo(title="Information",message="Aucun score est enregistré dans le tableau")
        return

    with open(fichier_score, "r") as score:
        scores = json.load(score)

    fenetre_scores=tk.Toplevel()
    fenetre_scores.title("Tableau des scores")

    Information=("Mot choisi", "Tentatives", "Indices Utilises", "Score")
    Tableau= ttk.Treeview(fenetre_scores, columns=Information)

    for info in Information:
        Tableau.heading(info, text=info.capitalize())
        Tableau.column(info, width=100)

    for score in scores:
        Tableau.insert("", tk.END, values=(
            score["Mot choisi"],
            score["Tentatives"],
            score["Indices Utilises"],
            score["Score"]))

    Tableau.pack(fill=tk.BOTH, expand=True)


##########################################################################################################################
#################### VARIABLE DU JEU ############################
lettres_trouvees=[]
lettres_fausses=[]
Tentatives=0
Indices_utilises=0

########################################################################################
#######################  FONCTION POUR LA PAGE DE JEU ################################
#Fonction qui valide la longueur du mots et le nombre d'essais maximum et qui enlève la visibilité de ces labels
def Validation_longueur():
    global Nb_lettres, longueur, nb_essais_max, nb_indices_restants
    longueur=int(Nb_lettres.get())
    nb_essais_max = int(Nb_erreurs.get())
    nb_indices_restants = nb_indices()
    Nb_lettres.place_forget()
    Validation_nb.place_forget()
    Nb_erreurs.place_forget()
    Validation_lettres.place(x=500,y=450)
    Indice.place(x=0,y=360)
    jeu()
    return nb_essais_max

#Fonction qui afficher le mot et le nombre erreurs

def affichage_mot_et_erreurs(nb_essais_max,lettres_trouvees,lettres_fausses,mot_choisi):
    global Essais_restants

    Essais_restants=nb_essais_max-len(lettres_fausses)
    mot_cache = "".join([tentative if tentative in lettres_trouvees else "*" for tentative in mot_choisi])

    Afficher_mot=tk.Label(root2,
                              text=mot_cache,
                              font=("Courier New", 20),
                              fg="white",
                              bg="#0e3b03",
                              width=25)
    Afficher_mot.place(x=400,y=350)

    Afficher_erreurs_restantes=tk.Label(root2,
                                        text=("Essais restants : " + str(Essais_restants)),
                                        font=("Courier New",20),
                                        fg="white",
                                        bg="#0e3b03")
                                        #width=30)
    Afficher_erreurs_restantes.place(x=10,y=10)

    Afficher_lettres_essayees=tk.Label(root2,
                               text=("Lettres essayées : " + ", ".join(lettres_fausses)),
                               font=("Courier New", 14),
                               fg="white",
                               bg="#0e3b03")
    Afficher_lettres_essayees.place(x=10,y=55)

#fonction commande du bouton indice :
mot_choisi = None

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
    else :              #au cas où je ne sais pas comment l'utilisateur parviant à entrer une longueur qui n'est pas acceptée
        indices = 0
    return indices

def bouton_indice(mot_choisi, nb_essais_max) : #mot_choisi issu de la fonction jeu(), resultat de choisir_mot(longueur) ; nb_essai issu de validation_longueur
    global lettres_trouvees, nb_indices_restants, Afficher_indices_restants, Indices_utilises

    if nb_indices_restants > 0 :
        for lettre in mot_choisi :
            if lettre not in lettres_trouvees : #rappel : lettre = variable qui contient la lettre saisie par l'utilisateur
                lettres_trouvees.append(lettre)
                break #revele qu'1 seule lettre

        affichage_mot_et_erreurs(nb_essais_max, lettres_trouvees, lettres_fausses, mot_choisi)
        nb_indices_restants = nb_indices_restants - 1
        Indices_utilises+=1

    elif nb_indices_restants == 0 :
        messagebox.showerror(title="STOP", message="Vous avez déjà utilisé le nombre maximum d'indices disponibles")
        Indice.config(state=tk.DISABLED)  # Désactive le bouton Indice

    Afficher_indices_restants=tk.Label(root2,
                               text=("Indices restants : " + str(nb_indices_restants)),
                               font=("Courier New", 14),
                               fg="white",
                               bg="#0e3b03")
    Afficher_indices_restants.place(x=10,y=100)
    return Indices_utilises

#fonction pour le bouton quitter :
def bouton_quitter(root) :
    root.destroy()

def bouton_menu_principal():
    reponse=messagebox.askyesno(title="Arrêter la partie", message="Voulez vous quitter la partie\n Et revenir au menu principal ?")
    if reponse:
        root2.destroy()
        page_accueil()

#Fonction du dessin du pendu
def dessin_pendu(erreurs, nb_essais_max):
    canvas_pendu.delete("all")
    Pendu=[
    lambda: canvas_pendu.create_line(500,100,500,300, fill='white', width=5),
    lambda:canvas_pendu.create_line(500,100,600,100, fill='white', width=2),
    lambda:canvas_pendu.create_line(600,100,600,110, fill='white', width=2),
    lambda:canvas_pendu.create_oval(580,110,620,150, outline='white', fill='white', width=2),
    lambda:canvas_pendu.create_line(600,150,600,200, fill='white', width=2),
    lambda:canvas_pendu.create_line(600,150,575,175, fill='white', width=2),
    lambda:canvas_pendu.create_line(600,150,625,175, fill='white', width=2),
    lambda:canvas_pendu.create_line(600,200,575,225, fill='white', width=2),
    lambda:canvas_pendu.create_line(600,200,625,225, fill='white', width=2)]

    dessin=round(len(Pendu) * erreurs / nb_essais_max) #correction chatgpt utilisation de round pour arrondir le nombre d'erreurs
    for i in range(dessin):
        Pendu[i]()


#####################################################################################
############################ FONCTIONS DU JEU :
#Fonction d'initialisation du jeu
def jeu():
    global mot_choisi, Longueur_texte
    mot_choisi=choisir_mot(longueur)
    Longueur_texte.destroy()
    affichage_mot_et_erreurs(nb_essais_max,lettres_trouvees,lettres_fausses,mot_choisi)
    Lettres.place(x=350,y=400)
    return

#Fonction qui choisi un mot aléatoirement en fonction de la longueur de celui ci en 'piochant' dans le fichier Liste_mots
def choisir_mot(longueur_mot):
    mot=charger_mots(fichier_mots)
    return random.choice(mot[str(longueur_mot)])


# #Fonction qui vérifie les lettres entrées

def verification_lettres(lettres_trouvees,lettres_fausses,nb_essais_max, longueur_mot,fichier_score):
        global Lettres, Tentatives
        Tentatives+=1
        Lettre_entree = Lettres.get().lower()
        Lettres.delete(0, tk.END)
        if not Lettre_entree.isalpha() or len(Lettre_entree) != 1 :
            messagebox.showerror(title="Problème", message="Veuillez entrer qu'une seule lettre de l'alphabet")
            return

        if (Lettre_entree in lettres_trouvees) or (Lettre_entree in lettres_fausses) :
            messagebox.showwarning(title="Problème",message="Vous avez déjà entré cette lettre")
            return

        if Lettre_entree in mot_choisi :
            lettres_trouvees.append(Lettre_entree)
        else :
            lettres_fausses.append(Lettre_entree)
            print(lettres_fausses)
            dessin_pendu(len(lettres_fausses), nb_essais_max)

        mot_cache = "".join([Lettre_entree if Lettre_entree in lettres_trouvees else "*" for Lettre_entree in mot_choisi])
        affichage_mot_et_erreurs(nb_essais_max,lettres_trouvees,lettres_fausses,mot_choisi)

        if Essais_restants==0:
            messagebox.showerror(title="Partie terminée",message=f"Vous avez malheureusement perdu\nLe mot à deviner était : {mot_choisi}")
            afficher_fenetre_fin()

        if mot_cache == mot_choisi :
            messagebox.showinfo(title="Victoire", message=f"Bravo vous avez deviné le mot : {mot_choisi}")
            sauvegarder_score(fichier_score,mot_choisi,Tentatives,Indices_utilises,longueur)
            afficher_fenetre_fin()

        return lettres_fausses,lettres_trouvees

#Calcul des scores
def calculer_score(longueur_mot, tentatives, indices_utilises): # Fonction pour calculer le score
    # Points de base selon la longueur du mot
    points_base = longueur_mot * 4  # 4 points de base pour chaque lettre du mot
    points_reduction = 0 # Initialisation des points de réduction

    # Réduction des points pour les indices utilisés
    points_reduction += indices_utilises * 2  # -2 points par indice utilisé

    # Réduction des points en fonction du nombre de tentatives
    if tentatives > longueur_mot: # Si le nombre de tentatives est supérieur à 1
        points_reduction += (tentatives - 1) * 1  # -1 point pour chaque tentative après la première

    # Calcul final du score
    score_final = points_base - points_reduction # Score final = points de base - points de réduction

    # On ne veut pas de score négatif, donc si le score devient négatif, on le met à 0
    if score_final < 0: # Si le score final est inférieur à 0
        score_final = 0 # Si le score final est inférieur à 0, on le met à 0

    return score_final # Retourne le score final calculé

#Sauvegarde du score après une partie gagnée
def sauvegarder_score(fichier_tab_score,mot_choisi,tentatives,indices_utilises,longueur):
    score=calculer_score(longueur,tentatives,indices_utilises)
    nouveau_score={
    "Mot choisi": mot_choisi,
    "Tentatives" : tentatives,
    "Indices Utilises": indices_utilises,
    "Score" : score}

    if os.path.exists(fichier_score):
        with open(fichier_tab_score, "r") as score:
            score_existant = json.load(score)
    else:
        score_existant = []

    score_existant.append(nouveau_score)
    with open(fichier_score, "w") as score:
        json.dump(score_existant, score, indent=4)


##########################################################################################################################
#################################################### CREATION DES PAGES
def page_accueil():
    global window, mots
    mots = charger_mots(fichier_mots)
    # Création de la fenêtre principale
    window = Tk()
    window.title("JEU DU PENDU")
    window.geometry("1080x720")
    window.config(bg='#2E3440')  # Fond sombre et moderne
    window.attributes('-fullscreen', True)

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

#Bouton quitter
    bouton_quitter_a = Button(window,
        text="Quitter",
        font=("Helvetica", 14, "bold"),
        bg='#B22222',
        fg='white',
        activebackground='#FF0000',  
        activeforeground='white',
        relief=FLAT,
        bd=0,
        padx=15,
        pady=10,
        command= lambda :bouton_quitter(window)
    )
    bouton_quitter_a.place(x=1150, y=20)

#Bouton pour le tableau des scores
    bouton_score= Button(window,
        text="Tableau des scores",
        font=("Helvetica", 14, "bold"),
        bg='#FFFF00', 
        fg='white',
        activebackground='#FFD700',
        activeforeground='white',
        relief=FLAT,
        bd=0,
        padx=15,
        pady=10,
        command=Afficher_tableau_score)
    bouton_score.place(x=20, y=500)

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

    # Bouton "Ajouter un mot" en bas à droite
    button_add_word = Button(
        window,
        text="Ajouter un mot",
        font=("Helvetica", 12, "bold"),
        bg="#A3BE8C",
        fg="white",
        activebackground="#8FBC8F",
        activeforeground="white",
        relief=FLAT,
        bd=0,
        padx=10,
        pady=5,
        command=ouvrir_popup_ajout
    ) # Crée un bouton pour ouvrir la fenêtre d'ajout de mot
    button_add_word.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20) # Place le bouton en bas à droite de la fenêtre


    # Effets de survol
    button_help.bind("<Enter>", lambda e: button_help.config(bg='#FF8C00')) # Change la couleur de fond du bouton Aide au survol
    button_help.bind("<Leave>", lambda e: button_help.config(bg='#FFA500')) # Restaure la couleur de fond d'origine du bouton Aide

    button_play.bind("<Enter>", lambda e: button_play.config(bg='#81A1C1')) # Change la couleur de fond du bouton Jouer au survol
    button_play.bind("<Leave>", lambda e: button_play.config(bg='#5E81AC')) # Restaure la couleur de fond d'origine du bouton Jouer

    button_add_word.bind("<Enter>", lambda e: button_add_word.config(bg='#8FBC8F')) # Change la couleur de fond du bouton Ajouter un mot au survol
    button_add_word.bind("<Leave>", lambda e: button_add_word.config(bg='#A3BE8C')) # Restaure la couleur de fond d'origine du bouton Ajouter un mot

    bouton_quitter_a.bind("<Enter>", lambda e: bouton_quitter_a.config(bg='#B22222'))  # Change la couleur de fond du bouton Quitter au survol
    bouton_quitter_a.bind("<Leave>", lambda e: bouton_quitter_a.config(bg='#FF0000'))  # Restaure la couleur de fond d'origine du bouton Quitter

    bouton_score.bind("<Enter>", lambda e: bouton_score.config(bg='#FFD700'))  # Change la couleur de fond du bouton Tableau des scores au survol
    bouton_score.bind("<Leave>", lambda e: bouton_score.config(bg='#FFFF00'))  # Restaure la couleur de fond d'origine du bouton Tableau des scores


    # Lancer la boucle Tkinter
    window.mainloop()

def Page_jeu():
    global root2, Nb_lettres, Longueur_texte, Validation_nb, Validation_lettres, Nb_erreurs, Lettres, canvas_pendu, Indice
    lettres_trouvees.clear()
    lettres_fausses.clear()
    Tentatives=0
    root2 = tk.Tk()

    root2.title("Le jeu du pendu")
    root2.geometry("1080x720")
    root2.config(bg="#0e3b03")
    root2.attributes('-fullscreen', True)

    #Canvas pour le pendu
    canvas_pendu = tk.Canvas(root2,
                             width=900,
                             height=350,
                             bg="#0e3b03",
                             highlightthickness=0)
    canvas_pendu.place(x=100, y=0)

    #Choix de la longueur du mot
    Longueur_texte=tk.Label(root2,
                              text="Choisir la longueur du mot   |   Et le nombre d'erreurs acceptées",
                              font=("Courier New", 20),
                              fg="white", bg="#0e3b03",
                              )
    Longueur_texte.place(x=150,y=350)

    #Spinbox
    Nb_lettres=tk.Spinbox(root2,
                          from_=4, to=10,
                          font=("Comic Sans MS", 25),
                          bg="#0e3b03",
                          width=5)
    Nb_lettres.place(x=300,y=400)

    Nb_erreurs=tk.Spinbox(root2,
                          from_=4, to=7,
                          font=("Comic Sans MS",25),
                          bg="#0e3b03",
                          width=5)
    Nb_erreurs.place(x=800,y=400)

    #Saisie des lettres
    Lettres=tk.Entry(root2,
                    width=25,
                    font=("Courier New",25),
                    bg="#0e3b03",
                    fg="white")

    #Boutons
    Validation_nb=tk.Button(root2,
                              text="Valider le choix",
                              command=Validation_longueur,
                              font=("Courier New", 14),
                              bg="#26880e",
                              fg="white",
                              activebackground="white")
    Validation_nb.place(x=525,y=475)

    Validation_lettres=tk.Button(root2,
                              text="Valider la lettre",
                              command=lambda: verification_lettres(lettres_trouvees,lettres_fausses,nb_essais_max, longueur,fichier_score),
                              font=("Courier New", 14),
                              bg="#26880e", fg="white",
                              activebackground="white")
    Validation_lettres.place_forget()

    Indice=tk.Button(root2,
                     text="Indice",
                     command= lambda : bouton_indice(mot_choisi, nb_essais_max),
                     font=("Courier New", 14),
                     bg="#26880e", fg="white")
    Indice.place_forget()

#Fonctions pour quitter la partie en cours quitter ou menu principal
    Quitter = tk.Button(root2,
                               text="Quitter",
                               command= lambda : bouton_quitter(root2),
                               font=("Courier New", 14),
                               bg="#26880e", fg="white")
    Quitter.place(x=1070, y=25)

    Menu_principal = tk.Button(root2,
                               text="Menu Principal",
                               command= bouton_menu_principal,
                               font=("Courier New", 14),
                               bg="#26880e", fg="white")
    Menu_principal.place(x=1070, y=75)

#Fonction pour la fin de jeu
def afficher_fenetre_fin():
    def rejouer():
        fenetre_fin.destroy()
        root2.destroy()
        Page_jeu()  # Relance une nouvelle partie

    def quitter():
        fenetre_fin.destroy()
        root2.destroy()

    def menu_principal():
            fenetre_fin.destroy()
            root2.destroy()
            page_accueil()   

    fenetre_fin = tk.Tk()
    fenetre_fin.title("Fin de la partie")
    fenetre_fin.geometry("400x300")
    fenetre_fin.resizable(False, False)

    label = tk.Label(fenetre_fin, text="Que voulez-vous faire ?", font=("Arial", 12))
    label.pack(pady=20)

    bouton_rejouer = tk.Button(fenetre_fin, text="Rejouer une partie", width=20, command=rejouer)
    bouton_rejouer.pack(pady=5)

    bouton_menu_principal = tk.Button(fenetre_fin, text="Menu principal", width=20, command=menu_principal)
    bouton_menu_principal.pack(pady=5)

    bouton_quitter = tk.Button(fenetre_fin, text="Quitter le jeu", width=20, command=quitter)
    bouton_quitter.pack(pady=5)

    fenetre_fin.mainloop()

#######################################
## PROGRAMME PRINCIPAL
if __name__ == "__main__":
    page_accueil()