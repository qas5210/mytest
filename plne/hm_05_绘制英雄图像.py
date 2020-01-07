import pygame

pygame.init()  # 初始化

screen = pygame.display.set_mode((480,700))  # 创建游戏的窗口

bg = pygame.image.load("./images/bg/主界面.jpg")  # 加载主页面

screen.blit(bg,(0,0))  # 绘制图形位置 blit背景坐标
# pygame.display.update()  # 更新屏幕显示

#  绘制英雄图像
hero = pygame.image.load("./images/hero/hero01.png")
screen.blit(hero,(200,500))
pygame.display.update()

clock = pygame.time.Clock()


while True:  # 游戏循环
    clock.tick(60) #指定游戏代码内部循环频率
pygame.quit()