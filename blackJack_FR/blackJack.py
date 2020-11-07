import time 
import random 


def creer_jeu(): #fonction pour crée le jeu de carte
    jeu = []
    for i in ("Coeur", "¨Pique", "Trèfle", "Carreau"):
        for j in range(2,15):
            jeu.append([j,i])
    random.shuffle(jeu)
    return jeu


def rejouer():
    replay = input("Voulez-vous rejouer ? ((O)ui/(N)on)")
    replay.lower()
    if replay == "o":
        clearConsole()
        blackJack()
    else:
        print("Merci d'avoir jouer, à bientôt !")
        return exit()


def distribuer(jeu,main):
    carte = jeu.pop()
    if carte[0] == 11:
        carte[0] = "Valet"
    if carte[0] == 12:
        carte[0] = "Dame"
    if carte[0] == 13:
        carte[0] = "Roi"
    if carte[0] == 14:
        carte[0] = "As"
    main.append(carte)
    return main

def miser():
    f = open("banque.txt", "r")
    argent_total = f.read()
    f.close()
    print("Vous avez ", argent_total,"$ sur votre compte, combien souhaitez vous miser ?")
    mise = int(input("réponse:"))
    f = open("banque.txt", "w")
    print(argent_total)
    argent_total = int(argent_total) - mise
    f.write(str(argent_total))
    f.close()
    return mise


def miseUpdate(mise):
    f = open("banque.txt", "r")
    argent_total = f.read()
    f.close()
    f = open("banque.txt", "w")
    argent_total = int(int(argent_total) + mise)
    f.write(str(argent_total))
    f.close()
    return mise


def checkBlackJack(main_joueur, main_croupier):
    print("on rentre dans checkBlackJack")
    if valeurMain(main_joueur) == valeurMain(main_croupier) and valeurMain(main_joueur) == 21:
        print("Vous et le croupier avez un BLACKJACK, match nul.")
        rejouer()
    elif valeurMain(main_joueur) == 21:
        print("Félicitations ! Vous avez un BLACKJACK, vous avez gagner ")
        rejouer()
    elif valeurMain(main_croupier) == 21:
        print("Dommage, le croupier a fait un BLACKJACK...")
        rejouer()
    return 

def tirer(jeu):
    carte = jeu.pop()
    return carte


def clearConsole():
    print("Clear console :")
    for _ in range(15):
        print("\n")

def valeurMain(main):
    valeur = 0
    for i in main:
        if i[0] == "Valet" or i[0] == "Dame" or i[0] == "Roi":
            valeur += 10
        elif i[0] == "As":
            if valeur > 10:
                valeur += 1
            else:
                valeur += 11
        else:
            valeur += i[0]
    return valeur

def afficherMains(mainJoueur,mainCroupier):
    print("Voici les mains : \n")
    print("MAIN JOUEUR : ", mainJoueur, "Valeur : ", valeurMain(mainJoueur))
    print("MAIN CROUPIER : ", mainCroupier, "Valeur :", valeurMain(mainCroupier))


def scoreFin(mainJoueur, mainCroupier, mise):
    afficherMains(mainJoueur,mainCroupier)
    if valeurMain(mainJoueur) > 21:
        print("Vous avez dépassé 21 vous avez perdu..")
    elif valeurMain(mainCroupier) > 21:
        print("Le croupier a dépassé 21, vous avez gagné !")
        miseUpdate(mise*1.5)
    elif valeurMain(mainJoueur) == 21:
        print(" Vous avez un BLACK JACK !, vous avez gagné")
        miseUpdate(mise*1.5)
    elif valeurMain(mainCroupier) == 21:
        print("Le croupier a fait un BLACKJACK, vous avez perdu...")
    elif valeurMain(mainJoueur) == valeurMain(mainCroupier) <= 21:
        print("Le croupier et vous avez le même score, personne ne gagne..")
        miseUpdate(mise)
    elif valeurMain(mainJoueur) > valeurMain(mainCroupier):
        print("Félicitations ! Vous avez plus de point que le croupier, vous remportez cette manche.")
        miseUpdate(mise*1.5)
    elif valeurMain(mainJoueur) < valeurMain(mainCroupier):
        print("Dommage.. Le croupier a une meilleure main que vous.")
    
    
def blackJack():
    print(" ______________________________________")
    print("| BIENVENUE SUR LE JEU DU BLACKJACK ! |")
    print("|              (par Téva)             |")
    print("|_____________________________________|")
    reponse = ""
    jeu = [] 
    jeu = creer_jeu()
    mainJoueur = []
    mainCroupier = []
    mise = miser()
    for _ in range(2):
        mainJoueur = (distribuer(jeu,mainJoueur))
        mainCroupier = (distribuer(jeu,mainCroupier))
    checkBlackJack(mainJoueur, mainCroupier)
    while reponse != "q":
        if valeurMain(mainJoueur) > 21 or valeurMain(mainJoueur) == 21:
            scoreFin(mainJoueur, mainCroupier, mise)
            rejouer()
        elif valeurMain(mainCroupier) > 21 or valeurMain(mainCroupier) == 21:
            scoreFin(mainJoueur, mainCroupier, mise)
            rejouer()
            
        afficherMains(mainJoueur, mainCroupier)
        reponse = input("Voulez-vous (T)irer, (R)ester avec ces cartes ou bien (Q)uitter")
        reponse.lower()
        if reponse == "q":
            return 
        elif reponse == "t":
            if reponse == "t":
                mainJoueur.append(tirer(jeu)) #Le joueur tire une carte et la boucle recommence
        else: #Le joueur a fini son tour on passe maintenant au tour du croupier a
            print('elif reponse == "r"')
            while valeurMain(mainCroupier) < 17:
                    mainCroupier.append(tirer(jeu))
            scoreFin(mainJoueur, mainCroupier, mise)
            reponse = rejouer()


blackJack()