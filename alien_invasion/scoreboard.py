import pygame.font

class Scoreboard():
    """显示得分类"""
    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #显示得分字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #准备初始得分图像
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """将得分渲染成图像"""
        rounded_score = int(round(self.stats.score,-1))
        #score_str = str(self.stats.score)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        #得分放置屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)

    def prep_high_score(self):
        """最高分渲染为图像"""
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

        #将最高分放在屏幕顶部
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

