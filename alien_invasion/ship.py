import pygame
from pygame.sprite import Sprite
#ship继承Sprite
class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其起始位置"""
        super(Ship,self).__init__()
        self.screen = screen

        self.ai_settings = ai_settings

        #加载飞船图片，并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp') #加载飞船图片
        #self.image = pygame.image.load(r'E:\VsCodeExercise\alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将新飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在center中存储小数值
        self.center = float(self.rect.centerx)

        #飞船移动
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def center_ship(self):
        #飞船屏幕居中
        self.center = self.screen_rect.centerx

    def blitme(self):
        """指定位置放置飞船"""
        self.screen.blit(self.image,self.rect)

