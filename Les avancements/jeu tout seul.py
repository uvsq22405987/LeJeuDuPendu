## FONCTIONS DU JEU :

import random


longueur_mot = int(input("Choisir la longueur du mots entre 4 et 10"))

def choisir_mot(longueur_mot):
    mots = {4:["loup","lots","jour","chat","aide","code"],
    5:["loupe","soupe","livre","sable","fleur","glace","neige","nuage","terre","pomme","table","chien","liste","photo"],
    6:["soleil","maison","raison","animal","moteur","projet"],
    7:["bonjour","hopital","voiture","trousse","aimable","chateau","costume","horloge","famille","bonheur","travail"],
    8:["amoureux","cartable","voyageur","magicien","patience","correcte","sagesse"],
    9:["mangouste","confusion","isolation","imprudent","solitaire","certitude","optimiste"],
    10:["silencieux","maintenant","importance","abonnement","impression"]}
    
    global mot_choisi
    mot_choisi = random.choice(mots[longueur_mot])
    return mot_choisi


def jeu_pendu(mot_choisi) :
    
    mot_cache = "*" * len(mot_choisi) 
    lettres_trouvees = []
    lettres_fausses = []
    nb_essais_max = 7 ##car à 8 le bonhomme est déjà pendu et le jeu est donc perdu.
    nb_essais = 0
    
    while nb_essais < nb_essais_max : 
        
        tentative = input("saisir une lettre").lower() ##est ce vraiment nécessaire le .lower() (-> apparamment oui mais j'ai pas compris pourquoi donc je le laisse comme vous l'aviez mis)
        
        if not tentative.isalpha() or len(tentative) != 1 :  ## -> idée de chat gpt : vérifier que le joueur a bien rentré une lettre de l'alphabet et pas un autre caractère, et qu'il en a bien rentré qu'une seule.
            print("veuillez entrer qu'une seule lettre de l'alphabet")
            continue   #continue = stop, recommence la boucle

        if (tentative in lettres_trouvees) or (tentative in lettres_fausses) :
            print("vous avez déjà essayé cette lettre")
            continue  
        
        if tentative in mot_choisi :
            lettres_trouvees.append(tentative)
            mot_cache = "".join([tentative if tentative in lettres_trouvees else "*" for tentative in mot_choisi])

        else :
            print(tentative, "vous vous êtes trompé")
            lettres_fausses.append(tentative)
            print(lettres_fausses)  ##c'est mieux d'afficher les tentatives fausses du joueur comme ça ça lui évite de les retester (et j'ai créé au dessus une condition au cas où il le ferait quand même)
            nb_essais += 1
            #print(dessin_pendu(len(lettres_fausses))) 
            #root.update()  ##pour mettre à jour l'interface graphique
        
        print(mot_cache)  ##mis à la fin, après avoir traité la lettre (la fameuse tentative), car comme ça le joueur peut voir l'avancée de son mot au fur et à mesure.
        
        global erreurs ##création de la variable erreur en mode global pour qu'elle soit utilisable dans l'interface graphique
        erreurs = len(lettres_fausses)            ##finalement je sais pas trop si cette variable est utile (je pense qu'on peut la supprimer)

        if mot_cache == mot_choisi :
            print("c'est gagné !")
            break

    if mot_cache != mot_choisi :    
        print("vous avez atteint le nombre maximum d'essais. Le mot à deviner était", mot_choisi)


choisir_mot(longueur_mot)
jeu_pendu(mot_choisi)
#dessin_pendu(erreurs)
#affiche_mot(longueur_mot)

