import pygame as pg
import math
import sys

screen = pg.display.set_mode((800, 800))
pg.init()
pg.display.set_caption("Function generator")
screen.fill((255, 255, 255))

def y(y):
    x = y - 400
    try:
        #################### Type Function down here: ####################
        y = 2*math.cos(1/10*x)*20 +100 - math.sin(1/10*x)*20
        ##################################################################
    except ZeroDivisionError:
        pg.draw.rect(screen, (0, 0, 255), pg.Rect(i-1, y-1, 1, 800))
    except ValueError: pass

    return -y + 400

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)

    pg.draw.rect(screen, (0, 0, 0), pg.Rect(400, 0, 1, 800))
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(0, 400, 800, 1))

    for i in range(800):
        pg.draw.rect(screen, (255, 0, 0), pg.Rect(i-1,y(i)-1, 3, 3))

        if i % 100 == 0: pg.draw.rect(screen, (0, 0, 0), pg.Rect(i-1,399, 3, 3))
        if i == 400:
            for j in range(9):
                pg.draw.rect(screen, (0, 0, 0), pg.Rect(399,j*100-1, 3, 3))

    pg.display.flip()
