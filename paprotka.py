import pygame as pg
import sys
import random

screen = pg.display.set_mode((800, 800))
pg.init()
pg.display.set_caption("Function generator")
screen.fill((255, 255, 255))


t = [0.849,0.037,-0.037,0.849,0.075,0.183],\
    [0.197,-0.226,0.226,0.197,0.400,0.049],\
    [-0.150,0.283,0.260,0.237,0.575,-0.084],\
    [0.000,0.000,0.000,0.160,0.500,0.000],

x=0.520
y=0

for i in range(20000):
    rand = random.randint(0,3)

    x=x*t[rand][0]+y*t[rand][1]+t[rand][4]
    y=x*t[rand][2]+y*t[rand][3]+t[rand][5]

    pg.draw.rect(screen, (20, 200, 30), pg.Rect(500-x*300, 800-y*300, 3, 3))

    pg.display.flip()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
