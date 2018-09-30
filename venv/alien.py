import pygame
from  pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self,ai_settings,screen):
        """初始化外星人冰设置起始位置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """加载外星人图像冰设置其属性"""
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        """每个外星人最初都在屏幕左上角"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """储存外星人的位置"""
        self.x = float(self.rect.x)

    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image,self.rect)