import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 刷新帧率
FRAME_PER_SEC = 60

class GameSprite(pygame.sprite.Sprite) :
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):

        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Backgroud(GameSprite):
    """游戏背景精灵"""

    def update(self):
        # 1.调用父类的方法实现
        super.update()
        # 2.判断是否移除屏幕,如果移除屏幕，将背景移动到正上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
