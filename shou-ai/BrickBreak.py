#!/usr/bin/python3

"""
游戏：打砖块

我们将从一个简单的打砖块游戏开始：
其中有一个球从平台上弹起以打破砖墙，玩家必须通过确保桨始终在那里将球弹回来来保持球的前进。
游戏将有三层砖块，每层砖块都有不同的打击能力，
这意味着有些砖块会在一次打击中破裂，有些砖块需要两次打击，有些则需要三次打击。

库：
    Tkinter：
        一个非常轻量级的模块，它有助于创建跨平台应用程序，python 自带。
"""

import tkinter


class GameObject(object):
    """
    游戏对象类
    所有其他类的父类
    """

    def __init__(self, canvas, item):
        """
        初始化函数
        :param canvas: 画布
        :param item: 画布上绘制的图形对象id
        """
        self.canvas = canvas
        self.item = item

    def get_position(self):
        """
        获取当前游戏对象的坐标
        :return: 返回坐标（四元素列表：左上点 x y 坐标，右下点 x y 坐标）
        """
        return self.canvas.coords(self.item)

    def move(self, x, y):
        """
        移动当前游戏对象
        :param x: x（水平）方向移动偏移量
        :param y: y（垂直）方向移动偏移量
        :return:
        """
        self.canvas.move(self.item, x, y)

    def delete(self):
        """
        删除当前游戏对象
        :return:
        """
        self.canvas.delete(self.item)


class Brick(GameObject):
    """
    砖块类
    """
    COLORS = {1: '#00FF00', 2: '#00FFFF', 3: '#0000FF', 4: '#FF00FF', 5: '#FF0000'}

    def __init__(self, canvas, x, y, hits):
        """
        初始化函数
        :param canvas: 画布
        :param x: 坐标 - x
        :param y:坐标 - y
        :param hits: 可撞击次数
        """
        self.width = 75
        self.height = 20
        self.hits = hits
        # 具有不同撞击次数(硬度)的砖块具有不同颜色
        color = Brick.COLORS[hits]
        # 在画布上创建矩形，得到图形id
        item = canvas.create_rectangle(x - self.width / 2, y - self.height / 2,
                                       x + self.width / 2, y + self.height / 2,
                                       fill=color, tags='brick')
        # 使用矩形作为砖块
        super(Brick, self).__init__(canvas, item)

    def hit(self):
        """
        砖块撞击函数（消失/变色）
        :return:
        """
        # 每被撞击一次，可撞击次数减少一次
        self.hits -= 1
        if self.hits == 0:
            # 可撞击次数为0，砖块消失
            self.delete()
        else:
            # 还有可撞击次数，重新设置该砖块对象：修改颜色
            self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])


class Ball(GameObject):
    """
    球类
    """

    def __init__(self, canvas, x, y):
        """
        初始化函数
        :param canvas: 画布
        :param x: 坐标 - x
        :param y: 坐标 - y
        """
        # 球半径
        self.radius = 10
        # 球前进方向[x, y]，x（正方向）向右为正，y（正方向）向下为正
        self.direction = [1, -1]
        # 球运动速度（每次移动时，x和y方向移动单位距离）
        self.speed = 5
        # 在画布上创建圆形，得到图形id
        item = canvas.create_oval(x - self.radius, y - self.radius,
                                  x + self.radius, y + self.radius,
                                  fill='white')
        # 使用圆形作为球
        super(Ball, self).__init__(canvas, item)

    def update(self):
        """
        球移动函数
        :return:
        """
        # 获取球对象的坐标
        coords = self.get_position()
        # 获取画布的宽度
        width = self.canvas.winfo_width()
        # 球到达画布两边后，x(水平)移动方向反转
        if coords[0] <= 0 or coords[2] >= width:
            self.direction[0] *= -1
        # 球到达画布上边后，y(垂直)运动方向反转
        if coords[1] <= 0:
            self.direction[1] *= -1
        # 按最新方向移动一次单位距离
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        self.move(x, y)

    def collide(self, game_objects):
        """
        球碰撞事件
        :param game_objects: 与球碰撞的其他游戏对象
        :return:
        """
        # 获取球对象坐标
        coords = self.get_position()
        # 球心 x 坐标
        x = (coords[0] + coords[2]) * 0.5
        if len(game_objects) > 1:
            # 如果球同时撞到了多个对象
            # 水平方向不变，垂直方向变化
            self.direction[1] *= -1
        elif len(game_objects) == 1:
            # 如果球只撞到了1个对象
            game_object = game_objects[0]
            # 获取被撞游戏对象的坐标
            coords = game_object.get_position()
            if x > coords[2]:
                # 如果球撞在游戏对象（砖块/桨）右侧
                # 水平方向变为向右
                self.direction[0] = 1
            elif x < coords[0]:
                # 如果球撞在游戏对象（砖块/桨）左侧
                # 水平方向变为向左
                self.direction[0] = -1
            else:
                # 其他情况，球撞在游戏对象（砖块/桨）的水平面上
                # 水平方向不变，垂直方向变化
                self.direction[1] *= -1

        for game_object in game_objects:
            # 循环所有被撞游戏对象
            if isinstance(game_object, Brick):
                # 如果该被撞游戏对象是砖块
                # 砖块发生撞击事件（函数）
                game_object.hit()


