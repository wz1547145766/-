import  sys
import pygame

from settings import Settings
from ship import Ship
import gane_funtions as gf
from pygame.sprite import Group
from alien import  Alien


def run_game():
    """初始化游戏并,设置冰创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("外星人大战")

    """创建一个飞船"""
    ship = Ship(ai_settings,screen)

    """创建一个子弹编组"""
    bullets = Group()

    """创建一个外星人编组"""
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens)

    """创建一个外星人"""
    alien = Alien(ai_settings,screen)

    while True:
        gf.cheak_events(ai_settings,screen,ship,bullets)
        ship.updect()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
