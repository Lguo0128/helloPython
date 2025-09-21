# 12-3  火箭：编写一个游戏，开始时屏幕中央有一个火箭，而玩家可使用四个方向
# 键上下左右移动火箭。请务必确保火箭不会移到屏幕外面

import sys

import pygame

filepath = "d:\\workspaces\\helloPython\\practice\\chap12to14-Alians\\aliens\\"


class Rocket:
    def __init__(self, screen):
        self.screen = screen

        # 加载图像并获取其外接矩形
        self.image = pygame.image.load(filepath + "images\\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.speed_factor = 1.5
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True

    def check_keyup_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
        elif event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False

    def update(self):
        # 更新的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 向右移动飞船
            self.centerx += self.speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            # 向左移动飞船
            self.centerx -= self.speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            # 向上移动飞船
            self.centery -= self.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # 向下移动飞船
            self.centery += self.speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制"""
        self.screen.blit(self.image, self.rect)


def update_screen(bg_color, screen, rocket):
    # Redraw the screen during each pass through the loop.
    # 每次循环时都重绘屏幕
    screen.fill(bg_color)
    rocket.blitme()

    # Make the most recently drawn screen visible.
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def run_rocket():
    """创建一个背景为蓝色的Pygame 窗口。"""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rocket Window")
    rocket = Rocket(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                rocket.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                rocket.check_keyup_events(event)

        rocket.update()
        update_screen("Light Green", screen, rocket)


if __name__ == "__main__":
    # Make a game instance, and run the game.
    run_rocket()
