import pygame, sys


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 650))
    screen.blit(floor_surface, (floor_x_pos + 450, 650))


def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (600, 400))
    return new_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5;
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)


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

# Трубы
pipe_surface = pygame.image.load('sprites/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 5
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())
            print(pipe_list)

    screen.blit(bg_surface, (0, 0))

    # Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Floor
    draw_floor()
    floor_x_pos -= 1

    if floor_x_pos <= -450:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
