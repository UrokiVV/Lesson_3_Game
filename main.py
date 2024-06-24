# main  Game "Tir"  22.06.2024
import pygame
import random
pygame.init()

print("Game Tir")
SCREEN_SIZE_X = 800
SCREEN_SIZE_Y = 600
screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
pygame.display.set_caption("Игра Тир")
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

icon = pygame.image.load("img/icon_N1.jpg")
pygame.display.set_icon(icon)
target_image  = pygame.image.load("img/target.png")
target_width  = 80
target_height = 80
target_x = random.randint(0, SCREEN_SIZE_X - target_width)
target_y = random.randint(0, SCREEN_SIZE_Y - target_height)
screen.fill(color)

screen.blit(target_image, (target_x, target_y))
pygame.display.update()
#print("event=" + str(pygame.quit))


fl_run = True
while fl_run:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            fl_run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x+target_width and target_y < mouse_y < target_y+target_height:
                target_x = random.randint(0, SCREEN_SIZE_X - target_width)
                target_y = random.randint(0, SCREEN_SIZE_Y - target_height)
                screen.blit(target_image, (target_x, target_y))
                pygame.display.update()


pygame.quit()


