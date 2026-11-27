import asyncio
import pygame
from structure_marelle import Marelle


def dessiner_pion(screen, image, index_point):
    x, y = points[index_point]
    rect = image.get_rect(center=(x, y))
    screen.blit(image, rect)

def joueur_du_tour():
    return 1 if marelle.tour % 2 == 0 else 2

def joueur_oppose(joueur):
    other_player = {1: 2, 2: 1}
    return other_player[joueur]

def placer_pion(case_arr, case_dep=None):
    joueur = joueur_du_tour()
    coup_joue = None
    if marelle.tour < 18:
        if marelle.check_possible_init(case_arr):
            marelle.pions[case_arr] = joueur
            marelle.tour += 1
            coup_joue = case_arr
    else:
        if marelle.check_possible(case_dep, case_arr, joueur):
            print(case_dep, case_arr, marelle.adj[case_dep])
            marelle.pions[case_dep] = 0
            marelle.pions[case_arr] = joueur
            marelle.tour += 1
            coup_joue = case_arr
    return coup_joue





def afficher_texte_style(screen, texte, x, y, taille=28,
                         couleur=(245, 245, 245),
                         ombre=(0, 0, 0),
                         police="georgia",
                         gras=True,
                         centre=False,
                         largeur_max=500,
                         espacement=8):

    font = pygame.font.SysFont(police, taille, bold=gras)

    # Découpage du texte en mots
    mots = texte.split(" ")
    lignes = []
    ligne_actuelle = ""

    for mot in mots:

        test = ligne_actuelle + " " + mot if ligne_actuelle else mot

        # Vérifie si la ligne dépasse la largeur maximale
        if font.size(test)[0] <= largeur_max:
            ligne_actuelle = test

        else:
            if ligne_actuelle:
                lignes.append(ligne_actuelle)

            ligne_actuelle = mot

    if ligne_actuelle:
        lignes.append(ligne_actuelle)

    # Affichage de chaque ligne
    hauteur_ligne = font.get_height() + espacement

    for i, ligne in enumerate(lignes):

        texte_ombre = font.render(ligne, True, ombre)
        texte_surface = font.render(ligne, True, couleur)

        rect = texte_surface.get_rect()

        if centre:
            rect.center = (x, y + i * hauteur_ligne)
        else:
            rect.topleft = (x, y + i * hauteur_ligne)

        # Ombre portée
        screen.blit(texte_ombre, (rect.x + 2, rect.y + 3))

        # Texte principal
        screen.blit(texte_surface, rect)

    return len(lignes) * hauteur_ligne



pygame.init()
<<<<<<< HEAD
WIDTH, HEIGHT = 800, 800
=======
WIDTH, HEIGHT = 1400, 800
ROWS = 6
MARGIN = 24
GAP = 7
GRID_TOP = 155
>>>>>>> f6363ff (fin interface)

BG = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Chemins relatifs : les images doivent être dans le même dossier que main.py (jeu/)
fond = pygame.image.load("marelle_jungle.png").convert()
pion_j1 = pygame.image.load("pion_blanc.png").convert_alpha()
pion_j2 = pygame.image.load("pion_noir.png").convert_alpha()

pygame.display.set_caption("Marelle")
clock = pygame.time.Clock()

# SysFont ne marche pas sur le web : police par défaut de pygame
TITLE_FONT = pygame.font.Font(None, 54)
INFO_FONT = pygame.font.Font(None, 28)
SMALL_FONT = pygame.font.Font(None, 22)

C = 400
tolerance = 20

points = []
for r in (330, 220, 110):  # carré extérieur, milieu, intérieur
    for dx, dy in [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]:
        points.append((C + dx*r, C + dy*r))

marelle = Marelle()

pion_selected = False
pion_selected_val = None
last_move = None
joueur_qui_alligne = None
alligne = False
win = False
texte = f"Supprimez un pion de votre adversaire, tour du joueur {joueur_du_tour()}"

<<<<<<< HEAD
async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, (px, py) in enumerate(points):
                    if px - tolerance <= x <= px + tolerance and py - tolerance <= y <= py + tolerance:
                        marelle.pions[i] = 1

        screen.fill(BG)
        screen.blit(fond, (0, 0))
        for i in marelle.nombre_liste_pions(1)[1]:
            dessiner_pion(screen, pion_j1, i)
        for i in marelle.nombre_liste_pions(2)[1]:
            dessiner_pion(screen, pion_j2, i)

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)  # obligatoire pour pygbag

    pygame.quit()


asyncio.run(main())
=======
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            i = 0
            
            for r in (330, 220, 110):  # carré extérieur, milieu, intérieur
                for dx, dy in [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]:
                    px = C + dx*r
                    py =  C + dy*r

                    if px -tolerance <= x <= px + tolerance and py -tolerance <= y <= py + tolerance and not win:
                        temp = None
                        if alligne:
                            texte = f"Supprimez un pion de votre adversaire, tour du joueur {joueur_du_tour()}"
                            if marelle.pions[i] == joueur_oppose(joueur_qui_alligne):
                                marelle.pions[i] = 0
                                alligne = False

                        elif marelle.tour < 18:
                            temp = placer_pion(i)
                            if temp is not None:
                                last_move = temp
                            texte = f"Début de partie, placez tous vos pions sur la grille, tour du joueur {joueur_du_tour()}"
                        else:
                            if pion_selected:
                                texte = f"Choisissez l'endroit de dépose, tour du joueur {joueur_du_tour()}"                                
                                temp = placer_pion(i, pion_selected_val)
                                if temp is not None:
                                    last_move = temp
                                pion_selected = False
                            else:
                                texte = f"Sélectionnez un pion à bouger,  tour du joueur {joueur_du_tour()}"
                                if marelle.pions[i] == joueur_du_tour():
                                    pion_selected = True
                                    pion_selected_val = i

                        if temp is not None:                            
                            if marelle.check_alligne(last_move)[0]:
                                alligne = True
                                joueur_qui_alligne = marelle.check_alligne(last_move)[1]                            
                    i += 1


    clock.tick(30)
    screen.fill(BG)

    if alligne:
        texte = f"Supprimez un pion de votre adversaire, tour du joueur {joueur_du_tour()}"
    elif marelle.tour < 18:
        texte = f"Début de partie, placez tous vos pions sur la grille, tour du joueur {joueur_du_tour()}"
    else:
        if pion_selected:
            texte = f"Choisissez l'endroit de dépose, tour du joueur {joueur_du_tour()}"
        else:
            texte = f"Sélectionnez un pion à bouger,  tour du joueur {joueur_du_tour()}"
    screen.blit(fond, (0, 0))
    afficher_texte_style(screen, texte, 820, 390)
    for i in marelle.nombre_liste_pions(1)[1]:
        dessiner_pion(screen, pion_j1, i)
    for i in marelle.nombre_liste_pions(2)[1]:
        dessiner_pion(screen, pion_j2, i)

    win, winner = marelle.check_win()
    if win:
        texte = f"Félicitation, le joueur {joueur_du_tour()} a gagné"
    pygame.display.flip()

pygame.quit()
>>>>>>> f6363ff (fin interface)
