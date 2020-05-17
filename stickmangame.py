from tkinter import *
import random
import time


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title('Человечек бежит к выходу')
        self.tk.resizable(0, 0)
        self.tk.wm_attributes('-topmost', 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_width = 500
        self.canvas_height = 500
        self.bg = PhotoImage(file='background.gif')
        self.bg2 = PhotoImage(file='background_wood.gif')
        self.bg3 = PhotoImage(file='background_marble.gif')
        self.bg4 = PhotoImage(file='background_desert.gif')
        self.bg5 = PhotoImage(file='background_ice.gif')
        backgrounds = [self.bg, self.bg2, self.bg3, self.bg4, self.bg5]
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h, image=backgrounds[2], anchor='nw')
                random.shuffle(backgrounds)
        self.sprites = []
        self.running = True

    def mainloop(self):
        while 1:
            if self.running:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)


class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        pass

    def coords(self):
        return self.coordinates


class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + width, y +height)


def within_x(co1, co2):
    if (co2.x1 < co1.x1 < co2.x2) \
            or (co2.x1 < co1.x2 < co2.x2) \
            or (co1.x1 < co2.x1 < co1.x2) \
            or (co1.x1 < co2.x2 < co1.x2):
        return True
    else:
        return False


def within_y(co1, co2):
    if (co2.y1 < co1.y1 < co2.y2) \
            or (co2.y1 < co1.y2 < co2.y2) \
            or (co1.y1 < co2.y1 < co1.y2) \
            or (co1.y1 < co2.y2 < co1.y2):
        return True
    else:
        return False


def collided_left(co1, co2):
    if within_y(co1, co2):
        if co2.x2 >= co1.x1 >= co2.x1:
            return True
    return False


def collided_right(co1, co2):
    if within_y(co1, co2):
        if co2.x1 <= co1.x2 <= co2.x2:
            return True
    return False


def collided_top(co1, co2):
    if within_x(co1, co2):
        if co2.y2 >= co1.y1 >= co2.y1:
            return True
    return False


def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if co2.y1 <= y_calc <= co2.y2:
            return True
    return False


g = Game()
platform1 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 0, 480, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 150, 440, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 45, 60, 66, 10)
platform9 = PlatformSprite(g, PhotoImage(file='platform3.gif'), 170, 250, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file='platform3.gif'), 230, 200, 32, 10)
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.mainloop()
