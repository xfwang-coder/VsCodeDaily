import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对子弹进行管理的类"""
    
    def __init__(self,ai_settings,screen,ship):
        """在飞船所在位置创建一个子弹"""
        super(Bullet,self).__init__() #继承父类
        self.screen = screen

        #设置一个矩形
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #用小数表示子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
