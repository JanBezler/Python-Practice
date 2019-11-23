import pygame as pg
import sys
import random

screen = pg.display.set_mode((800, 800))
pg.init()
pg.display.set_caption("Function generator")
screen.fill((255, 255, 255))

x=1
y=1

for i in range(10000):
    rand = random.randint(0,1)

    if rand == 0:
        x = -0.4*x-1
        y = -0.4*y+0.1

    if rand == 1:
        x = 0.76*x-0.4*y
        y = 0.4*x+0.76*y

    if i >= 100:
        pg.draw.rect(screen, (20, 200, 30), pg.Rect(300-x*300, 400-y*300, 2, 2))

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
