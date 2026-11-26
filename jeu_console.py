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

def jouer(self):
    tour = 0
    while not checkWin():
        
        

afficher_plateau(marelle)        