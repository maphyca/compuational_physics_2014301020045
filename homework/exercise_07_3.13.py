import math
step = 0.04
g=9.8
import matplotlib.pyplot as plt

class oscillation:
    def __init__(self,q):
        self.l = 9.8
        self.q = q
        self.omega = 0
        self.theta = 0.2
        self.t = 0
    def oscillate(self):
        self.f=1.2*math.sin(2/3*self.t)
        self.omega=self.omega-((g/self.l)*math.sin(self.theta)+self.q*self.omega-self.f)*step
        self.theta=self.theta+self.omega*step

        self.t+=step
plt.figure()
A=oscillation(0.5)
B=oscillation(0.5001)
theta=[]
omega=[]
t=[]
for i in range(10000):
    A.oscillate()
    B.oscillate()
    theta.append((B.theta-A.theta))
    omega.append(B.omega-A.omega)
    t.append(A.t)
    plt.plot(t,theta)
plt.show()