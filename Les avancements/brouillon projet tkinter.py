import tkinter as tk



################################################################################




root=tk.Tk()

root.geometry("600x100")   #définition de la taille de la fenêtre dans laquelle on va rentrer la longueur souhaitée du mot

valeur_saisie=tk.StringVar()   #stringvar = type d'objet propre à tkinter : il s'agit d'un str variable


def bouton_ok():    #programmation du bouton ok : bouton qui valide 

    valeur_str=valeur_saisie.get()  #je nomme valeur_str (str car c'est une str, c'etait pour mieux m'y retrouver) la valeur que je récupère de la variable valeur saisie (grâce au .get())
    
    print("La valeur est : " + valeur_str)   #pour afficher (dans le terminal) la valeur saisie dans le champ de saisie de la fenêtre (c'etait juste un test, pas utile)
    valeur_int = int(valeur_str)      #je convertis en objet de type entier ma valeur rentrée dans le champ de saisie (qui était donc un str)

    ##########################################

    root2 = tk.Tk()    #création d'une 2e fenêtre 
    
    bienvenue = tk.Label(root2, text="à vous de jouer !", font=("helvetica", "25"))  #dans cette 2e fenêtre je choisi d'afficher un message indiquant le début du jeu : c'est là qu'il y aura le dessin du pendu
    bienvenue.grid(column=2, row=0)  #placement du texte créé dans la fenêtre
    
    label = tk.Label(root2, text=(valeur_int * "*"), font=("helvetica", "20")) #création de l'affichage des *
    label.grid(column=20, row=20)  #placement des *

    root2.mainloop() 
    
    
valeur_label = tk.Label(root, text = 'Choisir la longueur du mot (entre 4 et 10 lettres maximum) :', font=('helvetica',10, 'bold')) #dans la fenêtre 2, création du texte qui demande à l'utilisateur de choisir la longueur... (texte en gras)   
 

valeur_entry = tk.Entry(root,textvariable = valeur_saisie, font=('helvetica',10))  #création du widget Entry : widget pour que l'utilisateur entre le nb de lettres de son mot
 

bouton=tk.Button(root,text = 'Valider', command = bouton_ok)  #création du widget bouton ok
 

valeur_label.grid(row=0,column=0)  #placement des 3 widget que l'on vient de créer
valeur_entry.grid(row=0,column=1)
bouton.grid(row=2,column=1)




#########################################################################################

root.mainloop()