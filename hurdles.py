'''Design of hurdles'''
from obstacles import Pipe, Valley, Brick
from enemy import Pakistan, China
from coins import coin_row
from spring import Spring
from base import FLOOR, Point, Dimension

HURDLES = []


class Hurdle:
    '''A group of obstacles'''

    def __init__(self, start, width, obstacles, enemies, board):
        self.start = start
        self.width = width
        self.obstacles = obstacles
        self.enemies = enemies
        self.board = board

    def load(self):
        '''Render on board'''
        for i in self.obstacles:
            i.draw()
        for i in self.enemies:
            i.update()

    def motion(self):
        '''Self motion of enemies'''
        for i in self.enemies:
            i.self_move(1)


class ThreePipes(Hurdle):
    '''Creating three pipe hurdle'''

    def __init__(self, start, board):
        width = 21
        obstacles = []
        obstacles.append(Pipe(start, 6, board))
        obstacles.append(Pipe(start + 8, 10, board))
        obstacles.append(Valley(start+13, 3, board))
        obstacles.append(Pipe(start + 16, 14, board))
        Hurdle.__init__(self, start, width, obstacles, [], board)
        self.load()


HURDLES.append([21, ThreePipes])


class TwoPipes(Hurdle):
    ''' 2 enemies between two pipes'''

    def __init__(self, start, board):
        width = 36
        obstacles = []
        obstacles.append(Pipe(start, 6, board))
        obstacles.append(Pipe(start + 30, 6, board))
        enemy = []
        enemy.append(Pakistan(FLOOR - 2, start + 9, board))
        enemy.append(Pakistan(FLOOR - 2, start + 13, board))
        Hurdle.__init__(self, start, width, obstacles, enemy, board)
        self.load()


HURDLES.append([36, TwoPipes])


class BrickJungle(Hurdle):
    '''Some arrangement of bricks'''

    def __init__(self, start, board):
        width = 56
        obstacles = []
        obstacles.append(Brick(Point(19, start), Dimension(2, 5), board))
        obstacles.append(Brick(Point(15, start + 8), Dimension(2, 5), board))
        obstacles.append(Brick(Point(11, start + 16), Dimension(2, 5), board))
        obstacles.append(Brick(Point(5, start + 21), Dimension(2, 11), board))
        obstacles.append(Brick(Point(19, start + 21), Dimension(2, 11), board))
        obstacles.append(Valley(start + 19, 15, board))
        obstacles.append(Brick(Point(11, start + 32), Dimension(2, 5), board))
        obstacles.append(Brick(Point(15, start + 40), Dimension(2, 5), board))
        obstacles.append(Brick(Point(19, start + 48), Dimension(2, 5), board))
        coin_row(Point(4, start+21), Dimension(1, 11), board)
        Hurdle.__init__(self, start, width, obstacles, [], board)
        self.load()


HURDLES.append([56, BrickJungle])


class BossPipes(Hurdle):
    ''' 1 boss enemies between two pipes'''

    def __init__(self, start, board):
        width = 36
        obstacles = []
        obstacles.append(Pipe(start, 6, board))
        obstacles.append(Pipe(start + 30, 6, board))
        obstacles.append(Brick(Point(15, start + 9), Dimension(2, 7), board))
        obstacles.append(Brick(Point(15, start + 19), Dimension(2, 7), board))
        enemy = []
        enemy.append(China(FLOOR - 3, start + 9, board))
        coin_row(Point(FLOOR - 1, start + 5), Dimension(1, 25), board)
        Hurdle.__init__(self, start, width, obstacles, enemy, board)
        self.load()


HURDLES.append([36, BossPipes])


class SpringPipe(Hurdle):
    '''Springs'''

    def __init__(self, start, board):
        width = 26
        obstacles = []
        obstacles.append(Spring(start + 3, 6, board))
        coin_row(Point(8, start + 6), Dimension(10, 1), board)
        enemy = []
        enemy.append(Pakistan(FLOOR - 2, start, board))
        enemy.append(Pakistan(FLOOR - 2, start + 13, board))
        Hurdle.__init__(self, start, width, obstacles, enemy, board)
        self.load()


HURDLES.append([26, SpringPipe])
