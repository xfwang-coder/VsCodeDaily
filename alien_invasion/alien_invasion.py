import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf 
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():
    #初始化游戏并创建屏幕对象
    pygame.init()
 

    #创建Settings的实例
    ai_settings = Settings()

    #screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
    pygame.display.set_caption("Alien Invasion")

   #创建play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一艘飞船
    ship = Ship(ai_settings,screen) #创建一个实例，名为ship
    #存储子弹的编组
    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建一个外星人
    #alien = Alien(ai_settings,screen)
    
    #创建统计游戏信息的实例
    stats = GameStats(ai_settings)

    #开始游戏循环
    while True:
        #监视键盘和鼠标
        """for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()"""
        gf.check_events(ai_settings,screen,stats,play_button,ship,bullets)
        #gf.check_events(ship)
        if stats.game_active:
            #更新事件状态
            ship.update()
            #更新子弹
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            #更新alien位置
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)

run_game()
