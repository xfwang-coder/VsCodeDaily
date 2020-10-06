import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf 
from pygame.sprite import Group
from alien import Alien


def run_game():
    #初始化游戏并创建屏幕对象
    pygame.init()
    #创建Settings的实例
    ai_settings = Settings()

    #screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings,screen) #创建一个实例，名为ship
    #存储子弹的编组
    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens)
    #创建一个外星人
    #alien = Alien(ai_settings,screen)
    #设置背景颜色
    #bg_color = (225,225,225)

    #开始游戏循环
    while True:
        #监视键盘和鼠标
        """for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()"""
        gf.check_events(ai_settings,screen,ship,bullets)
        #gf.check_events(ship)
        #更新事件状态
        ship.update()
        #更新屏幕
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
