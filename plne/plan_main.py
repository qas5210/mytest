import pygame
from plane_sprites import *

class PlanGame(object):
    """飞机大战游戏"""

    def __init__(self):
        print("游戏初始化")
        # 1.创建游戏的窗口
        self.scree = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("游戏开始...")

        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self._event_handler()
            # 3，碰撞检测
            self._check_collide()
            # 4.更新、绘制精灵族
            self._check_collide()
            # 5.更新显示
            pygame.display.update()

    def _event_handler(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlanGame._game_over()

    def _check_collide(self):
        pass

    def _update_sprites(self):
        pass

    @staticmethod
    def _game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    # 创建游戏对象
    game = PlanGame()
    game.start_game()