#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import player
import entities

WIDTH = 800
HEIGHT = 640
DISPLAY = (WIDTH, HEIGHT)
BG_COLOR = '#323232'
LEVEL = ['-------------------------',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-                       -',
         '-------------------------']


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

    entities_group = pygame.sprite.Group()
    blocks = []
    entities_group.add(hero)

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

        x = y = 0
        for row in LEVEL:
            for col in row:
                if col == '-':
                    block = entities.Block(x, y)
                    entities_group.add(block)
                    blocks.append(block)
                x += block.width
            y += block.height
            x = 0

        hero.update(left, right, up, down)
        entities_group.draw(screen)

        pygame.display.update()     # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
