import pygame

from plane_sprites import  *



pygame.init()


screen = pygame.display.set_mode((480,700))

bg = pygame.image.load("./images/bg/主界面.jpg")
screen.blit(bg,(0,0))  #

hero = pygame.image.load("./images/hero/hero01.png")
screen.blit(hero,(200,500))

clock = pygame.time.Clock()
hero_rect = pygame.Rect(200,500,120,100)


# 创建敌机的精灵
enemy = GameSprite("./images/enemy/enemy.png")
# 精灵组
enemy_group = pygame.sprite.Group(enemy)


while True:
    clock.tick(60)

    for event in pygame.event.get():  # 监听时间退出游戏
         if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit()
    hero_rect.y -= 1
    if hero_rect.y <= -120:
        hero_rect.y =700
    screen.blit(bg, (0, 0))
    screen.blit(hero,hero_rect)
    # 让精灵族调用两个方法
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()
pygame.quit()