import pygame, sys

pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()  # импорт изображения земли
floor_surface = pygame.transform.scale(floor_surface,(450, 150))  # подгоняем ширину под холст (и высоту)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    screen.blit(floor_surface, (0, 650))  # Отобразим землю в нужном месте холста

    pygame.display.update()
    clock.tick(120)
