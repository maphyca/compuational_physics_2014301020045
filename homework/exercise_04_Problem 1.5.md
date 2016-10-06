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
    while abs(A.value-B.value)>0.01:
        t+=0.01
        print "After 0.01 seconds, %f seconds have passed" %t
        A.decay(B)
        B.decay(A)
        A.getnumber()
        B.getnumber()

## 引入newvalue属性后，解决了微分近似时计算的不同步问题，以下给出了解决该问题后的程序，该程序附带一个图像结果，给出了A与B的随时间变化的具体趋势

    #-*-coding:UTF-8-*-
    from scipy.integrate import odeint
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
            self.newvalue=self.value+(others.value/others.ratio-self.value/self.ratio)*0.01
        def update(self):
            self.value = self.newvalue

    A = particles('A', 100, 1)
    B = particles('B', 0, 1)
    ti = 0
    def decay(w, t, a):
        # 给出比例系数a计算出
        # dNA/dt, dNB/dt的值
        x, y=w
        return np.array([y/a-x/a, x/a-y/a])

    t = np.arange(0, 5, 0.01) # 创建时间点
    # 调用ode对Decay进行求解
    track = odeint(decay, (100, 0), t, (1,))
    # 绘图
    plt.figure(figsize=(10,6))
    plt.plot(t,track[:,0], label='Value of A', color="red",linewidth=2)
    plt.plot(t,track[:,1], label='Value of B', color="blue",linewidth=2)
    plt.xlabel("Time(s)")
    plt.ylabel("Values")
    plt.legend()
    plt.show()

    while abs(A.value-B.value)>0.01:
        ti+=0.01
        print "After 0.01 seconds, %f seconds have passed" %ti
        A.decay(B)
        B.decay(A)
        A.update()
        B.update()
        A.getnumber()
        B.getnumber()
