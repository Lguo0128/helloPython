# 12-4  按键：创建一个程序，显示一个空屏幕。在事件循环中，每当检测到
# pygame.KEYDOWN 事件时都打印属性event.key。运行这个程序，并按各种键，看看Pygame
# 如何响应。

import sys

import pygame


def check_keydown_events(event):
    if event.type == pygame.KEYDOWN:
        print("Event: " + str(event))
        # print("Pressed Key: " + str(event.dict['unicode']))
        print("\tPressed Key: " + pygame.key.name(event.key))


def run():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    screen.fill("light yellow")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event)

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    run()
