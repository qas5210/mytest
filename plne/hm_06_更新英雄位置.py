import pygame

pygame.init()

screen = pygame.display.set_mode((480,700))

bg = pygame.image.load("./images/bg/主界面.jpg")
screen.blit(bg,(0,0))  #

hero = pygame.image.load("./images/hero/hero01.png")
screen.blit(hero,(200,500))
# pygame.display.update()

clock = pygame.time.Clock()
hero_rect = pygame.Rect(200,500,120,100)

while True:  # 游戏循环
    clock.tick(60) #指定游戏代码内部循环频率
    hero_rect.y -= 1
    screen.blit(bg, (0, 0))  # 再次绘制主页面会遮挡住移动的阴影
    screen.blit(hero,hero_rect)
    pygame.display.update()
pygame.quit()