import pygame
pygame.init()
WIDTH, HEIGHT = 600, 760
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
pygame.display.set_caption("Marelle")
clock = pygame.time.Clock()

TITLE_FONT = pygame.font.SysFont("arial", 44, bold=True)
INFO_FONT = pygame.font.SysFont("arial", 22)
SMALL_FONT = pygame.font.SysFont("arial", 18)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    screen.fill(BG)
    pygame.display.flip()

pygame.quit()
