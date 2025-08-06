import pygame, sys

pygame.init()
screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png').convert()  # добавляем преобразование изображения
bg_surface = pygame.transform.scale(bg_surface, (450, 800))  # Делаем фоновое изображение по размеру экрана

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))

    pygame.display.update()
    clock.tick(120)