class Paddle(GameObject):
    """
    桨（挡板）类
    """

    def __init__(self, canvas, x, y):
        """
        初始化函数
        :param canvas: 画布
        :param x: 坐标 - x
        :param y: 坐标 - y
        """
        self.width = 80
        self.height = 10
        self.ball = None
        # 在画布上创建矩形元素，得到图形id
        item = canvas.create_rectangle(x - self.width / 2, y - self.height / 2,
                                       x + self.width / 2, y + self.height / 2,
                                       fill='grey')
        # 使用矩形元素作为桨
        super(Paddle, self).__init__(canvas, item)

    def set_ball(self, ball):
        """
        设置桨（挡板）上的球
        :param ball: 桨上的球对象
        :return:
        """
        self.ball = ball

    def slide(self, offset):
        """
        左右移动桨（挡板）
        :param offset: 左右移动的偏移量
        :return:
        """
        # 获取当前元素对象（桨）坐标
        coords = self.get_position()
        # 获取画布的宽度
        width = self.canvas.winfo_width()
        # 如左右移动目标位置在画布范围内，则移动
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super(Paddle, self).move(offset, 0)
            # 如桨上有球存在，则球也一起移动
            if self.ball is not None:
                self.ball.move(offset, 0)


class Game(tkinter.Frame):
    """
    游戏总控
    """

    def __init__(self, master):
        """
        初始化函数
        :param master: 程序窗口对象
        """
        # 在窗口中创建游戏框架
        super(Game, self).__init__(master)
        # 游戏生命次数
        self.lives = 3
        # 设置框架宽度
        self.width = 600
        # 设置框架高度
        self.height = 400
        # 在框架上创建画布
        self.canvas = tkinter.Canvas(self, bg='#D6D1F5',
                                     width=self.width, height=self.height)
        # 布局画布
        self.canvas.pack()
        # 布局游戏框架
        self.pack()
        # 游戏内各个对象字典
        self.items = dict[int, GameObject]()
        self.ball = None
        # 创建桨（挡板）对象
        self.paddle = Paddle(self.canvas, self.width / 2, 326)
        # 把桨放入对象字典
        self.items[self.paddle.item] = self.paddle
        # 横向每隔75像素循环绘制
        row = len(Brick.COLORS)
        for x in range(0, self.width, 75):
            # 纵向循环3次绘制
            for n in range(row):
                # 在指定坐标处添加一个指定砖块
                self.add_brick(x + 37.5, n * 20 + 50, 5 - n)
        # 游戏生命信息文字绘制id
        self.hud = None
        # 游戏提示信息绘制id
        self.text = None
        # 启动游戏
        self.setup_game()
        # 使画布获取焦点
        self.canvas.focus_set()
        # 画布绑定按键：<Left> --> 桨向左移动10像素
        self.canvas.bind('<Left>', lambda _: self.paddle.slide(-10))
        # 画布绑定按键：<Right> --> 桨向右移动10像素
        self.canvas.bind('<Right>', lambda _: self.paddle.slide(10))

    def setup_game(self):
        """
        启动游戏
        :return:
        """
        # 添加一个球
        self.add_ball()
        # 更新游戏生命信息
        self.update_lives_text()
        # 绘制启动提示文字，得到提示文字绘制id
        self.text = self.draw_text(300, 200, 'Press Space to start')
        # 画布绑定按键：<space> --> 开始游戏
        self.canvas.bind('<space>', lambda _: self.start_game())

    def add_ball(self):
        """
        添加球对象
        :return:
        """
        # 如果游戏中已存在球对象，则删除
        if self.ball is not None:
            self.ball.delete()
        # 获取桨的坐标
        paddle_coords = self.paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) / 2
        # 在桨中间位置创建一个球
        # 桨y=326(321-331)，球y=310(300-320)
        self.ball = Ball(self.canvas, x, 310)
        # 将球设置给桨
        self.paddle.set_ball(self.ball)

    def add_brick(self, x, y, hits):
        """
        添加砖块对象
        :param x: 坐标 - x
        :param y: 坐标 - y
        :param hits: 可撞击次数
        :return:
        """
        # 创建一个砖块
        brick = Brick(self.canvas, x, y, hits)
        # 将砖块放入游戏对象字典
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size=40):
        """
        在画布上绘制文本
        :param x: 坐标 - x
        :param y: 坐标 - y
        :param text: 文本
        :param size: 字体大小
        :return: 画布上的文字绘制对象id
        """
        font = ('Forte', size)
        return self.canvas.create_text(x, y, text=text, font=font)

    def update_lives_text(self):
        # 游戏生命次数信息
        text = 'Lives: %s' % self.lives
        if self.hud is None:
            # 如果生命次数信息绘制id不存在(游戏最初)
            # 绘制文本，得到绘制id
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            # 如果绘制id已存在（游戏中途）
            # 根据绘制id，更新文本信息
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        """
        开始游戏
        :return:
        """
        # 画布解绑按键：<space>
        self.canvas.unbind('<space>')
        # 根据绘制id删除绘制对象（开始游戏提示信息）
        self.canvas.delete(self.text)
        # 解绑桨上的球
        self.paddle.ball = None
        # 执行游戏循环
        self.game_loop()

    def game_loop(self):
        """
        游戏循环
        :return:
        """
        # 撞击检查并处理
        self.check_collisions()
        # 获取剩余砖块数量
        num_bricks = len(self.canvas.find_withtag('brick'))
        if num_bricks == 0:
            # 如果砖块全部消失
            # 球停止运动
            self.ball.speed = None
            # 画布绘制 win 文字信息
            self.draw_text(300, 200, 'Win! Bricks Breaker!')
        elif self.ball.get_position()[3] >= self.height:
            # 如果球掉到画布底部（落地）
            # 球停止运动
            self.ball.speed = None
            # 游戏生命 - 1
            self.lives -= 1
            if self.lives <= 0:
                # 更新游戏生命信息
                self.update_lives_text()
                self.draw_text(300, 200, 'Failed! Game Over!')
            else:
                self.after(1000, self.setup_game)
        else:
            # 其他情况（即没 win 也没 落地）
            # 球继续移动
            self.ball.update()
            self.after(50, self.game_loop)

    def check_collisions(self):
        """
        撞击检查
        :return:
        """
        # 获取球坐标(左上点和右下点坐标)
        ball_coords = self.ball.get_position()
        # 在画布上，查找球坐标矩形范围内，其他重叠绘制项的id
        items = self.canvas.find_overlapping(*ball_coords)
        # 循环游戏对象字典（桨和砖块），找出重叠绘制项
        objects = [self.items[x] for x in items if x in self.items]
        # 执行球的撞击事件(函数)，参数为重叠绘制项，即撞击到的游戏对象
        self.ball.collide(objects)


if __name__ == '__main__':
    root = tkinter.Tk()  # 创建窗口
    root.title("BrickBreak")
    game = Game(root)
    game.mainloop()
