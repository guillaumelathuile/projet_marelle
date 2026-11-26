from structure_marelle import Marelle

def afficher_plateau(self):
    p = [f"{self.plateau[i]}({i:02d})" if self.plateau[i] == '.' else f" {self.plateau[i]}  " for i in range(24)]
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

def jouer_coup(joueur):
    case = int(input("Dans quelle case voulez-vous jouer (0 à 23) : "))
    while not check_possible(case_depart,case_arrivee):
        case = int(input("Dans quelle case voulez-vous jouer (0 à 23) : "))
    if(joueur == 1):
        marelle.pions[case] = 1
    else:
        marelle.pions[case] = 2
    return case

def retirer_pion(adversaire):
    case = int(input("Quelle pion voulez-vous retirer à votre adversaire (0 à 23) : "))
    if(marelle.pions[case] == adversaire):
        marelle.pions[case] = 0
        

def jouer():
    tour = 0
    while not check_win()[0]:
        if(tour%2 == 0):
            joueur = 1
        else:
            joueur = 2
        case = jouer_coup(joueur)
        if check_alligne(case):
            if (joueur == 1):
                retirer_pion(2)
            else:
                retirer_pion(1)
        tour += 1
        
marelle = Marelle()
afficher_plateau(marelle)  