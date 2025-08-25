import pygame, sys, random


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 650))
    screen.blit(floor_surface, (floor_x_pos + 450, 650))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(600, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(600, random_pipe_pos - 300))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 800:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, flip_x=False, flip_y=True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 800:
        return False

    return True


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect


def score_display():  # Создаём функцию для отображения очков
    score_surface = game_font.render(str(int(score)), True, (255, 255, 255))  # Надпись, сглаживание и цвет
    score_rect = score_surface.get_rect(center=(225, 100))
    screen.blit(score_surface, score_rect)


pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf', 40)  # Стиль и размер шрифта


# Game variables
gravity = 0.25
bird_movement = 0
game_active = True  # Флаг работы игры
score = 0  # Текущее кол-во очков
high_score = 0  # Лучший результат

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (450, 800))

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface, (450, 150))
floor_x_pos = 0

# Bird
bird_downflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-upflap.png').convert_alpha())

bird_frames = [bird_downflap, bird_midflap, bird_upflap]  # Список с "кадрами" анимации
bird_index = 0  # Индекс кадра в списке
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 400))

BIRDFLAP = pygame.USEREVENT + 1  # Каждое следующее событие создаётся с увеличением на +1
pygame.time.set_timer(BIRDFLAP, 200)

# bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert_alpha()
# bird_surface = pygame.transform.scale2x(bird_surface)
# bird_rect = bird_surface.get_rect(center=(100, 400))

# Трубы
pipe_surface = pygame.image.load('sprites/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [300, 400, 500]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 5

            if event.key == pygame.K_SPACE and not game_active:
                pipe_list.clear()
                bird_rect.center = (100, 400)
                bird_movement = 0
                game_active = True

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            bird_index = (bird_index + 1) % len(bird_frames)
            bird_surface, bird_rect = bird_animation()

    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)

        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)  # повёрнутая птица
        game_active = check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Scores
        score += 0.01
        score_display()


    # Floor
    draw_floor()
    floor_x_pos -= 1

    if floor_x_pos <= -450:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
