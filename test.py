#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import player

WIDTH = 800
HEIGHT = 600
DISPLAY = (WIDTH, HEIGHT)
BG_COLOR = '#323232'

def main():
    pygame.init() # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("CRUSADER") # Пишем в шапку
    bg = pygame.Surface(DISPLAY) # Создание видимой поверхности
                                         # будем использовать как фон
    bg.fill(pygame.Color(BG_COLOR))     # Заливаем поверхность сплошным цветом
    timer = pygame.time.Clock()
    hero = player.Player(55, 55)
    left=right=up=down = False

    while 1: # Основной цикл программы
        timer.tick(60)
        for event in pygame.event.get(): # Обрабатываем события
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                up = True
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                up = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                down = True
            if event.type == pygame.KEYUP and event.key == pygame.K_s:
                down = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                left = True
            if event.type == pygame.KEYUP and event.key == pygame.K_a:
                left = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                right = True
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                right = False

        screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать
        hero.update(left, right, up, down)
        hero.draw(screen)
        pygame.display.update()     # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
