# Problem 1.5
## 下列程序给出了该问题的一个比较初步的解，事实上，在程序运行中，由于计算A与B的衰变并不是同时进行的，总粒子数会不断减少。在进行了300次循环后，A=49.869，B=49.629，A+B=99.498，大致可以接受这样的损失。

    #-*-coding:UTF-8-*-
    import numpy as np
    import matplotlib.pyplot as plt
    class particles(object):
        def __init__ (self, name, value, ratio):
            self.name = name
            self.value = value
            self.ratio = ratio
        def getnumber(self):
            print self.name, "=", self.value
        def decay(self, others):
            self.value=self.value+(others.value/others.ratio-self.value/self.ratio)*0.01
    A = particles('A', 100, 1)
    B = particles('B', 0, 1)
    t = 0
    x, y, z = [], [], []
    while abs(A.value-B.value)>0.01:
        t+=0.01
        print "After 0.01 seconds, %f seconds have passed" %t
        A.decay(B)
        B.decay(A)
        A.getnumber()
        B.getnumber()
