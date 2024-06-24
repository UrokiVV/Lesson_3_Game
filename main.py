# main  Game "Tir"  22.06.2024
import pygame
import random
pygame.init()

SCREEN_SIZE_X = 800
SCREEN_SIZE_Y = 600
screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img / icon_N1.jpg")
pygame.display.set_icon(icon)

target_image  = pygame.image.load("img /")
target_width  = 80
target_height = 80
target_x = random.randint(0, SCREEN_SIZE_X - target_width)
target_y = random.randint(0, SCREEN_SIZE_Y - target_height)
# случайный выбор цвета
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

