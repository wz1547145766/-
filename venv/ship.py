import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        """加载飞船图形冰获取其外界矩形"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """将飞船放到屏幕最下方中央"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        """在飞船的属性中存储小数"""
        self.center = float(self.rect.centerx)

        """移动标志"""
        self.moving_right = False
        self.moving_left = False

    def updect(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
