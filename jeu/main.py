import asyncio
import pygame

def dessiner_pion(screen, image, index_point):
    x, y = POINTS[index_point]
    rect = image.get_rect(center=(x, y))
    screen.blit(image, rect)

pygame.init()
WIDTH, HEIGHT = 800, 800
BG = (234, 18, 19)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
fond = pygame.image.load("marelle_jungle.png").convert()
pion_j1 = pygame.image.load("pion_bleu.png").convert_alpha()
pion_j2 = pygame.image.load("pion_rouge.png").convert_alpha()

pygame.display.set_caption("Marelle")
clock = pygame.time.Clock()

# Police par défaut de pygame (SysFont ne marche pas sur le web)
TITLE_FONT = pygame.font.Font(None, 54)
INFO_FONT = pygame.font.Font(None, 28)
SMALL_FONT = pygame.font.Font(None, 22)

C = 400
POINTS = []
for r in (330, 220, 110):  # carré extérieur, milieu, intérieur
    for dx, dy in [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]:
        POINTS.append((C + dx*r, C + dy*r))


async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG)
        screen.blit(fond, (0, 0))
        dessiner_pion(screen, pion_j1, 0)

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)   # obligatoire pour pygbag

asyncio.run(main())