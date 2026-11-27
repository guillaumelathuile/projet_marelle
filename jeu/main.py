import pygame
from structure_marelle import Marelle

def dessiner_pion(screen, image, index_point):
    x, y = points[index_point]
    rect = image.get_rect(center=(x, y))
    screen.blit(image, rect)


pygame.init()
WIDTH, HEIGHT = 800, 800
ROWS = 6
MARGIN = 24
GAP = 7
GRID_TOP = 155

BG = (234, 18, 19)

WHITE = (245, 245, 245)
GREY = (58, 58, 60)
BORDER = (70, 70, 72)
GREEN = (83, 141, 78)
YELLOW = (181, 159, 59)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
fond = pygame.image.load(r"C:\Users\Lucas\Documents\ESEO\Algo et struct\Algo_et_struct_Projet_marelle\marelle_jungle.png").convert()
pion_j1 = pygame.image.load(r"C:\Users\Lucas\Documents\ESEO\Algo et struct\Algo_et_struct_Projet_marelle\pion_blanc.png").convert()
pion_j2 = pygame.image.load(r"C:\Users\Lucas\Documents\ESEO\Algo et struct\Algo_et_struct_Projet_marelle\pion_noir.png").convert()

pygame.display.set_caption("Marelle")
clock = pygame.time.Clock()

TITLE_FONT = pygame.font.SysFont("arial", 44, bold=True)
INFO_FONT = pygame.font.SysFont("arial", 22)
SMALL_FONT = pygame.font.SysFont("arial", 18)

C = 400
tolerance = 20

points = []
for r in (330, 220, 110):  # carré extérieur, milieu, intérieur
    for dx, dy in [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]:
        points.append((C + dx*r, C + dy*r))

marelle = Marelle()


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

                    if px -tolerance <= x <= px + tolerance and py -tolerance <= y <= py + tolerance:
                        marelle.pions[i] = 1
                    i += 1


    clock.tick(60)
    screen.fill(BG)
    
    screen.blit(fond, (0, 0))
    for i in marelle.nombre_liste_pions(1)[1]:
        dessiner_pion(screen, pion_j1, i)
    for i in marelle.nombre_liste_pions(2)[1]:
        dessiner_pion(screen, pion_j2, i)

    
    pygame.display.flip()

pygame.quit()
