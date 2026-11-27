import asyncio
import pygame
from structure_marelle import Marelle


def dessiner_pion(screen, image, index_point):
    x, y = points[index_point]
    rect = image.get_rect(center=(x, y))
    screen.blit(image, rect)


pygame.init()
WIDTH, HEIGHT = 800, 800

BG = (234, 18, 19)

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