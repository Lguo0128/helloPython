import pygame
from pygame.sprite import Sprite


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
        self.rect.centerx = ship.rect.centerx
        # 子弹应从飞船顶部射出，因此我们将表示子弹的rect的top属性设置为飞船的rect的top属性，让子弹看起来像是从飞船中射出的。
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        # 我们将子弹的y坐标存储为小数值，以便能够微调子弹的速度。
        self.y = float(self.rect.y)

        # 我们将子弹的颜色和速度设置分别存储到self.color和self.speed_factor中。
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self): 
        """向上移动子弹""" 
        #更新表示子弹位置的小数值 
        self.y -= self.speed_factor 
        #更新表示子弹的rect的位置 
        self.rect.y = self.y 
 
    def draw_bullet(self): 
        """在屏幕上绘制子弹""" 
        # 函数draw.rect()使用存储在self.color中的颜色填充表示子弹的rect占据的屏幕部分。
        pygame.draw.rect(self.screen, self.color, self.rect)