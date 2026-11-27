import pygame

def dessiner_pion(screen, image, index_point):
    x, y = POINTS[index_point]
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
fond = pygame.image.load("marelle_jungle.png").convert()
pion_j1 = pygame.image.load("pion_bleu.png").convert()
pion_j2 = pygame.image.load("pion_rouge.png").convert()

pygame.display.set_caption("Marelle")
clock = pygame.time.Clock()

TITLE_FONT = pygame.font.SysFont("arial", 44, bold=True)
INFO_FONT = pygame.font.SysFont("arial", 22)
SMALL_FONT = pygame.font.SysFont("arial", 18)

C = 400
POINTS = []
for r in (330, 220, 110):  # carré extérieur, milieu, intérieur
    for dx, dy in [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]:
        POINTS.append((C + dx*r, C + dy*r))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    screen.fill(BG)
    
    screen.blit(fond, (0, 0))
    dessiner_pion(screen, pion_j1, 0)

    
    pygame.display.flip()

pygame.quit()
