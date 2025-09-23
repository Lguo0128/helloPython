import sys

import game_functions as gf
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # 初始化游戏并创建一个屏幕对象
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""

        # 创建一艘飞船
        ship = Ship(self.settings, self.screen)

        # 创建一个用于存储子弹的编组
        bullets = Group()

        # 开始游戏主循环
        while True:
            # Watch for keyboard and mouse events.
            # 监听键盘和鼠标事件
            gf.check_events(self.settings, self.screen, ship, bullets)
            ship.update()
            bullets.update()
            gf.update_screen(self.settings, self.screen, ship, bullets)


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
