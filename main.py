import pygame, sys


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 650))
    screen.blit(floor_surface, (floor_x_pos + 450, 650))


pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

# Game variables
gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(450, 150))
floor_x_pos = 0

bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(100, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 5

    screen.blit(bg_surface, (0, 0))

    bird_movement += gravity
    bird_rect.centery += bird_movement

    screen.blit(bird_surface, bird_rect)
    draw_floor()
    floor_x_pos -= 1

    if floor_x_pos <= -450:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
