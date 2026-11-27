class Marelle:
    def __init__(self):
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
        self.adj = {
            0: [1, 7], 1: [0, 2, 9], 2: [1, 3], 3: [2, 4, 11],
            4: [3, 5], 5: [4, 6, 13], 6: [5, 7], 7: [6, 0, 15],
            8: [9, 15], 9: [8, 10, 1, 17], 10: [9, 11], 11: [10, 12, 3, 19],
            12: [11, 13], 13: [12, 14, 5, 21], 14: [13, 15], 15: [14, 8, 7, 23],
            16: [17, 23], 17: [16, 18, 9], 18: [17, 19], 19: [18, 20, 11],
            20: [19, 21], 21: [20, 22, 13], 22: [21, 23], 23: [22, 16, 15]
        }

        self.pions = [0]*24
        self.tour = 0

    def check_possible(self, case_dep, case_arr, joueur):
        if self.nombre_liste_pions(joueur)[0] > 3:
            return self.pions[case_arr] == 0
        else:
            return self.pions[case_arr] == 0 and case_arr in self.adj[case_dep]

    def check_possible_init(self, case):
        return self.pions[case] == 0
    
    def nombre_liste_pions(self, joueur):
        assert joueur in [1, 2], "Joueur doit etre soit 1 ou 2"
        n = 0
        l = []
        for i in range(len(self.pions)):
            if self.pions[i] == joueur:
                n += 1
                l.append(i)
        return n, l

    def check_win(self):
        win = False
        winner = None
        other_player = {1: 2, 2: 1}
        for joueur in [1, 2]:
            if self.nombre_liste_pions(joueur)[0] == 2:
                win = True
                winner = other_player[joueur]

        if not win:
            for joueur in [1, 2]:
                blocked = True
                n, l_cases = self.nombre_liste_pions(joueur)
                if n > 3 :
                    for case_dep in l_cases:
                        for case_arr in self.adj[case_dep]:
                            if self.pions[case_arr] == 0:
                                blocked = False

                    if blocked:
                        win = True
                        winner = other_player[joueur]

        return win, winner

    def check_alligne(self, last_move):
        for a, b, c in self.moulins:
            if last_move in [a, b, c]:
                if self.pions[a] == self.pions[b] == self.pions[c] and self.pions[a] != 0:
                    return True, self.pions[a]
        return False, None

    def is_blocked(self, case):
        blocked = True
        for case_arr in self.adj[case]:
            if self.pions[case_arr] == 0:
                blocked = False
        return blocked

    def enregistrer_console(self):
        lignes = [
            self.moulins,
            self.adj,
            self.pions,
            self.tour
        ]
        nom_fichier = input("Vous voulez enregistrer la partie sous quel nom ?")

        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            fichier.writelines(lignes)

        