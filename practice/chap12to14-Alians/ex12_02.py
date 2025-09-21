# 12-2  游戏角色：找一幅你喜欢的游戏角色位图图像或将一幅图像转换为位图。创
# 建一个类，将该角色绘制到屏幕中央，并将该图像的背景色设置为屏幕背景色，或将屏
# 幕背景色设置为该图像的背景色。
import sys

import pygame

filepath = "d:\\workspaces\\helloPython\\practice\\chap12to14-Alians\\"


class Character:
    def __init__(self, screen):
        """初始化游戏角色并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(filepath + "RS_ICON_PRE_FTB-768x769.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


def run():
    """创建一个背景为蓝色的Pygame 窗口。"""
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Blue Window")
    character = Character(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill("Light Blue")
        character.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    run()
