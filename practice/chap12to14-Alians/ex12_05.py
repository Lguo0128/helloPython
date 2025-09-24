# 12-5  侧面射击：编写一个游戏，将一艘飞船放在屏幕左边，并允许玩家上下移动
# 飞船。在玩家按空格键时，让飞船发射一颗在屏幕中向右穿行的子弹，并在子弹离开屏
# 幕而消失后将其删除。

# 1. import sys pygame
# 2. 创建主窗口
# 3. 根据需求创建对象类

import sys

import pygame
from pygame.sprite import Group, Sprite

filepath = "d:\\workspaces\\helloPython\\practice\\chap12to14-Alians\\aliens\\"


class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10


class Ship:
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(filepath + "images\\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕左中
        self.rect.centery = self.screen_rect.centery

        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 向右移动飞船
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            # 向左移动飞船
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            # 向上移动飞船
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # 向下移动飞船
            self.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        # 注意:代码super(Bullet, self).__init__()使用了Python 2.7语法。这种语法也适用于Python 3，但你也可以将这行代码简写为super().__init__()。
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        # 子弹并非基于图像的，因此我们必须使用pygame.Rect()类从空白开始创建一个矩形。创建这个类的实例时，必须提供矩形左上角的x坐标和y坐标，还有矩形的宽度和高度。
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        # 我们将子弹的centerx设置为飞船的rect.centerx。
        self.rect.centery = ship.rect.centery
        # 子弹应从飞船顶部射出，因此我们将表示子弹的rect的top属性设置为飞船的rect的top属性，让子弹看起来像是从飞船中射出的。
        self.rect.right = ship.rect.right

        # 存储用小数表示的子弹位置
        # 我们将子弹的y坐标存储为小数值，以便能够微调子弹的速度。
        self.x = float(self.rect.x)

        # 我们将子弹的颜色和速度设置分别存储到self.color和self.speed_factor中。
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向右移动子弹"""
        # 更新表示子弹位置的小数值
        self.x += self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        # 函数draw.rect()使用存储在self.color中的颜色填充表示子弹的rect占据的屏幕部分。
        pygame.draw.rect(self.screen, self.color, self.rect)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    # Redraw the screen during each pass through the loop.
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    # 我们给在屏幕上绘制子弹的update_screen() 添加了形参bullets 。方法bullets.sprites()返回一个列表，其中包含编组bullets中的所有精灵。为在屏幕上绘制发射的所有子弹，我们遍历编组bullets中的精灵，并对每个精灵都调用draw_bullet()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Make the most recently drawn screen visible.
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets, ai_settings):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    # 在for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本。我们使用了方法copy()来设置for循环
    for bullet in bullets.copy():
        if bullet.rect.right > ai_settings.screen_width:
            bullets.remove(bullet)
    # print(len(bullets))


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def run_game():
    """主窗口"""
    # 初始化
    pygame.init()
    settings = Settings()
    # 设置窗口大小
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # 创建一艘飞船
    ship = Ship(settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 主循环
    while True:
        check_events(settings, screen, ship, bullets)
        ship.update()
        update_bullets(bullets, settings)
        update_screen(settings, screen, ship, bullets)


if __name__ == "__main__":
    # Make a game instance, and run the game.
    run_game()
