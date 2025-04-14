#Les deux spinbox pour le choix de la longueur et du nombres d'erreurs
#Choix de la longueur du mot
Longueur_texte=tk.Label(root2,text="Choisis la longueur du mot      Et le nombre d'erreurs acceptés",font=("Arial",20),width=50)
Longueur_texte.place(x=200,y=350)

Nb_lettres=tk.Spinbox(root2, from_=4, to=10,font=("Arial",25),width=5)
Nb_lettres.place(x=400,y=400)

Nb_erreurs=tk.Spinbox(root2, from_=4, to=7,font=("Arial",25),width=5)
Nb_erreurs.place(x=700,y=400)