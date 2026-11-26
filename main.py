class JeuDeLaMarelle:
    def __init__(self):
        # 24 intersections vides ('.'), 'X' pour Joueur 1, 'O' pour Joueur 2
        self.plateau = ['.'] * 24
        self.joueurs = ['X', 'O']
        self.tour = 0
        self.pions_a_poser = {'X': 9, 'O': 9}
        self.pions_sur_plateau = {'X': 0, 'O': 0}

        # Liste des 16 moulins possibles (alignements de 3)
        self.moulins = [
            # Carré extérieur
            (0, 1, 2), (2, 3, 4), (4, 5, 6), (6, 7, 0),
            # Carré moyen
            (8, 9, 10), (10, 11, 12), (12, 13, 14), (14, 15, 8),
            # Carré intérieur
            (16, 17, 18), (18, 19, 20), (20, 21, 22), (22, 23, 16),
            # Lignes transversales
            (1, 9, 17), (3, 11, 19), (5, 13, 21), (7, 15, 23)
        ]

        # Graphe des connexions (cases adjacentes pour les déplacements)
        self.voisins = {
            0: [1, 7], 1: [0, 2, 9], 2: [1, 3], 3: [2, 4, 11],
            4: [3, 5], 5: [4, 6, 13], 6: [5, 7], 7: [6, 0, 15],
            8: [9, 15], 9: [8, 10, 1, 17], 10: [9, 11], 11: [10, 12, 3, 19],
            12: [11, 13], 13: [12, 14, 5, 21], 14: [13, 15], 15: [14, 8, 7, 23],
            16: [17, 23], 17: [16, 18, 9], 18: [17, 19], 19: [18, 20, 11],
            20: [19, 21], 21: [20, 22, 13], 22: [21, 23], 23: [22, 16, 15]
        }

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

    def forme_moulin(self, position, joueur):
        """Vérifie si la position fait partie d'un moulin pour le joueur."""
        for m in self.moulins:
            if position in m:
                if all(self.plateau[i] == joueur for i in m):
                    return True
        return False

    def capturer_pion(self, joueur_actif):
        """Permet de retirer un pion adverse."""
        adversaire = 'O' if joueur_actif == 'X' else 'X'
        print(f"MOULIN ! Joueur {joueur_actif}, choisissez un pion '{adversaire}' à retirer.")

        # Vérifier si tous les pions adverses sont dans des moulins
        pions_adverses = [i for i, val in enumerate(self.plateau) if val == adversaire]
        tous_dans_moulin = all(self.forme_moulin(pos, adversaire) for pos in pions_adverses)

        while True:
            try:
                cible = int(input(f"Numéro de la case du pion '{adversaire}' à capturer : "))
                if cible not in pions_adverses:
                    print("Cette case ne contient pas un pion adverse.")
                elif not tous_dans_moulin and self.forme_moulin(cible, adversaire):
                    print("Impossible de retirer un pion faisant partie d'un moulin (d'autres pions sont libres).")
                else:
                    self.plateau[cible] = '.'
                    self.pions_sur_plateau[adversaire] -= 1
                    print(f"Pion en {cible} capturé !")
                    break
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def a_des_mouvements(self, joueur):
        """Vérifie si le joueur peut encore bouger."""
        if self.pions_a_poser[joueur] > 0 or self.pions_sur_plateau[joueur] == 3:
            return True
        for i, val in enumerate(self.plateau):
            if val == joueur:
                if any(self.plateau[v] == '.' for v in self.voisins[i]):
                    return True
        return False

    def jouer(self):
        while True:
            joueur = self.joueurs[self.tour % 2]
            self.afficher_plateau()

            # Vérification de défaite avant de jouer
            if self.pions_a_poser[joueur] == 0:
                if self.pions_sur_plateau[joueur] < 3:
                    gagnant = 'O' if joueur == 'X' else 'X'
                    print(f"Fin de partie ! Joueur {joueur} a moins de 3 pions. Victoire de {gagnant} !")
                    break
                if not self.a_des_mouvements(joueur):
                    gagnant = 'O' if joueur == 'X' else 'X'
                    print(f"Fin de partie ! Joueur {joueur} est bloqué. Victoire de {gagnant} !")
                    break

            print(f"--- Tour du Joueur {joueur} ---")

            # PHASE 1 : Pose des pions
            if self.pions_a_poser[joueur] > 0:
                print(f"Phase de pose (Pions restants à poser : {self.pions_a_poser[joueur]})")
                while True:
                    try:
                        pos = int(input("Choisissez une case libre (0-23) : "))
                        if 0 <= pos <= 23 and self.plateau[pos] == '.':
                            self.plateau[pos] = joueur
                            self.pions_a_poser[joueur] -= 1
                            self.pions_sur_plateau[joueur] += 1
                            if self.forme_moulin(pos, joueur):
                                self.afficher_plateau()
                                self.capturer_pion(joueur)
                            break
                        else:
                            print("Case invalide ou déjà occupée.")
                    except ValueError:
                        print("Veuillez entrer un nombre entre 0 et 23.")

            # PHASE 2 & 3 : Déplacement (et saut si 3 pions)
            else:
                mode_saut = (self.pions_sur_plateau[joueur] == 3)
                print("Phase de déplacement" + (" (MODE SAUT ACTIVÉ : vous pouvez aller sur n'importe quelle case libre !)" if mode_saut else ""))
                while True:
                    try:
                        depart = int(input("Case du pion à déplacer : "))
                        if not (0 <= depart <= 23) or self.plateau[depart] != joueur:
                            print("Vous devez sélectionner l'un de vos pions.")
                            continue
                        
                        arrivee = int(input("Case de destination : "))
                        if not (0 <= arrivee <= 23) or self.plateau[arrivee] != '.':
                            print("La case de destination doit être libre.")
                            continue

                        if not mode_saut and arrivee not in self.voisins[depart]:
                            print("Déplacement invalide : la case n'est pas adjacente.")
                            continue

                        # Exécution du mouvement
                        self.plateau[depart] = '.'
                        self.plateau[arrivee] = joueur
                        if self.forme_moulin(arrivee, joueur):
                            self.afficher_plateau()
                            self.capturer_pion(joueur)
                        break
                    except ValueError:
                        print("Veuillez entrer des numéros de case valides.")

            self.tour += 1

if __name__ == "__main__":
    jeu = JeuDeLaMarelle()
    jeu.jouer()