import pygame as pg
import sys
from os import path


class main(object):
    def __init__(self):
        self.screen = pg.display.set_mode((860, 640))
        self.loadData()
        self.firstMakeMatrix()
        pg.init()
        pg.display.set_caption("Game")

        self.whitef = ["P1","P2","P3","P4","P5","P6","P7","P8","W1","W2","G1","G2","S1","S2","H","K"]
        self.blackf = ["PC1","PC2","PC3","PC4","PC5","PC6","PC7","PC8","WC1","WC2","GC1","GC2","SC1","SC2","HC","KC"]
        self.selected = []
        self.possibilities = []
        self.player = 0


        while True:
            self.draw()
            self.screen.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)

                if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pos()[0] / 80 < 8:
                    self.hor = pg.mouse.get_pos()[0] / 80
                    self.ver = pg.mouse.get_pos()[1] / 80

                    self.selected.insert(0,{"h":int(self.hor),"v":int(self.ver),"t":self.matrix[int(self.ver)][int(self.hor)]})
                    try:

                        self.validate()

                    except: pass




    def moveFigure(self, fr1, fr2, to1, to2):
        if fr1 != to1 or fr2 != to2:
            if self.matrix[fr1][fr2] != "O":
                self.matrix[to1][to2] = self.matrix[fr1][fr2]
                self.matrix[fr1][fr2] = "O"
                self.player += 1
                self.selected.clear()


    def validate(self):
        if self.whitef.count(self.selected[0].get("t")) == 1:
            if self.whitef.count(self.selected[0].get("t")) == self.whitef.count(self.selected[1].get("t")):
                return 0

        if self.blackf.count(self.selected[0].get("t")) == 1:
            if self.blackf.count(self.selected[0].get("t")) == self.blackf.count(self.selected[1].get("t")):
                return 0

        if self.selected[1].get("t") == "W1" or self.selected[1].get("t") == "W2" \
                or self.selected[1].get("t") == "WC1" or self.selected[1].get("t") == "WC2":

            ##################################################################################################################




            pass
        self.moveFigure(self.selected[1].get("v"), self.selected[1].get("h"), self.selected[0].get("v"),
                        self.selected[0].get("h"))


    def draw(self):

        colorid = 0
        for i in range(8):
            colorid += 1
            for j in range(8):
                if colorid % 2 == 0:
                    color = (90, 90, 90)
                else:
                    color = (220, 220, 220)
                colorid += 1
                self.drawLabel[i][j] = pg.draw.rect(self.screen, (color), pg.Rect(i * 80, j * 80, 80, 80))

        for i in range(8):
            for j in range(8):
                if self.matrix[i][j] == "P1": self.P1 = self.screen.blit(self.figureP, (j * 80, i * 80))
                if self.matrix[i][j] == "P2": self.P2 = self.screen.blit(self.figureP, (j * 80, i * 80))
                if self.matrix[i][j] == "P3": self.P3 = self.screen.blit(self.figureP, (j * 80, i * 80))
                if self.matrix[i][j] == "P4": self.P4 = self.screen.blit(self.figureP, (j * 80, i * 80))
                if self.matrix[i][j] == "P5": self.P5 = self.screen.blit(self.figureP, (j * 80, i * 80))
                if self.matrix[i][j] == "P6": self.P6 = self.screen.blit(self.figureP, (j * 80, i * 80))
                if self.matrix[i][j] == "P7": self.P7 = self.screen.blit(self.figureP, (j * 80, i * 80))
                if self.matrix[i][j] == "P8": self.P8 = self.screen.blit(self.figureP, (j * 80, i * 80))
                if self.matrix[i][j] == "PC1": self.PC1 = self.screen.blit(self.figurePC, (j * 80, i * 80))
                if self.matrix[i][j] == "PC2": self.PC2 = self.screen.blit(self.figurePC, (j * 80, i * 80))
                if self.matrix[i][j] == "PC3": self.PC3 = self.screen.blit(self.figurePC, (j * 80, i * 80))
                if self.matrix[i][j] == "PC4": self.PC4 = self.screen.blit(self.figurePC, (j * 80, i * 80))
                if self.matrix[i][j] == "PC5": self.PC5 = self.screen.blit(self.figurePC, (j * 80, i * 80))
                if self.matrix[i][j] == "PC6": self.PC6 = self.screen.blit(self.figurePC, (j * 80, i * 80))
                if self.matrix[i][j] == "PC7": self.PC7 = self.screen.blit(self.figurePC, (j * 80, i * 80))
                if self.matrix[i][j] == "PC8": self.PC8 = self.screen.blit(self.figurePC, (j * 80, i * 80))
                if self.matrix[i][j] == "K": self.K = self.screen.blit(self.figureK, (j * 80, i * 80))
                if self.matrix[i][j] == "KC": self.KC = self.screen.blit(self.figureKC, (j * 80, i * 80))
                if self.matrix[i][j] == "H": self.H = self.screen.blit(self.figureH, (j * 80, i * 80))
                if self.matrix[i][j] == "HC": self.HC = self.screen.blit(self.figureHC, (j * 80, i * 80))
                if self.matrix[i][j] == "W1": self.W1 = self.screen.blit(self.figureW, (j * 80, i * 80))
                if self.matrix[i][j] == "W2": self.W2 = self.screen.blit(self.figureW, (j * 80, i * 80))
                if self.matrix[i][j] == "WC1": self.WC1 = self.screen.blit(self.figureWC, (j * 80, i * 80))
                if self.matrix[i][j] == "WC2": self.WC2 = self.screen.blit(self.figureWC, (j * 80, i * 80))
                if self.matrix[i][j] == "G1": self.G1 = self.screen.blit(self.figureG, (j * 80, i * 80))
                if self.matrix[i][j] == "G2": self.G2 = self.screen.blit(self.figureG, (j * 80, i * 80))
                if self.matrix[i][j] == "GC1": self.GC1 = self.screen.blit(self.figureGC, (j * 80, i * 80))
                if self.matrix[i][j] == "GC2": self.GC2 = self.screen.blit(self.figureGC, (j * 80, i * 80))
                if self.matrix[i][j] == "S1": self.S1 = self.screen.blit(self.figureS, (j * 80, i * 80))
                if self.matrix[i][j] == "S2": self.S2 = self.screen.blit(self.figureS, (j * 80, i * 80))
                if self.matrix[i][j] == "SC1": self.SC1 = self.screen.blit(self.figureSC, (j * 80, i * 80))
                if self.matrix[i][j] == "SC2": self.SC2 = self.screen.blit(self.figureSC, (j * 80, i * 80))
                if pg.mouse.get_pos()[0] / 80 < 8: pg.draw.rect(self.screen, (100, 120, 200),
                             pg.Rect(int(pg.mouse.get_pos()[0] / 80) * 80, int(pg.mouse.get_pos()[1] / 80) * 80, 80,
                                     80), 4)
        try:
            pg.draw.rect(self.screen, (200, 40, 40), pg.Rect(self.selected[0].get("h") * 80, self.selected[0].get("v") * 80, 80, 80), 2)
        except: pass

        if self.player % 2 == 0:
            self.screen.blit(pg.font.SysFont('Times New Roman', 48).render(("White turn"), True, (230, 230, 100)), (648, 10))
        else:
            self.screen.blit(pg.font.SysFont('Times New Roman', 48).render(("Black turn"), True, (230, 230, 100)), (648, 570))

        pg.display.flip()

    def loadData(self):
        img_dir = path.join(path.dirname(__file__), "data/")
        self.figureW = pg.image.load(img_dir + "w.png")
        self.figureWC = pg.image.load(img_dir + "wc.png")
        self.figureP = pg.image.load(img_dir + "p.png")
        self.figurePC = pg.image.load(img_dir + "pc.png")
        self.figureG = pg.image.load(img_dir + "g.png")
        self.figureGC = pg.image.load(img_dir + "gc.png")
        self.figureK = pg.image.load(img_dir + "k.png")
        self.figureKC = pg.image.load(img_dir + "kc.png")
        self.figureS = pg.image.load(img_dir + "s.png")
        self.figureSC = pg.image.load(img_dir + "sc.png")
        self.figureH = pg.image.load(img_dir + "h.png")
        self.figureHC = pg.image.load(img_dir + "hc.png")

    def firstMakeMatrix(self):
        self.matrix = []
        self.drawLabel = []

        for i in range(8):
            self.matrix.append([])
            for j in range(8):
                self.matrix[i].append("O")

        self.matrix[0][0] = "W1"
        self.matrix[0][1] = "S1"
        self.matrix[0][2] = "G1"
        self.matrix[0][3] = "K"
        self.matrix[0][4] = "H"
        self.matrix[0][5] = "G2"
        self.matrix[0][6] = "S2"
        self.matrix[0][7] = "W2"
        self.matrix[1][0] = "P1"
        self.matrix[1][1] = "P2"
        self.matrix[1][2] = "P3"
        self.matrix[1][3] = "P4"
        self.matrix[1][4] = "P5"
        self.matrix[1][5] = "P6"
        self.matrix[1][6] = "P7"
        self.matrix[1][7] = "P8"

        self.matrix[6][0] = "PC1"
        self.matrix[6][1] = "PC2"
        self.matrix[6][2] = "PC3"
        self.matrix[6][3] = "PC4"
        self.matrix[6][4] = "PC5"
        self.matrix[6][5] = "PC6"
        self.matrix[6][6] = "PC7"
        self.matrix[6][7] = "PC8"
        self.matrix[7][0] = "WC1"
        self.matrix[7][1] = "SC1"
        self.matrix[7][2] = "GC1"
        self.matrix[7][3] = "KC"
        self.matrix[7][4] = "HC"
        self.matrix[7][5] = "GC2"
        self.matrix[7][6] = "SC2"
        self.matrix[7][7] = "WC2"

        for i in range(8):
            self.drawLabel.append([])
            for j in range(8):
                self.drawLabel[i].append(0)

while True:
    if __name__ == "__main__":
        main()
