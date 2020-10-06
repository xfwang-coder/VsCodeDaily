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

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5



