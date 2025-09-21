# 12-1 蓝色天空：创建一个背景为蓝色的Pygame 窗口。

import sys

import pygame


def blue_windows():
    """创建一个背景为蓝色的Pygame 窗口。"""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blue Window")
    screen.fill("Blue")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    blue_windows()
