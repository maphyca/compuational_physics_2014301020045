import random
import math
import matplotlib.pyplot as plt
fv = 200  # fieldofvision
n = 500  # number of fishes
m = 100  # number of simulations
x0 = 0  # initial positon
h0 = 0  # initial altitude
xot = 60000  # x of target
hot = 500  # h of target
y0 = 10000  # ratio of air density changing
b0 = 0.1  # ratio of air drag
ea = 1  # ratio of equivalent distance
ev = 1  # ratio of equivalent distance
vfx = 50  # speed of wind
vfy = 0   # speed of wind
g0 = 9.8  # gravity
size = 10  # step size of calculation
step = 100  # step size of simluations


def food(m):
    return 1000 / (m + 100)


def ed(A, B):  # equivalent distance
    return math.hypot(ev * (A.v - B.v), ea * (A.a - B.a))


class fish(object):

    def __init__(self, jam=0.1,):
        self.jam = jam
        self.n = 0
        self.v = 0
        self.a = 0
        self.step = step
        self.gv = 0
        self.ga = 0
        self.fv = 0
        self.fa = 0

    def ini(self):  # iniltialize
        self.ffood = 0
        self.gfood = 0

    def getfood(self):
        return food(self.getdistance())

    def getdistance(self):
        return distance(self.v, self.a)

    def foraging(self):
        for io in range(5):
            self.nv = self.v + self.step * random.uniform(-1, 1)
            if random.uniform(-1, 1) > 0:
                self.na = self.a + 0.01 * (random.uniform(self.a, 90) - self.a)
            else:
                self.na = self.a + 0.01 * (self.a - random.uniform(0, self.a))
            if distance(self.nv, self.na) < self.getdistance():
                break
            else:
                io += 1
        self.v, self.a = self.nv, self.na

    def gather(self):
        self.g = random.uniform(0, 1)
        self.nv += self.g * (self.gv - self.v),
        self.na += self.g * (self.ga - self.a)

    def follow(self):
        self.f = random.uniform(0, 1)
        self.nv += self.f * (self.fv - self.v)
        self.na += self.f * (self.fa - self.a)

    def boardcast(self):
        if self.getfood() > board.food:
            board.food = self.getfood()
            board.v = self.v
            board.a = self.a
        if (self.v < board.v and self.getdistance() < 100):
            board.lowestv = self.v


class board(object):

    def __init__(self):
        self.v = 0
        self.a = 0
        self.getfood = 0
        self.lowestv = 200000


def distance(v, a):
    vx = v * math.cos(a)
    vy = v * math.sin(a)
    x = x0
    h = h0
    b = b0
    g = g0
    while not (vy < 0 and h0 == hot):
        kx1 = fx(vx, vy, b)
        ky1 = fy(vx, vy, b, g)
        x += vx * size
        h += vy * size
        vx += kx1 * size
        vy += ky1 * size
        g = g0 * math.pow(((6371000 + h) / (6371000 + h0)), 2)
        b = b0 * math.exp(h / y0)
    return x - xot


def fx(x, y, b):
    return -b * math.hypot((vfx - x), (vfy - y)) * (vfx - x)


def fy(x, y, b, g):
    return -b * math.hypot((vfx - x), (vfy - y)) * (vfy - y) - g

board = board()
Group = []
Groupv = []
Groupa = []
Groupfood = []
plt.figure(figsize=(4, 4))
ax1 = plt.subplot2grid((3, 4), (0, 0), rowspam=3)
ax2 = plt.subplot2grid((1, 1), (3, 0), rowspan=1)
ax3 = plt.subplot2grid((1, 1), (3, 1), rowspan=1)
ax4 = plt.subplot2grid((1, 1), (3, 2), rowspan=1)
ax5 = plt.subplot2grid((1, 1), (3, 3), rowspan=1)
for i in range(n):
    Group.append(fish())
    i += 1
for s in range(m):
    for i in range(n):
        Group[i].getfood()
        for j in range(i + 1, n):
            if ed(Group[i], Group[j]) < fv:
                Group[i].n += 1
                Group[j].n += 1
                Group[i].ga += Group[j].a
                Group[j].ga += Group[i].a
                Group[i].gv += Group[j].v
                Group[j].gv += Group[i].v
            if Group[j].food > Group[i].food:
                Group[i].ffood = Group[j].food
                Group[i].fa = Group[j].a
                Group[i].fv = Group[j].v
            else:
                Group[j].ffood = Group[i].food
                Group[j].fa = Group[i].a
                Group[j].fv = Group[i].v
        Group[i].gfood = food(distance(Group[i].gv / n, Group[i].ga / n))
        Groupv.append(Group[i].v)
        Groupa.append(Group[i].a)
        Groupfood.append(Group[i].food)
        if Group[i].gfood > Group[i].food:
            Group[i].gather()
        elif Group[i].ffood > Group[i].food:
            Group[i].follow()
        else:
            Group[i].foraging()
        Group[i].ini()
    plt.sca(ax1)
    plt.scatter(
        Groupv,
        Groupa,
        s=20,
        c=Groupfood,
        marker=(5, 3),
        alpha=0.8,
        lw=2,
        facecolors="none")
    if s == (m / 4 - 1):
        plt.sca(ax2)
        plt.scatter(
            Groupv,
            Groupa,
            s=20,
            c=Groupfood,
            marker=(5, 3),
            alpha=0.8,
            lw=2,
            facecolors="none")
    if s == (m / 2 - 1):
        plt.sca(ax3)
        plt.scatter(
            Groupv,
            Groupa,
            s=20,
            c=Groupfood,
            marker=(5, 3),
            alpha=0.8,
            lw=2,
            facecolors="none")
    if s == (3 * m / 4) - 1:
        plt.sca(ax4)
        plt.scatter(
            Groupv,
            Groupa,
            s=20,
            c=Groupfood,
            marker=(5, 3),
            alpha=0.8,
            lw=2,
            facecolors="none")
    if s == m - 1:
        plt.sca(ax5)
        plt.scatter(
            Groupv,
            Groupa,
            s=20,
            c=Groupfood,
            marker=(5, 3),
            alpha=0.8,
            lw=2,
            facecolors="none")
