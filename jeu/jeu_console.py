from structure_marelle import Marelle


def afficher_plateau(marelle):
    p = [f"({i:02d})" if marelle.pions[i] == 0 else f" {marelle.pions[i]}  " for i in range(24)]
    print("\n" + "=" * 45)
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
    print("=" * 45 + "\n")


def saisir_case(message):
    while True:
        try:
            c = int(input(message))
            if 0 <= c <= 23:
                return c
        except ValueError:
            pass
        print("Entrée invalide.")


def joueur_du_tour():
    return 1 if marelle.tour % 2 == 0 else 2


def adversaire_de(joueur):
    return 2 if joueur == 1 else 1


def init_game():
    afficher_plateau(marelle)
    while marelle.tour < 18:
        joueur = joueur_du_tour()
        print(f"Joueur {joueur} :")
        placer_pion(joueur)
        afficher_plateau(marelle)
        marelle.tour += 1


def placer_pion(joueur):
    case = saisir_case("Où voulez-vous placer votre pion (0 à 23) : ")
    while not marelle.check_possible_init(case):
        case = saisir_case("Case non disponible, choisissez-en une autre (0 à 23) : ")
    marelle.pions[case] = joueur
    if marelle.check_alligne(case)[0]:
        afficher_plateau(marelle)
        retirer_pion(adversaire_de(joueur))


def jouer_coup(joueur):
    case_depart = saisir_case("Quel pion voulez-vous déplacer (0 à 23) : ")
    while marelle.pions[case_depart] != joueur or (
        marelle.nombre_liste_pions(joueur)[0] > 3 and marelle.is_blocked(case_depart)
    ):
        case_depart = saisir_case("Pion invalide ou bloqué, choisissez-en un autre (0 à 23) : ")

    case_arrivee = saisir_case("Dans quelle case voulez-vous jouer (0 à 23) : ")
    while not marelle.check_possible(case_depart, case_arrivee, joueur):
        case_arrivee = saisir_case("Déplacement impossible, choisissez une autre case (0 à 23) : ")

    marelle.pions[case_depart] = 0
    marelle.pions[case_arrivee] = joueur
    return case_arrivee


def retirer_pion(adversaire):
    case = saisir_case("Quel pion voulez-vous retirer à votre adversaire (0 à 23) : ")
    while marelle.pions[case] != adversaire:
        case = saisir_case("Ce n'est pas un pion adverse, choisissez-en un autre (0 à 23) : ")
    marelle.pions[case] = 0


def jouer():
    init_game()
    marelle.tour = 0
    while not marelle.check_win()[0]:
        joueur = joueur_du_tour()
        print(f"Joueur {joueur} :")
        case = jouer_coup(joueur)
        afficher_plateau(marelle)
        if marelle.check_alligne(case)[0]:
            retirer_pion(adversaire_de(joueur))
            afficher_plateau(marelle)
        marelle.tour += 1
    gagnant = marelle.check_win()[1]
    print(f"Le joueur {gagnant} a gagné !")
    rep = int(input("Voulez-vous rejouer ? (1 : Oui / 2 : Non) : "))
    if rep == 1:
        jouer()
    else:
        print("Merci d'avoir joué ! ")


marelle = Marelle()
jouer()