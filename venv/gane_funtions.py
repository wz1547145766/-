import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def cheak_events(ai_settings,screen,ship,bullets):
    """监视鼠标键盘事件"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship,aliens,bullets):
    """每次循环都重绘制屏幕"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    """最近绘制的屏幕可见"""
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹位置冰删除消失的子弹"""
    """更新位置"""
    bullets.update()

    """删除消失的子弹"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(ai_settings,screen,ship,bullets):
    """创建一颗子弹，并将其加入到bullets"""
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullets = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullets)

def create_fleet(ai_settings,screen,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算可容纳多少个
    #外星人间距为外星人的宽度
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    """创建第一个外星人"""
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings,screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)