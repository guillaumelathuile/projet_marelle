from structure_marelle import Marelle

def afficher_plateau(marelle):
    p = [f"{marelle.pions[i]}({i:02d})" if marelle.pions[i] == '.' else f" {marelle.pions[i]}  " for i in range(24)]
    print("\n" + "="*45)
    print(f"{p[0]} ---------- {p[1]} ---------- {p[2]}")
    print("|                 |                 |")
    print(f"|   {p[8]} ------ {p[9]} ------ {p[10]}   |")
    print("|   |             |             |   |")
    print(f"|   |   {p[16]} -- {p[17]} -- {p[18]}   |   |")
    print("|   |   |                   |   |   |")
    print(f"{p[7]}-{p[15]}-{p[23]}               {p[19]}-{p[11]}-{p[3]}")
    print("|   |   |                   |   |   |")
    print(f"|   |   {p[22]} -- {p[21]} -- {p[20]}   |   |")
    print("|   |             |             |   |")
    print(f"|   {p[14]} ------ {p[13]} ------ {p[12]}   |")
    print("|                 |                 |")
    print(f"{p[6]} ---------- {p[5]} ---------- {p[4]}")
    print("="*45 + "\n")


def init_game():
    afficher_plateau(marelle)  
    tour = 0
    while not tour == 18:
        if tour%2 == 0:
            joueur = 1
        else:
            joueur = 2
        placer_pion(joueur)
        afficher_plateau(marelle)
        tour += 1
        
def placer_pion(joueur):
    case = int(input("Ou voulez-vous placer votre pion (0 à 23) : "))
    while not marelle.check_possible_init(case):
        case = int(input("Case non disponible, choisissez-en une autre (0 à 23) : "))
    marelle.pions[case] = joueur
    if marelle.check_alligne(case):
            if (joueur == 1):
                retirer_pion(2)
            else:
                retirer_pion(1)

def jouer_coup(joueur):
    case_depart = int(input("Quelle pion voulez-vous déplacer (0 à 23) : "))
    while marelle.is_blocked(case_depart):
        case_depart = int(input("Pion bloqué, choisissez-en un autre(0 à 23) : "))
    case_arrivee = int(input("Dans quelle case voulez-vous jouer (0 à 23) : "))
    while not marelle.check_possible(case_depart,case_arrivee, joueur):
        case = int(input("Déplacement impossible, choisissez une autre case (0 à 23) : "))
    if(joueur == 1):
        marelle.pions[case] = 1
    else:
        marelle.pions[case] = 2
    return case

def retirer_pion(adversaire):
    case = int(input("Quelle pion voulez-vous retirer à votre adversaire (0 à 23) : "))
    while not (marelle.pions[case] == adversaire):
        case = int(input("Ce n'est pas un pion adversaire, choisissez-en un autre (0 à 23) : "))
    marelle.pions[case] = 0
        

def jouer():
    init_game()
    tour = 0
    while not marelle.check_win(marelle)[0]:
        if(tour%2 == 0):
            joueur = 1
        else:
            joueur = 2
        case = jouer_coup(joueur)
        if Marelle.check_alligne(case):
            if (joueur == 1):
                retirer_pion(2)
            else:
                retirer_pion(1)
        afficher_plateau(marelle)
        tour += 1
        
marelle = Marelle()
jouer()