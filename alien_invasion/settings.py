class Settings():
    """存储所有有关alien invasion 的设置"""
    
    def __init__(self):
        """初始化alien invasion"""
        #屏幕设置
        self.screen_width = 960
        self.screen_heigth = 540
        self.bg_color = (230,230,230)

        #飞船移动设置
        self.ship_speed_factor = 1.5 #此处为小数，需要更改其他处像素设置
        self.ship_limit = 1

        #子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5

        #外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        #1向右，-1向左
        self.fleet_direction = -1

        #升级游戏，以某一加速度加快游戏进程
        self.speedup_scale = 1.1
        #外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而改变的参数"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = -1
        #计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        #当前击中一个外星人的得分
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)
        


        



