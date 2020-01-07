import pygame
pygame.init()

screen = pygame.display.set_mode((480,700))  # 创建游戏的窗口

bg = pygame.image.load("./images/bg/主界面.jpg")  # 加载主页面

screen.blit(bg,(0,0))  # 绘制图形位置 blit背景坐标
pygame.display.update()  # 更新屏幕显示



while True:
    pass
pygame.quit()